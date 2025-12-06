import pygame
import random

# Inicialização do pygame
pygame.init()

# Tamanho da tela
largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("🐍 Jogo da Cobrinha")

# Cores
preto = (0, 0, 0)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
branco = (255, 255, 255)

# Variáveis do jogo
tamanho_quadrado = 20
velocidade = 9

clock = pygame.time.Clock()

def gerar_comida():
    x = round(random.randrange(0, largura - tamanho_quadrado) / tamanho_quadrado) * tamanho_quadrado
    y = round(random.randrange(0, altura - tamanho_quadrado) / tamanho_quadrado) * tamanho_quadrado
    return x, y

def desenhar_cobra(tamanho_quadrado, lista_cobra):
    for p in lista_cobra:
        pygame.draw.rect(tela, verde, [p[0], p[1], tamanho_quadrado, tamanho_quadrado])

def jogo():
    game_over = False
    game_close = False

    x = largura / 2
    y = altura / 2
    x_velocidade = 0
    y_velocidade = 0

    lista_cobra = []
    comprimento_cobra = 1

    comida_x, comida_y = gerar_comida()

    while not game_over:

        while game_close:
            tela.fill(preto)
            fonte = pygame.font.SysFont("Arial", 35)
            msg = fonte.render("Game Over! Pressione C para jogar de novo ou Q para sair.", True, branco)
            tela.blit(msg, [20, altura / 2])
            pygame.display.update()

            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if evento.key == pygame.K_c:
                        jogo()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_velocidade = -tamanho_quadrado
                    y_velocidade = 0
                elif evento.key == pygame.K_RIGHT:
                    x_velocidade = tamanho_quadrado
                    y_velocidade = 0
                elif evento.key == pygame.K_UP:
                    y_velocidade = -tamanho_quadrado
                    x_velocidade = 0
                elif evento.key == pygame.K_DOWN:
                    y_velocidade = tamanho_quadrado
                    x_velocidade = 0

        x += x_velocidade
        y += y_velocidade

        # Se bater na parede
        if x >= largura or x < 0 or y >= altura or y < 0:
            game_close = True

        tela.fill(preto)
        pygame.draw.rect(tela, vermelho, [comida_x, comida_y, tamanho_quadrado, tamanho_quadrado])

        lista_cobra.append([x, y])
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for parte in lista_cobra[:-1]:
            if parte == [x, y]:
                game_close = True

        desenhar_cobra(tamanho_quadrado, lista_cobra)

        pygame.display.update()

        # Se comer a comida
        if x == comida_x and y == comida_y:
            comida_x, comida_y = gerar_comida()
            comprimento_cobra += 1

        clock.tick(velocidade)

    pygame.quit()
    quit()

jogo()