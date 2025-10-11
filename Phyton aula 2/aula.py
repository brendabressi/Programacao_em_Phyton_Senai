n1 = 10
n2 = 20
print(n1,'-',n2,'=',n1 - n2)
print(n1,'+',n2,'=',n1 + n2)
print(n1,'/',n2,'=',n1 / n2) 
print(n1,'//',n2,'=',n1 // n2) 
print(10 % 20  )


nome = input('digite seu nome:')  
#  o imput naturalmente gera um texto, não pode ser número ou dado aritmédico
# int - inteiro
# float - numero com decimal
n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
print(n1 + n2)

#concatenação -- juntar dados

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
endereco = input('Digite seu endereco:  ')
curso = input('Curso: ')
salario = input(float(input('Digite seu salario: ')))

print('Nome: ',nome)
print('Sua idade é: ',idade)
print('Seu endereço é: ',endereco)
print('Seu curso é: ',curso)
print('Seu salário é',salario)
