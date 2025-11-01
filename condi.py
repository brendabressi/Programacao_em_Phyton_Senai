# # Criando uma lista vazia
# lista_de_compras = []

# while True:
#     print("\n=== LISTA DE COMPRAS ===")
#     print("1 - Adicionar item")
#     print("2 - Remover item")
#     print("3 - Ver lista")
#     print("4 - Sair")

#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         item = input("Digite o nome do item: ")
#         lista_de_compras.append(item)
#         print(f"✅ '{item}' foi adicionado à lista.")

#     elif opcao == "2":
#         item = input("Digite o nome do item a remover: ")
#         if item in lista_de_compras:
#             lista_de_compras.remove(item)
#             print(f"❌ '{item}' foi removido.")
#         else:
#             print("⚠️ Esse item não está na lista.")

#     elif opcao == "3":
#         print("\n🧾 Sua lista de compras:")
#         if len(lista_de_compras) == 0:
#             print("(vazia)")
#         else:
#             for i, item in enumerate(lista_de_compras, start=1):
#                 print(f"{i}. {item}")

#     elif opcao == "4":
#         print("👋 Saindo... até mais!")
#         break

#     else:
#         print("Opção inválida! Tente novamente.")

# estoque = {
#     'frutas':{
#         'uvas':
#               {'quantidade':30,
#                'preço':10.55,
#                },
#         'bananas':{
#                 'quantidade':20,
#                 'preço':15.25

#         },
     
#         },
#     'eletronicos':{
#         'fone':{
#                 'quantidade':10,
#                 'preço':500.55
#         },
#         'iphone':{
#                 'quantidade':5,
#                 'preço':17000
#         }

#     }
    
#     }


# carrinho =  []
# total =  []

# senha =  '123'
# login = '@bea'

# dig_senha =  input('Digite sua senha: ')
# dig_login =  input('Digite seu login: ')

# if dig_login == login and dig_senha == senha:
#     print('Seja bem vindo(a))')
#     pedir  =  input('Deseja fazer o pedido: sim ou não?')
#     if pedir == 'sim':
#         print('estoque: ', 'estoque, escolha se produto: ')
#         secao = input('Digite a seção -  frutas ou eletronicos')
#         produto =  input(f'escolha o produto{estoque[secao]} ')
#         print('Produto:', estoque[secao][produto])
#         carrinho.append(produto)
#         total.append(estoque[secao][produto]['preço'])
        
#         estoque[secao][produto]['quantidade'] - 1
#         print(estoque)

#         print('CArrinho', carrinho)
#         print('R$', total)
#         print('------------------------')
#         formapag = ['1 PIX', '2 - CC', '3 - CD']
#         pag =  int(input('Digite a forma de pagamento: '))
#         print('FORMA DE PAGAMENTO', formapag[pag])

#     else:
#         print('Obrigada volte sempre')    
# else:
#     print('Algo foi digitado errado... tente novamente')

import random 

ppt_maquina  =  ['🧻','🪨','✂️']
ppt_jogador  =  ['🧻','🪨','✂️']

aleatorio = random.choice(ppt_maquina)
escolha  =  int(input('''
0 - 🧻
1 - 🪨
2 - ✂️
'''))

if aleatorio == ppt_jogador[escolha]:
    print('EMPATE!')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha])

elif aleatorio == '🧻'  and   ppt_jogador[escolha] == '🪨':
    print('O computador ganhou!')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha])    


elif aleatorio == '🪨' and  ppt_jogador[escolha] == '✂️':
    print('O computador ganhou!')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha]) 


elif aleatorio == '✂️'  and   ppt_jogador[escolha] == '🧻':
    print('O computador ganhou!')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha]) 




elif  ppt_jogador[escolha] == '🧻'  and  aleatorio == '🪨':
    print('Você ganhou!')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha])    

elif ppt_jogador[escolha] == '🪨'  and   aleatorio == '✂️':
    print('Você ganhou!')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha]) 


elif ppt_jogador[escolha] == '✂️'  and   aleatorio  == '🧻':
    print('Você ganhou!')
    print('A maquina escolheu', aleatorio)
    print('Você escolheu', ppt_jogador[escolha]) 



    









