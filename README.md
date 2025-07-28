# 🎮 Roguelike Simples com Pygame Zero

Um jogo roguelike simples desenvolvido em Python usando a biblioteca Pygame Zero, seguindo rigorosos requisitos de projeto. Explore mas tome cuidado com os inimigos que rondam o território!

---

## ✨ Funcionalidades

* **Gênero Roguelike:** Visão de cima com movimento em grade suave.
* **Menu Principal Interativo:**
    * `Começar Jogo`: Inicia uma nova aventura.
    * `Saída`: Encerra o jogo.
    * *(Opcional: Se você recolocou o botão de controle de som)* `Sons Ligado/Desligado`: Alterna os efeitos sonoros do jogo.
* **Herói e Inimigos Animados:** Personagens com animações de sprite para movimento e estado parado.
* **Inimigos Perigosos:** Múltiplos inimigos com padrões de movimento em seu próprio território.
* **Mecânica de Colisão:** Detecta o contato entre o herói e os inimigos, levando ao "Fim de Jogo".
* **Interface Clara:** Design intuitivo e fácil de usar.
* **Código Otimizado:** Desenvolvido com foco em clareza, desempenho e aderência ao PEP8.

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.x**
* **PgZero** (Framework simplificado para jogos baseado em Pygame)
* **Módulos Padrão:** `math`, `random`
* **Pygame.Rect:** Importado especificamente para manipulação de retângulos.

---

## 🚀 Como Rodar o Jogo

Siga estas instruções para configurar e executar o jogo em sua máquina.

### Pré-requisitos

Certifique-se de ter o Python 3.x instalado em seu sistema.

### Instalação

1.  **Clone o Repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
    cd SEU_REPOSITORIO
    ```
    *(Substitua `SEU_USUARIO` e `SEU_REPOSITORIO` pelos seus dados do GitHub)*

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

Certifique-se de que seu diretório de projeto esteja organizado da seguinte forma:
