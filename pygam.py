import pygame 



pygame.init()


tela =  pygame.display.set_mode([500,500])
run = True


while run:
      for eventos in pygame.event.get():
          if eventos.type  == pygame.QUIT:
               run = False     


      tela.fill('red')


      pygame.display.flip()



pygame.quit()  

import pygame 



pygame.init()


tela =  pygame.display.set_mode([500,500])
run = True


while run:
      for eventos in pygame.event.get():
          if eventos.type  == pygame.QUIT:
               run = False     


      tela.fill('red')


      pygame.draw.rect(tela, 'green', (15,20,10,10))
      pygame.draw.rect(tela, 'green', (150,5,10,10))
      pygame.draw.rect(tela, 'green', (78,15,10,10))
      pygame.draw.rect(tela, 'green', (90,25,10,10))
      pygame.draw.rect(tela, 'green', (255,45,10,10))
      l =  [1,2,3]
      for x in l:
        pygame.draw.rect(tela, 'green', (78,300,10,10))
        pygame.draw.rect(tela, 'green', (90,325,10,10))
        pygame.draw.rect(tela, 'green', (255,228,10,10))
           


      


      pygame.display.flip()



pygame.quit()      


# import pygame
# import sys

# pygame.init()

# width = 700
# height = 500

# screen = pygame.display.set_mode((width, height)) 

# quandrado =  pygame.Rect(350,200, 150,70)
# rectangulo2 = pygame.Rect(10,150, 50,50)

# clock =  pygame.time.Clock()

# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#            pygame.quit() 
#            sys.exit()
        
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 quandrado.move_ip([10,0])
#             if event.key == pygame.K_LEFT:
#                 quandrado.move_ip([-10,0])
#             if event.key == pygame.K_UP:
#                 quandrado.move_ip([0,-10])
#             if event.key == pygame.K_DOWN:
#                 quandrado.move_ip([0,10])     

        
#         screen.fill('red')
#         pygame.draw.rect(screen,('green'), quandrado)
#         pygame.draw.rect(screen,('white'), rectangulo2)
#         pygame.display.update()








# import pygame 
# import sys

# pygame.init()

# tela =  pygame.display.set_mode([500,500])
# # run = True

# quadrado   =  pygame.Rect(15,20,10,10)


# clock =  pygame.time.Clock()

# while True:
#       for eventos in pygame.event.get():
#           if eventos.type  == pygame.QUIT:
#             #    run = False 
#                pygame.quit()
#                sys.exit()       
      
#           if eventos.type == pygame.KEYDOWN:
#                if eventos.key  == pygame.K_RIGHT:
#                   quadrado.move_ip([10,0])
#                if eventos.key == pygame.K_LEFT:
#                     quadrado.move_ip([-10,0])  

#                if eventos.key == pygame.K_UP:
#                     quadrado.move_ip([0,-10])

#                if eventos.key == pygame.K_DOWN:
#                     quadrado.move_ip([0,10])            
#           tela.fill('red')
#           pygame.draw.rect(tela, 'green', quadrado)
      

   
#           pygame.display.update()   

      

# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()


# o que a estrutura(sintaticamente)? para que serve(contexto)? 
# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/
# 1 - cita a estrutura de código
# 2 - contextualiza 




#exemplo:
# 2 varáveis , uma defini a aaltura a outra a largura 
largura, altura = 400, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Labirinto")


preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)


tamanho_celula = 40
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


x, y = 1 * tamanho_celula, 1 * tamanho_celula
velocidade = 40

def desenhar_labirinto():
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            cor = preto if labirinto[linha][coluna] == 1 else branco
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))


executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False


    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y


    tela.fill(branco)

    
    desenhar_labirinto()
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))


    pygame.display.flip()


    pygame.time.Clock().tick(10)


pygame.quit()
