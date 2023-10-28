# Chama a classe girafa que está em outro arquivo.
from girafa import Girafa

# Chama a classe da calculadora
from calculadora import Calculadora

# Definindo os valores do numero_um e do numero_dois.
numeros = Calculadora(32, 2)

numeros.somar()
numeros.multiplicar()
numeros.dividir()
numeros.subtrair()