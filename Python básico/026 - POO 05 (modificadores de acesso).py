# público( ) - Acessado em qualquer parte do código
# privado(__) - Acessado somente pela sua respectiva classe
# protegido(_) - Acessado somente pela sua respectiva classe e pelas suas sublcasses(classes filhas)
 
class Conta:

    # Saldo é um atributo privado, pois ele não deve ser modificado em qualquer parte do código
    def __init__(self):
        self.__saldo_atual = 0.0

    # Um método GETTER mostra o valor de um atributo privado, ele pode ter qualquer nome, tipo "Mostrar saldo"
    def getter(self):
        print(self.__saldo_atual)  
    # Um método SETTER muda o valor de um atributo privado, ele pode ter qualquer nome, tipo "Depositar"
    def setter(self, novo_saldo):
        self.__saldo_atual = novo_saldo

minhaconta = Conta()

minhaconta.getter()

minhaconta.setter(50)

minhaconta.getter()

input()