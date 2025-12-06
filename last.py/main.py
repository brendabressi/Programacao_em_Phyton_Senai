import pygame
import random
import time

# Inicializa o Pygame
pygame.init()

# Tamanho da tela
LARGURA_TELA = 600
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Pac-Man Profissional")

# Cores
PRETO = (0, 0, 0)
AMARELO = (255, 255, 0)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)
BRANCO = (255, 255, 255)
CINZA = (169, 169, 169)

# Fonte para pontuação
font = pygame.font.SysFont('Arial', 30)

# Definir Pac-Man
class PacMan(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, AMARELO, (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect.center = (300, 300)
        self.velocidade = 5

    def update(self, movimento):
        if movimento == 'esquerda':
            self.rect.x -= self.velocidade
        elif movimento == 'direita':
            self.rect.x += self.velocidade
        elif movimento == 'cima':
            self.rect.y -= self.velocidade
        elif movimento == 'baixo':
            self.rect.y += self.velocidade

# Definir Fantasmas
class Fantasma(pygame.sprite.Sprite):
    def __init__(self, cor, velocidade):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, LARGURA_TELA - 50)
        self.rect.y = random.randint(50, ALTURA_TELA - 50)
        self.velocidade = velocidade

    def update(self):
        movimento = random.choice(['esquerda', 'direita', 'cima', 'baixo'])
        if movimento == 'esquerda':
            self.rect.x -= self.velocidade
        elif movimento == 'direita':
            self.rect.x += self.velocidade
        elif movimento == 'cima':
            self.rect.y -= self.velocidade
        elif movimento == 'baixo':
            self.rect.y += self.velocidade

# Função para desenhar os pontos
def desenhar_pontos(pontos):
    for ponto in pontos:
        pygame.draw.circle(tela, BRANCO, ponto.center, ponto.width // 2)

# Função de colisão com pontos
def colisao_com_pontos(pacman, pontos, pontuacao):
    for ponto in pontos[:]:
        if pacman.rect.colliderect(ponto):
            pontos.remove(ponto)
            pontuacao += 10
    return pontuacao

# Função para desenhar o labirinto
def desenhar_labirinto():
    pygame.draw.rect(tela, CINZA, (50, 50, 500, 500), 5)
    pygame.draw.line(tela, CINZA, (50, 150), (550, 150), 5)
    pygame.draw.line(tela, CINZA, (50, 250), (550, 250), 5)
    pygame.draw.line(tela, CINZA, (50, 350), (550, 350), 5)
    pygame.draw.line(tela, CINZA, (50, 450), (550, 450), 5)
    pygame.draw.line(tela, CINZA, (150, 50), (150, 550), 5)
    pygame.draw.line(tela, CINZA, (250, 50), (250, 550), 5)
    pygame.draw.line(tela, CINZA, (350, 50), (350, 550), 5)
    pygame.draw.line(tela, CINZA, (450, 50), (450, 550), 5)

# Função principal do jogo
def jogo():
    pacman = PacMan()
    fantasmas = pygame.sprite.Group()
    for i in range(4):
        fantasmas.add(Fantasma(VERMELHO, 2))

    # Pontos
    pontos = [pygame.Rect(random.randint(100, 500), random.randint(100, 500), 10, 10) for _ in range(10)]
    
    # Contagem
    pontuacao = 0
    vidas = 3

    # Grupo de sprites
    todos_sprites = pygame.sprite.Group()
    todos_sprites.add(pacman)
    todos_sprites.add(fantasmas)

    # Clock e loop principal
    clock = pygame.time.Clock()
    game_over = False
    movimento = ''
    while not game_over:
        tela.fill(PRETO)
        
        # Verifica eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
        
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            movimento = 'esquerda'
        if teclas[pygame.K_RIGHT]:
            movimento = 'direita'
        if teclas[pygame.K_UP]:
            movimento = 'cima'
        if teclas[pygame.K_DOWN]:
            movimento = 'baixo'

        # Atualiza Pac-Man
        pacman.update(movimento)

        # Atualiza fantasmas
        fantasmas.update()

        # Colisão com pontos
        pontuacao = colisao_com_pontos(pacman, pontos, pontuacao)

        # Verifica colisão com fantasmas
        for fantasma in fantasmas:
            if pacman.rect.colliderect(fantasma.rect):
                vidas -= 1
                pacman.rect.center = (300, 300)
                if vidas == 0:
                    game_over = True

        # Desenha tudo
        desenhar_labirinto()
        desenhar_pontos(pontos)
        todos_sprites.draw(tela)

        # Exibe a pontuação e vidas
        texto_pontos = font.render(f"Pontos: {pontuacao}", True, BRANCO)
        tela.blit(texto_pontos, (10, 10))

        texto_vidas = font.render(f"Vidas: {vidas}", True, BRANCO)
        tela.blit(texto_vidas, (LARGURA_TELA - 120, 10))

        # Atualiza a tela
        pygame.display.update()

        # Controla a taxa de quadros
        clock.tick(30)

    # Tela de Game Over
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
