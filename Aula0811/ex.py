# # ***1*** 

# # ***CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS.***
# def comparar_par_impar():

#     num1 = int(input('num1: '))
#     num2 = int(input('num1: '))
#     # Função que compara dois números e verifica se são par ou ímpar.
#     resultado1 = "par" if num1 % 2 == 0 else "ímpar"
#     resultado2 = "par" if num2 % 2 == 0 else "ímpar"
    
#     print(f"O primeiro número ({num1}) é {resultado1}.")
#     print(f"O segundo número ({num2}) é {resultado2}.")

# comparar_par_impar()
# # ***2***

# # ***CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.***
# def multiplicar_tres_numeros():
#     # Função que multiplica três números.
#     num1 = int(input('num1: '))
#     num2 = int(input('num2: '))
#     num3 = int(input('num3: '))
#     resultado = num1 * num2 * num3
#     print(f"A multiplicação de {num1}, {num2} e {num3} é {resultado}.")

# multiplicar_tres_numeros()
# # ***3***

# # ***CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.***
# def elevar_numero():
#     # Função que calcula a potência de um número.
#     base = int(input('num base: '))
#     expoente = int(input('num expoente: '))
#     resultado = base ** expoente
#     print(f"{base} elevado a {expoente} é {resultado}.")

# elevar_numero()
# # # ***4***

# # ***CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.***

# # ***5***
# def mensagem_personalizada():
#     # Função que verifica se a idade é 18 anos e exibe uma mensagem personalizada.
#     idade = int(input('Digite sua idade: '))
#     if idade == 18:
#         print("Você tem 18 anos, parabéns pela maioridade!")
#     else:
#         print("Sua idade é:", idade)

# mensagem_personalizada()
# # ***DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.***

# def calcular_idade():
#     # Função que calcula a idade de uma pessoa.
#     ano_nascimento = int(input('Digite o ano em que você nasceu(0000): '))
#     ano_atual = 2025
#     idade = ano_atual - ano_nascimento
#     print(f"Sua idade é: {idade} anos.")

# calcular_idade()
# # ***6***

# # ***DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.***

# def verificar_vitoria_brasil_copa_1999():
#     # Função simples para verificar se o Brasil ganhou a Copa de 1999.
#     resposta = input("O Brasil ganhou a Copa do Mundo Feminina de 1999? (Sim/Não): ")

#     if resposta == "Sim":
#         print("Correto! O Brasil ganhou a Copa de 1999!")
#     elif resposta == "Não":
#         print("Errado! O Brasil ganhou a Copa de 1999!")
#     else:
#         print("Resposta inválida. Por favor, responda com 'Sim' ou 'Não'.")

# verificar_vitoria_brasil_copa_1999()
# # ***7*** 

# ***DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.***  

# ***1 - Função -  cumprimentar o cliente***
def sistema_restaurante():
    resposta = input('Olá, seja bem vindo! Deseja fazer um pedido?')
    carrinho = []
    while resposta == 'Sim':
        lista = ['SALADA','MACARRONADA','SANDUICHE','SORVETE']
        pedido = int(input('''f
        O que deseja comer hoje?
        0 - Salada
        1 - Macarronada
        2 - Sanduiche
        3 - Sorvete'''))
        carrinho.append(lista[pedido])
        print('Você escolheu: ',carrinho)

        resposta = input('Deseja continuar o pedido?')
    else:
        print('Obrigado, volte sempre')

sistema_restaurante()
        

# ***2 - Função - restaurante***

# ***3 - Sugestão utilize listas  e loops***