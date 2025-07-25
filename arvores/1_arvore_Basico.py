class No:
    def _init__(self,valor):
        self.valor=valor
        self.esquerda = None #Referencia Nó da esquerda
        self.direita = None #ReferenciaNó da direita

        #Se fosse uma arvore duplamente encadeada, teríamos uma referencia para o proximo e anterior
    def mostraNo(self):
        print(self.valor)

class ArvoreBinaria:
    def __init__(self):
        self.raiz=None
        