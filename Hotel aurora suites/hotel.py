#Cadastro
print('🌅 Bem vindo ao hotel Aurora Suítes 🌅... Deseja fazer uma reserva ?📝')
reserva = int(input(f'''
1 - Sim 😍
2 - Não 😣
'''))
if reserva == 1:
    #valores = [0 , 100, 150, 250]
    print('Escolha a quantidade de hospedes: ')
    hospedes = int(input(f'''
    1 - Quarto para uma pessoa 
    2 - Quarto para duas pessoas
    3 - Quarto para três pessoas
    '''))

    if hospedes == 1:
        hospede0 = input('Digite o nome do hospede: ')
        idade0 = int(input('Digite a idade: '))
        documento0 = int(input('Digite um documento: '))
        # dias = int(input('Dias'))
        # calc = valores[hospedes] * dias
        # print('Rs', calc)

    elif hospedes == 2:
        hospede1_1 = input('Digite o nome do 1 hospede: ')
        idade1_1 = int(input('Digite a idade: '))
        documento1_1 = int(input('Digite um documento: '))
        hospede1_2 = input('Digite o nome do 2 hospede: ')
        idade1_2 = int(input('Digite a idade: '))
        documento1_2 = int(input('Digite um documento: '))

    else:
        hospede2_1 = input('Digite o nome do 1 hospede: ')
        idade2_1 = int(input('Digite a idade: '))
        documento2_1 = int(input('Digite um documento: '))
        hospede2_2 = input('Digite o nome do 2 hospede: ')
        idade2_2 = int(input('Digite a idade: '))
        documento2_2 = int(input('Digite um documento: '))
        hospede2_3 = input('Digite o nome do 3 hospede: ')
        idade2_3 = int(input('Digite a idade: '))
        documento2_3 = int(input('Digite um documento: '))

    print('Escolha o tipo de quarto')
    quartos = int(input(f'''
    1 - Simples - Diária R$100.00
    2 - Duplo - Diária R$150.00
    3 - Luxo - Diária R$250.00
    '''))
    valores = [0,100.00,150.00,250.00]
    dias = int(input("Quantos dias deseja se hospedar? "))
    calc = valores[quartos] * dias
    print('Sua estadia custará:', calc, 'Qual a forma de pagamento? ')
    fpagamento = [0, 'Pix', 'Cartão de crédito', 'Cartão de débito','Dinheiro']
    pagamento = int(input(f'''
    1 - Pix
    2 - Cartão de débito
    3 - Cartão de crédito
    4 - Dinheiro
    ''')) 
    print('A forma de pagamento é', fpagamento[pagamento])
    print('Aurora Suítes agradece a preferencia 🌅 🥰')

else: 
    print("Aurora Suítes agradece seu contato🥰")