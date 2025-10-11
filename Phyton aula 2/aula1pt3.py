#Lista - n =[1, 3, 6, 5, 89, 7, 8]
lista_ = [1,2,3]
print(lista_[0])
lista_[0] = 100
print(lista_)

#Funções = nomeDaFunçao(lista)
#Alteram / Verificam o dado
#Métodos = nome.nomeMétodo

#adiciona um valor
lista_.append(10)
print(lista_)

#adiciona um valor na posição que eu quero
lista_.insert(1,200)
print(lista_)

#Adiciona varios valores no final da lista
lista_.extend(10,20,30,40)
print(lista_)

#adiciona varios valores no final da lista
lista_+=(10,20,30,40)

#remove o ultimo valor da lista
lista_.pop()
print(lista_)

#remove o valor do indice indicado da lista
lista_.pop(5)
print(lista_)

#remove o valor indicado
lista_.remove(200)
print(lista_)

#remove o índice
del lista_[0]
print(lista_)