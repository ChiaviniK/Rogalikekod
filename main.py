import pgzrun
import math
import random
from pygame import Rect
WIDTH = 800
HEIGHT = 600
TILE_SIZE = 64
class AnimatedSprite:
    def __init__(self, x, y, anim_frames_idle, anim_frames_move, speed):
        self.x = x
        self.y = y
        self.anim_frames_idle = anim_frames_idle
        self.anim_frames_move = anim_frames_move
        self.current_animation = self.anim_frames_idle
        self.frame_index = 0
        self.animation_timer = 0
        self.animation_speed = 0.15
        self.speed = speed
        self.moving = False
        self.target_x, self.target_y = x, y
        self.actor = Actor(self.current_animation[self.frame_index], (self.x, self.y))
        self.actor.pos = (self.x, self.y)
    def update_animation(self, dt):
        self.animation_timer += dt
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.frame_index = (self.frame_index + 1) % len(self.current_animation)
            self.actor.image = self.current_animation[self.frame_index]
    def draw(self):
        self.actor.draw()
    def set_animation(self, animation_type):
        new_animation = self.anim_frames_move if animation_type == "move" else self.anim_frames_idle
        if new_animation != self.current_animation:
            self.current_animation = new_animation
            self.frame_index = 0
            self.animation_timer = 0
class Player(AnimatedSprite):
    def __init__(self, x, y):
        idle_frames = ['player_idle_0', 'player_idle_1']
        move_frames = [f'player_move_{i}' for i in range(8)]
        super().__init__(x, y, idle_frames, move_frames, 250)
    def update(self, dt):
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
                self.set_animation("idle")
        else:
            self.set_animation("idle")
    def move_to_tile(self, tx, ty):
        if not self.moving:
            self.target_x = tx * TILE_SIZE + TILE_SIZE / 2
            self.target_y = ty * TILE_SIZE + TILE_SIZE / 2
            self.moving = True
class Enemy(AnimatedSprite):
    def __init__(self, x, y, min_x_tile, max_x_tile, min_y_tile, max_y_tile):
        idle_frames = ['enemy_idle_0', 'enemy_idle_1']
        move_frames = [f'enemy_move_{i}' for i in range(8)]
        super().__init__(x, y, idle_frames, move_frames, 120)
        self.min_x_tile = min_x_tile
        self.max_x_tile = max_x_tile
        self.min_y_tile = min_y_tile
        self.max_y_tile = max_y_tile
        self.move_timer = 0
        self.move_interval = 2.0
        self.set_random_target()
    def set_random_target(self):
        new_tx = random.randint(self.min_x_tile, self.max_x_tile)
        new_ty = random.randint(self.min_y_tile, self.max_y_tile)
        self.target_x = new_tx * TILE_SIZE + TILE_SIZE / 2
        self.target_y = new_ty * TILE_SIZE + TILE_SIZE / 2
        self.moving = True
        self.set_animation("move")
    def update(self, dt):
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
                self.set_animation("idle")
        else:
            self.move_timer += dt
            if self.move_timer >= self.move_interval:
                self.move_timer = 0
                self.set_random_target()
            self.set_animation("idle")
game_state = "MENU"
player = None
enemies = []
menu_buttons = []
sound_on = True
def init_game():
    global player, enemies
    player = Player(WIDTH / 2, HEIGHT / 2)
    enemies = []
    enemies.append(Enemy(TILE_SIZE * 2 + TILE_SIZE / 2, TILE_SIZE * 2 + TILE_SIZE / 2, 1, 3, 1, 3))
    max_tile_x = (WIDTH // TILE_SIZE) - 1
    max_tile_y = (HEIGHT // TILE_SIZE) - 1
    enemies.append(Enemy(WIDTH - TILE_SIZE * 2 - TILE_SIZE / 2, HEIGHT - TILE_SIZE * 2 - TILE_SIZE / 2,
                         max_tile_x - 3, max_tile_x - 1, max_tile_y - 3, max_tile_y - 1))
def draw_menu():
    screen.fill((0, 0, 0))
    screen.draw.text("Roguelike Simples", center=(WIDTH / 2, HEIGHT / 4), color="white", fontsize=60)
    start_button_rect = Rect(WIDTH / 2 - 100, HEIGHT / 2 - 30, 200, 60)
    exit_button_rect = Rect(WIDTH / 2 - 100, HEIGHT / 2 + 50, 200, 60)
    menu_buttons.clear()
    menu_buttons.append({'rect': start_button_rect, 'text': "Começar Jogo", 'action': start_game})
    menu_buttons.append({'rect': exit_button_rect, 'text': "Saída", 'action': quit_game})
    for button in menu_buttons:
        screen.draw.filled_rect(button['rect'], (50, 100, 200))
        screen.draw.text(button['text'], center=button['rect'].center, color="white", fontsize=30)
def draw_game():
    screen.fill((50, 50, 50))
    for x in range(0, WIDTH, TILE_SIZE):
        screen.draw.line((x, 0), (x, HEIGHT), (70, 70, 70))
    for y in range(0, HEIGHT, TILE_SIZE):
        screen.draw.line((0, y), (WIDTH, y), (70, 70, 70))
    if player:
        player.draw()
    for enemy in enemies:
        enemy.draw()
def update_game(dt):
    if player:
        player.update(dt)
        for enemy in enemies:
            enemy.update(dt)
            if player.actor.colliderect(enemy.actor):
                global game_state
                game_state = "GAME_OVER"
                if sound_on:
                    try:
                        sounds.game_over.play()
                    except AttributeError:
                        print("Atenção: Arquivo de som 'game_over.wav' não encontrado na pasta 'sounds'.")
def start_game():
    global game_state
    game_state = "PLAYING"
    init_game() 
def quit_game():
    exit()
def draw():
    if game_state == "MENU":
        draw_menu()
    elif game_state == "PLAYING":
        draw_game()
    elif game_state == "GAME_OVER":
        screen.fill((0,0,0))
        screen.draw.text("Fim de Jogo!", center=(WIDTH / 2, HEIGHT / 2 - 50), color="red", fontsize=80)
        screen.draw.text("Pressione ESC para retornar ao menu", center=(WIDTH / 2, HEIGHT / 2 + 50), color="white", fontsize=30)
def update(dt):
    if game_state == "PLAYING":
        update_game(dt)
def on_mouse_down(pos):
    if game_state == "MENU":
        for button in menu_buttons:
            if button['rect'].collidepoint(pos):
                button['action']()
                break
    elif game_state == "PLAYING":
        target_tile_x = pos[0] // TILE_SIZE
        target_tile_y = pos[1] // TILE_SIZE
        if 0 <= target_tile_x < WIDTH // TILE_SIZE and 0 <= target_tile_y < HEIGHT // TILE_SIZE:
            if player:
                player.move_to_tile(target_tile_x, target_tile_y)
    elif game_state == "GAME_OVER":
        pass
def on_key_down(key):
    global game_state
    if game_state == "GAME_OVER" and key == keys.ESCAPE:
        game_state = "MENU"
pgzrun.go()
