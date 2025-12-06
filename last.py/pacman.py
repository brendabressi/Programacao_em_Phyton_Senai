import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA_TELA = 600
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pac-Man Simplificado")

# Cores
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)

# Definindo Pac-Man
pacman = pygame.Rect(300, 300, 30, 30)
pacman_velocidade = 5

# Definindo os fantasmas
fantasmas = [pygame.Rect(random.randint(0, LARGURA_TELA - 30), random.randint(0, ALTURA_TELA - 30), 30, 30) for _ in range(3)]
fantasma_velocidade = 2

# Definindo pontos
pontos = [pygame.Rect(random.randint(50, LARGURA_TELA - 50), random.randint(50, ALTURA_TELA - 50), 10, 10) for _ in range(5)]
pontuacao = 0

# Fonte para exibir a pontuação
font = pygame.font.SysFont('Arial', 30)

# Função para desenhar o Pac-Man
def desenhar_pacman():
    pygame.draw.circle(tela, AMARELO, pacman.center, pacman.width // 2)

# Função para desenhar os fantasmas
def desenhar_fantasmas():
    for fantasma in fantasmas:
        pygame.draw.rect(tela, VERMELHO, fantasma)

# Função para desenhar os pontos
def desenhar_pontos():
    for ponto in pontos:
        pygame.draw.circle(tela, BRANCO, ponto.center, ponto.width // 2)

# Função para mover o Pac-Man
def mover_pacman(teclas):
    if teclas[pygame.K_LEFT] and pacman.left > 0:
        pacman.x -= pacman_velocidade
    if teclas[pygame.K_RIGHT] and pacman.right < LARGURA_TELA:
        pacman.x += pacman_velocidade
    if teclas[pygame.K_UP] and pacman.top > 0:
        pacman.y -= pacman_velocidade
    if teclas[pygame.K_DOWN] and pacman.bottom < ALTURA_TELA:
        pacman.y += pacman_velocidade

# Função para mover os fantasmas
def mover_fantasmas():
    for fantasma in fantasmas:
        direcao = random.choice(['left', 'right', 'up', 'down'])
        if direcao == 'left':
            fantasma.x -= fantasma_velocidade
        if direcao == 'right':
            fantasma.x += fantasma_velocidade
        if direcao == 'up':
            fantasma.y -= fantasma_velocidade
        if direcao == 'down':
            fantasma.y += fantasma_velocidade

# Função principal do jogo
def jogo():
    global pontuacao
    clock = pygame.time.Clock()
    game_over = False

    while not game_over:
        tela.fill(PRETO)

        # Verifica os eventos (como o fechamento da janela)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True

        # Mover o Pac-Man
        teclas = pygame.key.get_pressed()
        mover_pacman(teclas)

        # Mover os fantasmas
        mover_fantasmas()

        # Colisão com pontos
        for ponto in pontos[:]:
            if pacman.colliderect(ponto):
                pontos.remove(ponto)
                pontuacao += 10

        # Colisão com fantasmas
        for fantasma in fantasmas:
            if pacman.colliderect(fantasma):
                game_over = True

        # Desenhar tudo
        desenhar_pacman()
        desenhar_fantasmas()
        desenhar_pontos()

        # Exibir a pontuação
        texto_pontos = font.render(f"Pontos: {pontuacao}", True, BRANCO)
        tela.blit(texto_pontos, (10, 10))

        # Atualizar a tela
        pygame.display.update()

        # Controla a taxa de quadros
        clock.tick(30)

    # Exibir "Game Over" e pontuação final
    tela.fill(PRETO)
    texto_game_over = font.render("GAME OVER", True, AZUL)
    tela.blit(texto_game_over, (LARGURA_TELA // 3, ALTURA_TELA // 3))
    texto_pontos_finais = font.render(f"Pontos finais: {pontuacao}", True, BRANCO)
    tela.blit(texto_pontos_finais, (LARGURA_TELA // 3, ALTURA_TELA // 2))
    pygame.display.update()
    pygame.time.delay(3000)

    pygame.quit()

# Iniciar o jogo
jogo()
