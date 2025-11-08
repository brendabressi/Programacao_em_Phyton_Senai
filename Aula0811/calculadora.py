# peso = 65.00 # global 


# # 1º cria a função 
# def imc():
#     ''' Calcula o IMC '''
    
#     peso = 70 # float(input('Peso:')) # locais
#     altura  =   float(input('Altura:')) # locais
#     imc  =  peso / (altura ** 2)
#     print(imc)


# print(peso)
# print(peso)

# imc() # 2º chama para funcionar 

# def calculadora():
#     #variaveis locais (declaradas dentro da função)
#     while True:
#         n1 = float(input('n°>>: '))
#         op = input('+│ - │ * │ /')

#         if op =="+":
#             n2 = float(input('n°>>: '))
#             print('=',n1+n2)
#         elif op =="-":
#             n2 = float(input('n°>>: '))
#             print('=',n1-n2)
#         elif op =="*":
#             n2 = float(input('n°>>: '))
#             print('=',n1*n2)
#         elif op =="/":
#             n2 = float(input('n°>>: '))
#             print('=',n1/n2)
#         else:
#             print('Digite um número válido')
# calculadora()



# def soma(x, y):
#     return x + y


# print(soma(100,200))
# print(soma(10,20))
# print(soma(0,2))
# print(soma(1,10))

# horas extras do trabalhador

import colorama
from colorama import Fore, Back, Style, init
def valor_hora(salario, carga):
    return salario/carga


def hora_extra(valor_hora):
    return valor_hora * 1.5


def qua_hora_extra(hora_extra,quantidade):
    return hora_extra * quantidade


def salario_total(salario, qua_hora_extra):
    return salario +  qua_hora_extra


def sistema_rh():
    while True:    
        print('***SISTEMA RH***')
        salario = float(input('Salario: '))
        carga = float(input('Carga: '))
        hora_trab = valor_hora(salario, carga)
        print(Fore.RED + 'HORA DO TRABALHADOR R$', round(hora_trab,2) )
        print('-------------------------------')
        extra_50 =  hora_extra(hora_trab)
        print('HORA EXTRA VALOR R$', round(extra_50,2))
        print('-------------------------------')
        quantidade_extra =  float(input('Quantidade extra: '))
        qua_hr_extra = qua_hora_extra(extra_50,quantidade_extra)   
        print('R$', round(quantidade_extra,2)) 
        print('-------------------------------')
        salario_t = salario_total(salario,qua_hr_extra)
        print('R$', round(salario_t, 2))



sistema_rh()


input('digiter para sair: ')

# TESTE PROFESSORA

# import colorama
# from colorama import Fore, Back, Style, init

# init()
# def valor_hora(salario, carga):
#     return salario/carga

# def hora_extra(valor_hora):
#     return valor_hora * 1.5

# def qua_hora_extra(hora_extra,quantidade):
#     return hora_extra * quantidade

# def salario_total(salario, qua_hora_extra):
#     return salario +  qua_hora_extra

# def sistema_rh():
#     while True:    
#         print('***SISTEMA RH***')
#         salario = float(input(Style.BRIGHT+Back.BLACK + Fore.GREEN+'Salario: '))
#         carga = float(input(Style.BRIGHT+Back.BLACK + Fore.GREEN+'Carga: '))
#         hora_trab = valor_hora(salario, carga)
#         print(Style.BRIGHT+Back.BLACK + Fore.GREEN + 'HORA DO TRABALHADOR R$', round(hora_trab,2) )
#         print('-------------------------------')
#         extra_50 =  hora_extra(hora_trab)
#         print(Style.BRIGHT+Back.BLACK + Fore.GREEN+ 'HORA EXTRA VALOR R$', round(extra_50,2))
#         print('-------------------------------')
#         quantidade_extra =  float(input('Quantidade extra: '))
#         qua_hr_extra = qua_hora_extra(extra_50,quantidade_extra)   
#         print(Style.BRIGHT+Back.BLACK + Fore.GREEN + 'QUANTIDADE DE EXTRA HORA:', round(quantidade_extra,2)) 
        
#         print('-------------------------------')
#         salario_t = salario_total(salario,qua_hr_extra)
#         print(Style.BRIGHT+ Fore.YELLOW + Back.BLACK + 'SALARIO: R$', round(salario_t, 2))


# sistema_rh()

# input('digiter para sair: ')


