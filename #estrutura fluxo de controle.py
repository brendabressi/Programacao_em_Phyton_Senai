# #estrutura fluxo de controle
# #finito
# try:
#     x  =  int(input('>')) 
#     n = 10
#     n2 = 0
#     print(n/n2)
# except ValueError as erro:
#     print(erro)
# except ZeroDivisionError as erro:
#     print(erro)    
# else:
#     print('erro não identificado ')

# finally:
#     print('fim de carregamento... ')  

# Exercício 1:
# Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

# try:
#     x = int(input('Digite um número inteiro'))
# except ValueError:
#     print('Você não digitou um número inteiro. Tente novamente')

# Exercício 2:
# Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

# try:
#     numero1 = float(input('Digite um número'))
#     numero2 = float(input('Digite um número'))
# except ValueError:
#     print('Parece que você não digitou um número....Tente novamente')
# except ZeroDivisionError:
#     print('Você não pode dividir por 0, tente novamente')
# finally:
#     print('Seu resultado é: ',numero1/numero2)


# Exercício 3:
# Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

try:
    li  = [1,2,3,4,5,6]
    indice = int(input('Digite uma posição: '))
    print('Valor da posição: ', indice,'é', li[indice])
except IndexError:
    print('Essa posição não existe, tente novamente')

