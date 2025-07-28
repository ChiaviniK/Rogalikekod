import pgzrun
import math
import random
from pygame import Rect

# --- Configurações da Tela ---
WIDTH = 800
HEIGHT = 600
TILE_SIZE = 64 # Tamanho da célula da grade em pixels

# --- Classes de Personagem ---

class AnimatedSprite:
    """
    Classe base para personagens com animação de sprite.
    Gerencia frames de animação para estados parado e em movimento.
    """
    def __init__(self, x, y, anim_frames_idle, anim_frames_move, speed):
        self.x = x
        self.y = y
        self.anim_frames_idle = anim_frames_idle
        self.anim_frames_move = anim_frames_move
        self.current_animation = self.anim_frames_idle
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 0.15 # Velocidade da animação (tempo em segundos entre frames)
        self.speed = speed # Velocidade de movimento em pixels por segundo
        self.moving = False
        self.target_x, self.target_y = x, y # Coordenadas alvo para movimento suave
        self.actor = Actor(self.current_animation[self.frame_index], (self.x, self.y))
        # Centraliza o ator no tile, importante para movimento de grade
        self.actor.pos = (self.x, self.y)

    def update_animation(self, dt):
        """Atualiza o frame da animação com base no tempo."""
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.current_animation)
            self.actor.image = self.current_animation[self.frame_index]

    def draw(self):
        """Desenha o ator na tela."""
        self.actor.draw()

    def set_animation(self, animation_type):
        """Define o tipo de animação (idle ou move)."""
        new_animation = self.anim_frames_move if animation_type == "move" else self.anim_frames_idle
        if new_animation != self.current_animation:
            self.current_animation = new_animation
            self.frame_index = 0 # Reinicia a animação ao trocar
            self.animation_timer = 0


class Player(AnimatedSprite):
    """Classe para o personagem do jogador."""
    def __init__(self, x, y):
        idle_frames = ['player_idle_0', 'player_idle_1']
        move_frames = [f'player_move_{i}' for i in range(8)] # Adaptação para 8 frames
        super().__init__(x, y, idle_frames, move_frames, 250) # Velocidade do jogador um pouco maior

    def update(self, dt):
        """Atualiza a lógica do jogador e a animação."""
        self.update_animation(dt)
        if self.moving:
            # Calcula o vetor de movimento para o alvo
            dx = self.target_x - self.actor.x
            dy = self.target_y - self.actor.y
            distance = math.sqrt(dx**2 + dy**2)

            # Move o ator em direção ao alvo
            if distance > self.speed * dt:
                self.actor.x += (dx / distance) * self.speed * dt
                self.actor.y += (dy / distance) * self.speed * dt
                self.set_animation("move")
            else:
                # Chegou ao alvo
                self.actor.x = self.target_x
                self.actor.y = self.target_y
                self.moving = False
                self.set_animation("idle")
        else:
            self.set_animation("idle") # Garante animação 'idle' quando parado

    def move_to_tile(self, tx, ty):
        """Define um novo tile alvo para o movimento do jogador."""
        # Impede múltiplos movimentos antes de um terminar
        if not self.moving:
            # Calcula o centro do tile alvo
            self.target_x = tx * TILE_SIZE + TILE_SIZE / 2
            self.target_y = ty * TILE_SIZE + TILE_SIZE / 2
            self.moving = True


class Enemy(AnimatedSprite):
    """Classe para os personagens inimigos."""
    def __init__(self, x, y, min_x_tile, max_x_tile, min_y_tile, max_y_tile):
        idle_frames = ['enemy_idle_0', 'enemy_idle_1']
        move_frames = [f'enemy_move_{i}' for i in range(8)] # Adaptação para 8 frames
        super().__init__(x, y, idle_frames, move_frames, 120) # Velocidade do inimigo

        # Define a área de movimento do inimigo em coordenadas de tile
        self.min_x_tile = min_x_tile
        self.max_x_tile = max_x_tile
        self.min_y_tile = min_y_tile
        self.max_y_tile = max_y_tile

        self.move_timer = 0
        self.move_interval = 2.0 # Tempo em segundos para o inimigo escolher um novo alvo
        self.set_random_target()

    def set_random_target(self):
        """Define um novo tile alvo aleatório dentro da área do inimigo."""
        new_tx = random.randint(self.min_x_tile, self.max_x_tile)
        new_ty = random.randint(self.min_y_tile, self.max_y_tile)
        self.target_x = new_tx * TILE_SIZE + TILE_SIZE / 2
        self.target_y = new_ty * TILE_SIZE + TILE_SIZE / 2
        self.moving = True
        self.set_animation("move")

    def update(self, dt):
        """Atualiza a lógica do inimigo e a animação."""
        self.update_animation(dt)
        if self.moving:
            dx = self.target_x - self.actor.x
            dy = self.target_y - self.actor.y
            distance = math.sqrt(dx**2 + dy**2)

            if distance > self.speed * dt:
                self.actor.x += (dx / distance) * self.speed * dt
                self.actor.y += (dy / distance) * self.speed * dt
                self.set_animation("move")
            else:
                self.actor.x = self.target_x
                self.actor.y = self.target_y
                self.moving = False
                self.set_animation("idle") # Inimigo parado no alvo
        else:
            self.move_timer += dt
            if self.move_timer >= self.move_interval:
                self.move_timer = 0
                self.set_random_target() # Inimigo escolhe um novo alvo
            self.set_animation("idle") # Garante animação 'idle' quando parado

# --- Variáveis Globais de Jogo ---
game_state = "MENU" # Estados: "MENU", "PLAYING", "GAME_OVER"
player = None
enemies = []
menu_buttons = []
# music_on = True # Removido, pois não teremos música de fundo
sound_on = True # Controle para efeitos sonoros (mantido)

# --- Funções do Jogo ---

def init_game():
    """Inicializa os personagens e o estado do jogo para um novo início."""
    global player, enemies
    # Posição inicial do jogador no centro da tela
    player = Player(WIDTH / 2, HEIGHT / 2)
    enemies = []
    # Criação de inimigos com áreas de movimento restritas (em coordenadas de tile)
    # Inimigo 1: Área no canto superior esquerdo (tiles 1 a 3 em X e Y)
    enemies.append(Enemy(TILE_SIZE * 2 + TILE_SIZE / 2, TILE_SIZE * 2 + TILE_SIZE / 2, 1, 3, 1, 3))
    # Inimigo 2: Área no canto inferior direito (tiles que cobrem essa área)
    # Convertendo pixel para tile para os limites da área
    max_tile_x = (WIDTH // TILE_SIZE) - 1
    max_tile_y = (HEIGHT // TILE_SIZE) - 1
    enemies.append(Enemy(WIDTH - TILE_SIZE * 2 - TILE_SIZE / 2, HEIGHT - TILE_SIZE * 2 - TILE_SIZE / 2,
                         max_tile_x - 3, max_tile_x - 1, max_tile_y - 3, max_tile_y - 1))

def draw_menu():
    """Desenha o menu principal na tela."""
    screen.fill((0, 0, 0)) # Fundo preto
    screen.draw.text("Roguelike Simples", center=(WIDTH / 2, HEIGHT / 4), color="white", fontsize=60)

    # Definição dos retângulos dos botões
    start_button_rect = Rect(WIDTH / 2 - 100, HEIGHT / 2 - 30, 200, 60)
    # music_sound_button_rect = Rect(WIDTH / 2 - 100, HEIGHT / 2 + 50, 200, 60) # Removido
    exit_button_rect = Rect(WIDTH / 2 - 100, HEIGHT / 2 + 50, 200, 60) # Ajustado para subir

    menu_buttons.clear() # Limpa botões antigos
    menu_buttons.append({'rect': start_button_rect, 'text': "Começar Jogo", 'action': start_game})
    # Botão de som agora controla apenas sons, não música
    # menu_buttons.append({'rect': music_sound_button_rect, 'text': f"Sons: {'Ligado' if sound_on else 'Desligado'}", 'action': toggle_sound_only}) # Reativar se quiser apenas controle de som
    menu_buttons.append({'rect': exit_button_rect, 'text': "Saída", 'action': quit_game})

    # Desenha os botões na tela
    for button in menu_buttons:
        screen.draw.filled_rect(button['rect'], (50, 100, 200)) # Azul
        screen.draw.text(button['text'], center=button['rect'].center, color="white", fontsize=30)

def draw_game():
    """Desenha o cenário do jogo, jogador e inimigos."""
    screen.fill((50, 50, 50)) # Fundo cinza para o jogo

    # Desenha a grade para melhor visualização do movimento em tiles
    for x in range(0, WIDTH, TILE_SIZE):
        screen.draw.line((x, 0), (x, HEIGHT), (70, 70, 70))
    for y in range(0, HEIGHT, TILE_SIZE):
        screen.draw.line((0, y), (WIDTH, y), (70, 70, 70))

    if player:
        player.draw()
    for enemy in enemies:
        enemy.draw()


def update_game(dt):
    """Atualiza a lógica do jogo (movimento, colisões)."""
    if player:
        player.update(dt)
        for enemy in enemies:
            enemy.update(dt)
            # Detecção de colisão entre jogador e inimigo
            if player.actor.colliderect(enemy.actor):
                global game_state
                game_state = "GAME_OVER"
                if sound_on:
                    # Tenta tocar o som de game over
                    try:
                        sounds.game_over.play()
                    except AttributeError:
                        print("Atenção: Arquivo de som 'game_over.wav' não encontrado na pasta 'sounds'.")
                # music.stop() # Removido

def start_game():
    """Inicia o jogo a partir do menu."""
    global game_state
    game_state = "PLAYING"
    init_game() # Redefine o jogo
    # Removido: music.play("game_music", ...)

# Função para alternar APENAS sons (se desejar um botão para isso)
# def toggle_sound_only():
#     global sound_on
#     sound_on = not sound_on
#     print(f"Sons: {'Ligado' if sound_on else 'Desligado'}")


def quit_game():
    """Sai do jogo."""
    exit()

# --- Funções do Pygame Zero ---

def draw():
    """Função de desenho principal do Pygame Zero, chamada a cada frame."""
    if game_state == "MENU":
        draw_menu()
    elif game_state == "PLAYING":
        draw_game()
    elif game_state == "GAME_OVER":
        screen.fill((0,0,0))
        screen.draw.text("Fim de Jogo!", center=(WIDTH / 2, HEIGHT / 2 - 50), color="red", fontsize=80)
        screen.draw.text("Pressione ESC para retornar ao menu", center=(WIDTH / 2, HEIGHT / 2 + 50), color="white", fontsize=30)


def update(dt):
    """Função de atualização principal do Pygame Zero, chamada a cada frame."""
    if game_state == "PLAYING":
        update_game(dt)
    # Removido: update_music()

def on_mouse_down(pos):
    """Lida com cliques do mouse."""
    if game_state == "MENU":
        for button in menu_buttons:
            if button['rect'].collidepoint(pos):
                button['action']() # Executa a ação do botão clicado
                break
    elif game_state == "PLAYING":
        # Converte a posição do clique do mouse para coordenadas de tile
        target_tile_x = pos[0] // TILE_SIZE
        target_tile_y = pos[1] // TILE_SIZE
        # Garante que o clique seja dentro dos limites da grade
        if 0 <= target_tile_x < WIDTH // TILE_SIZE and 0 <= target_tile_y < HEIGHT // TILE_SIZE:
            if player:
                player.move_to_tile(target_tile_x, target_tile_y)
    elif game_state == "GAME_OVER":
        # Não faz nada com o clique do mouse no game over
        pass

def on_key_down(key):
    """Lida com o pressionar de teclas."""
    global game_state
    if game_state == "GAME_OVER" and key == keys.ESCAPE:
        game_state = "MENU"
        # music.stop() # Removido
        # Removido: music.play("menu_music", ...)

# Removido: Bloco de inicialização de música ao iniciar o jogo

# Inicia o loop principal do Pygame Zero
pgzrun.go()