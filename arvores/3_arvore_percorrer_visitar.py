#Um nó é VISITADO quando o controle do programa chega ao nó, em geral, com a finalidade de executar alguma ação

#Um nó é PERCORRIDO quando você passa por todos os nós em uma ordem pré definida

#A ordem sempre será Raiz, Esquerda, Direita.
#Então em uma árvore, ele sempre irá percorrer primeiro os nós da esquerda e depois da direita

'''
                                          53
                                    30          72
                                14  39       61    84
                            9  23  34  49         79

                            No caso dessa árvore, ele vai fazer a seguinte ordem: 53>30>14>9>23>39>34>49>72>61>84>79
'''

class No:
    def __init__(self,valor):
        self.valor=valor
        self.esquerda = None 
        self.direita = None 

        
    def mostraNo(self):
        print(self.valor)

class ArvoreBinaria:
    def __init__(self):
        self.raiz=None
        self.ligacoes=[]
    def inserir(self,valor):
        novo = No(valor) 

        if self.raiz ==None:
            self.raiz = novo

        else:
            atual = self.raiz 
            while True: 
                pai = atual 
                if valor < atual.valor:
                    atual = atual.esquerda 
                    if atual==None:
                        pai.esquerda = novo
                        self.ligacoes.append(str(pai.valor)+"->"+str(novo.valor))
                        return
                else:
                    atual = atual.direita
                    if atual ==None:
                        pai.direita =novo
                        self.ligacoes.append(str(pai.valor)+"->"+str(novo.valor))
                        return
    #raiz, esquerda, direita             
    def preOrdem(self,no):
        if no != None:
            print(no.valor) #eu estou só printando mas eu poderia estar fazendo outra coisa aqui
            self.preOrdem(no.esquerda)
            self.preOrdem(no.direita)

    #esquerda, raiz, direita   -->Observe que os valores irão sair em ordem crescente
    def emOrdem(self,no):
        if no != None:
            self.emOrdem(no.esquerda)
            print(no.valor)
            self.emOrdem(no.direita)
#webGrafviz
arvore = ArvoreBinaria()
arvore.inserir(53)
arvore.inserir(30)
arvore.inserir(14)
arvore.inserir(39)
arvore.inserir(9)
arvore.inserir(23)
arvore.inserir(34)
arvore.inserir(49)
arvore.inserir(72)
arvore.inserir(61)
arvore.inserir(84)
arvore.inserir(79)

print(arvore.ligacoes)

#arvore.preOrdem(arvore.raiz)
arvore.emOrdem(arvore.raiz)