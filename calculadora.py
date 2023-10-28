# EXERCÍCIO
# Criar uma classe chamada Calculadora.
# Essa classe receberá 2 propriedades: 
# --- Número_Um
# --- Número_Dois
# Deverá receber as seguintes funções:
# -- Somar
# -- Multiplicar
# -- Dividir
# -- Elevar
# -- Subtrair
# Deverá executar uma função sempre que as outras funções forem chamadas. 
# A qual deve garantir que 2 números foram inseridos.

class Calculadora:
    def __init__(self, numero_um, numero_dois):
        self.numero_um = numero_um
        self.numero_dois = numero_dois

    
    def verifica_numero(self):
        pass


    def somar(self):
        resultado = self.numero_um + self.numero_dois
        print("O resultado da soma de", self.numero_um, "e", self.numero_dois, "é igual a", resultado)


    def multiplicar(self):
        resultado = self.numero_um * self.numero_dois
        print("O resultado da multiplicação de", self.numero_um, "e", self.numero_dois, "é igual a", resultado)


    def dividir(self):
        if self.numero_dois == 0:
            resultado = "Erro"
            print("Não é possível dividir um número por 0.")
        else:
            resultado = self.numero_um / self.numero_dois
            print("O resultado da divisão de", self.numero_um, "por", self.numero_dois, "é igual a", resultado)


    def elevar(self):
        pass


    def subtrair(self):
        resultado = self.numero_um - self.numero_dois
        print( self.numero_um, "menos", self.numero_dois, "é igual a", resultado)

