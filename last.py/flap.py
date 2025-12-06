import pygame
import random
import sys

pygame.init()

# Configurações da janela
LARGURA = 400
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Flappy Bird - Python")

# Cores
AZUL = (135, 206, 250)
AMARELO = (255, 255, 0)
VERDE = (0, 200, 0)

# Configurações do jogo
gravidade = 0.5
forca_pulo = -8
velocidade_canos = 3
espaco_canos = 150

# Passarinho
x_passaro = 60
y_passaro = 300
vel_y = 0
raio_passaro = 15

# Lista de canos
canos = []
def criar_cano():
    altura = random.randint(100, 400)
    canos.append([LARGURA, altura])

def mover_canos():
    for cano in canos:
        cano[0] -= velocidade_canos

def desenhar_canos():
    for cano in canos:
        pygame.draw.rect(TELA, VERDE, (cano[0], 0, 50, cano[1]))
        pygame.draw.rect(TELA, VERDE, (cano[0], cano[1] + espaco_canos, 50, ALTURA))

def colisao():
    for cano in canos:
        if x_passaro + raio_passaro > cano[0] and x_passaro - raio_passaro < cano[0] + 50:
            if y_passaro - raio_passaro < cano[1] or y_passaro + raio_passaro > cano[1] + espaco_canos:
                return True
    if y_passaro - raio_passaro <= 0 or y_passaro + raio_passaro >= ALTURA:
        return True
    return False

# Loop principal
clock = pygame.time.Clock()
criar_cano()
pontuacao = 0
fonte = pygame.font.SysFont("Arial", 32)

while True:
    clock.tick(60)
    TELA.fill(AZUL)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                vel_y = forca_pulo

    # Movimento do pássaro
    vel_y += gravidade
    y_passaro += vel_y

    # Criar canos
    if len(canos) == 0 or canos[-1][0] < 200:
        criar_cano()

    mover_canos()
    desenhar_canos()

    # Remover canos fora da tela
    if canos[0][0] < -60:
        canos.pop(0)
        pontuacao += 1

    # Desenhar pássaro
    pygame.draw.circle(TELA, AMARELO, (x_passaro, int(y_passaro)), raio_passaro)

    # Colisão
    if colisao():
        texto = fonte.render(f"Game Over! Pontos: {pontuacao}", True, (255, 0, 0))
        TELA.blit(texto, (50, ALTURA // 2))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    # Mostrar pontuação
    texto = fonte.render(str(pontuacao), True, (255, 255, 255))
    TELA.blit(texto, (10, 10))

    pygame.display.update() 