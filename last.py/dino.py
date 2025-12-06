import pygame
import random

# Inicializa o pygame
pygame.init()

# Configurações da tela
LARGURA = 600
ALTURA = 400
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo do Dinossauro")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
MARROM = (139, 69, 19)

# Definindo o dinossauro
dino_largura = 50
dino_altura = 50
dino_x = 50
dino_y = ALTURA - dino_altura - 20
dino_velocidade = 0
pulo_forca = -12

# Definindo obstáculos
obstaculo_largura = 20
obstaculo_velocidade = 5

# Criar o clock para o FPS
clock = pygame.time.Clock()

# Função para desenhar o dinossauro
def desenhar_dino(x, y):
    pygame.draw.rect(tela, MARROM, (x, y, dino_largura, dino_altura))

# Função para desenhar o obstáculo
def desenhar_obstaculo(x, y, largura, altura):
    pygame.draw.rect(tela, PRETO, (x, y, largura, altura))

# Função principal
def jogo():
    global dino_y, dino_velocidade, obstaculo_x, obstaculo_y, obstaculo_largura
    score = 0
    game_over = False
    obstaculo_x = LARGURA
    obstaculo_altura = random.randint(20, 50)  # Inicializando a altura do obstáculo corretamente
    obstaculo_y = ALTURA - obstaculo_altura - 20  # A posição do obstáculo depende da altura

    while not game_over:
        tela.fill(BRANCO)

        # Loop de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and dino_y == ALTURA - dino_altura - 20:
                    dino_velocidade = pulo_forca

        # Movimento do dinossauro
        dino_velocidade += 1  # Gravidade
        dino_y += dino_velocidade

        # Impede o dinossauro de cair abaixo do solo
        if dino_y > ALTURA - dino_altura - 20:
            dino_y = ALTURA - dino_altura - 20
            dino_velocidade = 0

        # Movimento do obstáculo
        obstaculo_x -= obstaculo_velocidade
        if obstaculo_x < -obstaculo_largura:
            obstaculo_x = LARGURA
            obstaculo_altura = random.randint(20, 50)  # Recalcula a altura do obstáculo
            obstaculo_y = ALTURA - obstaculo_altura - 20  # Atualiza a posição Y com a nova altura
            score += 1

        # Colisão com o obstáculo
        if dino_x + dino_largura > obstaculo_x and dino_x < obstaculo_x + obstaculo_largura:
            if dino_y + dino_altura > obstaculo_y:
                game_over = True

        # Desenhar dinossauro e obstáculo
        desenhar_dino(dino_x, dino_y)
        desenhar_obstaculo(obstaculo_x, obstaculo_y, obstaculo_largura, obstaculo_altura)

        # Mostrar pontuação
        font = pygame.font.SysFont('Arial', 30)
        texto = font.render(f'Pontuação: {score}', True, PRETO)
        tela.blit(texto, (10, 10))

        pygame.display.update()
        clock.tick(30)  # Controla o FPS (velocidade do jogo)

    # Fim de jogo
    font = pygame.font.SysFont('Arial', 50)
    texto_fim = font.render(f'Fim de Jogo! Pontuação: {score}', True, PRETO)
    tela.fill(BRANCO)
    tela.blit(texto_fim, (150, ALTURA // 3))
    pygame.display.update()
    pygame.time.wait(2000)  # Espera 2 segundos antes de fechar

    pygame.quit()

# Iniciar o jogo
jogo()