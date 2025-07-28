# 🎮 Roguelike Simples com Pygame Zero

Um jogo roguelike simples e divertido, desenvolvido em Python usando a biblioteca Pygame Zero. Neste projeto, o foco foi atender a requisitos específicos, incluindo animações de sprite detalhadas e um sistema de jogo roguelike baseado em grade. Explore o mapa, mas cuidado com os inimigos que rondam o território!

---

## ✨ Funcionalidades Principais

* **Gênero Roguelike:** O jogo apresenta uma visão de cima, com movimentação do personagem em uma grade, garantindo transições suaves entre os tiles.
* **Menu Principal Interativo:**
    * `Começar Jogo`: Inicia uma nova aventura.
    * `Saída`: Encerra o jogo.
* **Herói e Inimigos Animados:** Tanto o personagem principal quanto os inimigos possuem animações de sprite dinâmicas, que mudam ao se mover ou ao ficar parados.
* **Inimigos Perigosos:** Múltiplos inimigos com movimentos autônomos dentro de territórios definidos, representando um desafio para o jogador.
* **Mecânica de Colisão:** Implementação de detecção de colisão entre o herói e os inimigos, levando a um estado de "Fim de Jogo".
* **Interface Clara e Intuitiva:** Design simples e funcional, fácil de compreender e jogar.
* **Código Otimizado e Legível:** Desenvolvido com foco na clareza do código, bom desempenho e aderência às diretrizes do PEP8 para Python.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **PgZero** (Framework simplificado para desenvolvimento de jogos em Python, construído sobre Pygame)
* **Módulos Padrão do Python:** `math` (para cálculos de distância e movimento) e `random` (para a inteligência artificial dos inimigos).
* **Pygame.Rect:** Importado especificamente para manipulação eficiente de retângulos e detecção de colisões.

---

## 🚀 Como Rodar o Jogo

Siga estas instruções para configurar e executar o jogo em sua máquina local.

### Pré-requisitos

Certifique-se de ter o **Python 3.x** instalado em seu sistema.

### Instalação

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/ChiaviniK/Rogalikekod.git](https://github.com/ChiaviniK/Rogalikekod.git)
    cd Rogalikekod
    ```

2.  **Crie e Ative um Ambiente Virtual (Recomendado):**
    ```bash
    python -m venv .venv
    # No Windows:
    .venv\Scripts\activate
    # No macOS/Linux:
    source .venv/bin/activate
    ```

3.  **Instale as Dependências:**
    ```bash
    pip install pgzero
    ```

### Estrutura de Arquivos

Para que o jogo funcione corretamente, seu diretório de projeto clonado deve estar organizado da seguinte forma, com todos os assets necessários nas pastas corretas:

Rogalikekod/
├── main.py
├── images/
│   ├── player_idle_0.png
│   ├── player_idle_1.png
│   ├── player_move_0.png
│   ├── player_move_1.png
│   ├── player_move_2.png
│   ├── player_move_3.png
│   ├── player_move_4.png
│   ├── player_move_5.png
│   ├── player_move_6.png
│   ├── player_move_7.png
│   ├── enemy_idle_0.png
│   ├── enemy_idle_1.png
│   ├── enemy_move_0.png
│   ├── enemy_move_1.png
│   ├── enemy_move_2.png
│   ├── enemy_move_3.png
│   ├── enemy_move_4.png
│   ├── enemy_move_5.png
│   ├── enemy_move_6.png
│   └── enemy_move_7.png
└── sounds/
└── game_over.wav
# Não há música de fundo neste projeto para simplificar a execução.


### Executando o Jogo

Com o ambiente virtual ativado, execute o jogo usando o comando `pgzrun`:

```bash
pgzrun main.py
💡 Como Jogar
No Menu Inicial:

Clique no botão "Começar Jogo" para iniciar uma nova partida.

Clique no botão "Saída" para fechar o jogo a qualquer momento.

Durante o Jogo:

Use o mouse para clicar em qualquer parte da tela. Seu personagem (o herói) se moverá suavemente em direção ao ponto clicado, seguindo a grade do jogo.

Objetivo: Evite colidir com os inimigos. Se seu personagem tocar em um inimigo, o jogo terminará.

Na Tela de "Fim de Jogo":

Pressione a tecla ESC para retornar ao menu principal e começar uma nova partida.

👨‍💻 Contribuição
Contribuições são bem-vindas! Se você tiver sugestões de melhoria, encontrar bugs ou quiser adicionar novas funcionalidades, sinta-se à vontade para:

Fazer um fork (ramificação) deste repositório.

Criar uma nova branch para sua funcionalidade (git checkout -b feature/minha-melhoria).

Implementar suas alterações.

Comitar suas mudanças (git commit -m 'feat: Adiciona nova funcionalidade X').

Fazer push para a sua branch (git push origin feature/minha-melhoria).

Abrir um Pull Request detalhando suas alterações.

📄 Licença
Este projeto está licenciado sob a Licença MIT. Para mais detalhes, consulte o arquivo LICENSE no repositório.

📧 Contato
Se tiver dúvidas ou sugestões, entre em contato:

Luiz Chiavini - luizchiavini@gmail.com

GitHub: @ChiaviniK


---

### Principais Alterações e Melhorias:

1.  **Título e Introdução:** Deixei a introdução um pouco mais descritiva sobre o foco do projeto.
2.  **Funcionalidades:**
    * Removi a linha `*(Opcional: Se você recolocou o botão de controle de som)*` porque, com a ausência de música de fundo, o controle de som pode ser simplificado ou até mesmo dispensado no menu para focar na mecânica principal. Se você quiser um botão apenas para ligar/desligar *efeitos sonoros*, pode reativar a linha e mudar o texto para "Sons Ligado/Desligado".
    * Adicionei alguns detalhes sobre as animações serem "dinâmicas" e o foco no "controle PEP8".
3.  **Tecnologias Utilizadas:** Adicionei pequenas descrições sobre o uso de cada módulo/biblioteca.
4.  **Como Rodar o Jogo:**
    * Atualizei o `git clone` para o seu link exato do repositório (`https://github.com/ChiaviniK/Rogalikekod.git`).
    * Deixei a estrutura de arquivos mais detalhada, listando cada sprite individualmente para clareza e reforçando a ausência de músicas de fundo.
5.  **Como Jogar:** As instruções foram ajustadas para o controle de mouse e para a ausência de música de fundo.
6.  **Contato:** Preenchi com seu nome e e-mail que encontrei no seu perfil, além do link direto para seu GitHub. Se o e-mail estiver incorreto ou você preferir outro, por favor, me avise!

---

**Próximos Passos:**

1.  **Copie o Código:** Copie todo o conteúdo do bloco de código acima.
2.  **Vá para o GitHub:** Acesse seu repositório `https://github.com/ChiaviniK/Rogalikekod`.
3.  **Crie/Edite o README.md:**
    * Se você ainda não tem um `README.md`, clique em **"Add file"** > **"Create new file"** e nomeie o arquivo como `README.md`.
    * Se você já tem um `README.md` (mesmo que esteja vazio ou com o modelo anterior), clique no arquivo `README.md` e depois no ícone de lápis para editar.
4.  **Cole o Conteúdo:** Cole o conteúdo revisado no editor do GitHub.
5.  **Commit:** Role para baixo, adicione uma mensagem de commit (ex: "Atualiza README com instruções e detalhes do projeto") e clique em **"Commit changes"** (ou "Commit new file").

Com este README atualizado e as pastas `images` e `sounds` carregadas, seu projeto estará muito bem apresentado e pronto para ser compartilhado!

Me diga se tem mais alguma coisa em que posso ajudar!
