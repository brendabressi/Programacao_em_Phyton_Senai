# Importa a biblioteca para gerar números aleatórios
import random
# 1 - Função para criar um número aleatório entre 5 e 10
def numero_aleatorio():
    return random.randint(5, 10)

# 2 - Função para criar 3 números aleatórios
def tres_numeros_aleatorios():
    return [random.randint(1, 100) for _ in range(3)]

# 3 - Função para criar um número aleatório entre 10 a 30 utilizando range()
def numero_aleatorio_range():
    return random.randint(10, 31)

# 4 - Função para exibir uma contagem regressiva simples de 10 a 1
def contagem_regressiva():
    for i in range(10, 0, -1):
        print(i)
    print("Fogo!")

# 5 - Função para calcular a soma dos números pares até o número inserido pelo usuário
def soma_numeros_pares():
    numero = int(input("Digite um número inteiro positivo: "))
    soma = 0
    for i in range(2, numero + 1, 2):  # Vai de 2 até o número inserido, com intervalo de 2 (números pares)
        soma += i
    return soma

# 6 - Função para mostrar a tabuada de multiplicação de um número inserido
def tabuada():
    numero = int(input("Digite um número inteiro para ver a tabuada: "))
    for i in range(1, 11):  # Vai de 1 até 10
        print(f"{numero} x {i} = {numero * i}")

# 7 - Função para exibir números ímpares de 99 a 1 (contagem regressiva)
def numeros_impares_reversos():
    for i in range(99, 0, -2):  # Vai de 99 até 1, com intervalo de -2 para pegar apenas os ímpares
        print(i)