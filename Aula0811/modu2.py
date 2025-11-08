# # arquivo modulo.py
# import  statistics

# #medida de tendencia central:
# # moda -  media - mediana  -  desvio  
# # variancia  -  amplitude 





# def estatistica(lista):
#     dados2 =  set(lista)
#     ''' moda é o que mais aparece'''
#     if len(lista) != len(dados2):
#         moda = statistics.mode(lista)
#         print('moda', moda)

#     else:    
#         print('Não tem moda')

# def media(lista):
#     ''' soma dos indices /  quantidade'''
#     media  =  statistics.mean(lista)
#     return 'media', media

# def mediana(lista):
#     ''' esta no meio da frequencia'''
#     med  =  statistics.median(lista)
#     return med

# def desvio(lista):
#     ''' a raiz quadrada da variancia '''
#     d =  statistics.stdev(lista)
#     return d

# def variancia(lista):
#     ''' a distancia entre a media quadratica a os indices '''
#     variancia   =  statistics.variance(lista)
#     return variancia


# def amplitude(lista):
#     ampl = max(lista) -  min(lista)
#     return ampl












# def imc(peso, altura):
#     return peso/altura**2

# def calcular_soma(x,y):
#     return x + y

# def verificar_idade(idade):
#     if idade >= 18:
#         return 'maior de idade'
#     else:
#         return 'Menor de idade'







import numpy as np
from scipy import stats

# Dados dos salários das empresas
empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]

# Função para calcular as métricas: média, mediana, moda e desvio padrão
def calcular_metrica(salarios):
    # Média
    media = np.mean(salarios)
    
    # Mediana
    mediana = np.median(salarios)
    
    # Moda (se existir)
    moda = stats.mode(salarios)[0][0] if len(set(salarios)) < len(salarios) else "Não existe moda"
    
    # Desvio Padrão
    desvio_padrao = np.std(salarios)
    
    return media, mediana, moda, desvio_padrao

# Calculando as métricas para cada empresa
empresa1_metrics = calcular_metrica(empresa1)
empresa2_metrics = calcular_metrica(empresa2)
empresa3_metrics = calcular_metrica(empresa3)
empresa4_metrics = calcular_metrica(empresa4)

# Exibindo os resultados
def exibir_resultados(empresa, metrics):
    print(f"Salários da {empresa}:")
    print(f"Média: {metrics[0]:.2f}")
    print(f"Mediana: {metrics[1]}")
    print(f"Moda: {metrics[2]}")
    print(f"Desvio Padrão: {metrics[3]:.2f}\n")

# Exibindo os resultados de todas as empresas
exibir_resultados("Empresa 1", empresa1_metrics)
exibir_resultados("Empresa 2", empresa2_metrics)
exibir_resultados("Empresa 3", empresa3_metrics)
exibir_resultados("Empresa 4", empresa4_metrics)

# Conclusão geral
print("Conclusão:")
if empresa3_metrics[0] > empresa2_metrics[0]:
    print("A Empresa 3 tem a maior média salarial, mas com um desvio padrão mais alto.")
else:
    print("A Empresa 2 tem uma boa média salarial e um desvio padrão baixo, o que significa mais estabilidade nos salários.")