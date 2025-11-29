import os
import shutil



# with open('q','w') as arq:
#     os.mkdir('u')



# os.rename('t','t2')



# with os.scandir('t2') as entr:
#      for dados in entr:
#           print(dados.name)
        
# with os.scandir('t2') as entr:
#      for dados in entr:
#           if dados.is_dir():
#              print(dados.name)
        


# with os.scandir('C:/Users/Aluno/Downloads/Nova pasta/t2') as entr:
#      for dados in entr:
#           if 'arq.txt':
#              with open('arq.txt','r') as conte:
#                   conte.read()


# with os.scandir('teste') as entrada :
#        for n in entrada:
#               print(n) 
#               if 'teste.txt':
#                   with open('C:/Users/Aluno/Downloads/Nova pasta/teste/teste.txt', 'r')  as t:
#                     content = t.read()



# print(content)
            #  print(dados.name)



# l =  []


# with open('teste.txt','r') as arqui:
#     conteudo   =  arqui.read()
#     for n in conteudo:
#         l.append(n)
#         print(n)
#     print(l)



# shutil.rmtree('x')


# shutil.copytree('C:/Users/Aluno/Downloads/Nova pasta/teste', 'teste2.py')
#-----------------------------------------------------------------------------------------------------------------
# # Criando e escrevendo em um arquivo
# with open('exemplo.txt', 'w') as arquivo:
#     arquivo.write('Este é um exemplo de arquivo criado em Python.\n')

# # Lendo o conteúdo do arquivo
# with open('exemplo.txt', 'r') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)

#     import os

# # Criando um diretório
# diretorio = 'novo_diretorio'
# if not os.path.exists(diretorio):
#     os.makedirs(diretorio)
#     print(f'Diretório "{diretorio}" criado com sucesso!')
# else:
#     print(f'O diretório "{diretorio}" já existe.')

#     import os

# # Renomeando o diretório
diretorio_antigo = 'novo_diretorio'
diretorio_novo = 'diretorio_renomeado'

# Verificando se o diretório existe antes de renomear
if os.path.exists(diretorio_antigo):
    os.rename(diretorio_antigo, diretorio_novo)
    print(f'Diretório renomeado de "{diretorio_antigo}" para "{diretorio_novo}".')
else:
    print(f'O diretório "{diretorio_antigo}" não existe.')
    
import shutil
import os

# Definindo o arquivo e diretórios
arquivo_origem = 'exemplo.txt'
diretorio_destino = 'novo_diretorio'

# Verificando se o arquivo existe
if os.path.exists(arquivo_origem):
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)  # Cria o diretório de destino se não existir

    # Copiando o arquivo para o diretório de destino
    shutil.copy(arquivo_origem, diretorio_destino)
    print(f'Arquivo "{arquivo_origem}" copiado para "{diretorio_destino}".')
else:
    print(f'O arquivo "{arquivo_origem}" não existe.')