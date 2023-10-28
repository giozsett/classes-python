# O nome de uma classe sempre começa com letra maiúscula.
class Girafa:

    #Define as propriedades da girafa.
    # As propriedades podem ser definidas dentro do __init__.
    # O _init_ executa quando a classe é instanciada.
    def __init__(self, nome, altura, idade, cor, origem):
        self.nome = nome
        self.altura = altura
        self.idade = idade
        self.cor = cor
        self.origem = origem
        self.__fome = 100

        # A classe não tem apenas propriedades.
        # Classes também podem ter funções.
    def andar(self):
        print(self.nome, "está andando.")

    # Função para a girafa comer.
    def comer(self, alimento):
        lista_alimentos = ["folhas", "frutas", "plantas"]

        if alimento in lista_alimentos:
            self.__fome -= 10
        else:
            print(self.nome, "não come esse tipo de alimento.")


    def fome(self):
        if self.__fome > 60:
            print(self.nome, "está morrendo de fome!")
        elif self.__fome > 40:
            print(self.nome, "está com fome!")
        elif self.__fome > 20:
            print(self.nome, "não está com fome.")
        elif self.__fome > 10
            print(self.nome, "está de buchin chei.")


    def respirar(self):
        print(self.nome, "está respirando.")
    
    def reproduzir(self):
        print(self.nome, "se reproduz.")