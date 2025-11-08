# arquivo main.py

import modulo as mdl

empresa  =  [1,2,10,15,1,22,33,35,40,50]

print(mdl.imc(65,1.70))
print(mdl.calcular_soma(10,30))
print(mdl.verificar_idade(25))
mdl.estatistica(empresa)
print('media',mdl.media(empresa))
print('mediana',mdl.mediana(empresa))
print('desvio',mdl.desvio(empresa))
print('variancia',mdl.variancia(empresa))
print('amplitude', mdl.amplitude(empresa))


