'''
                                          53
                                    30          72
                                14  39       61    84
                            9  23  34  49         79


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
         
    def preOrdem(self,no):
        if no != None:
            print(no.valor)
            self.preOrdem(no.esquerda)
            self.preOrdem(no.direita)

    def emOrdem(self,no):
        if no != None:
            self.emOrdem(no.esquerda)
            print(no.valor)
            self.emOrdem(no.direita)

    def pesquisar(self,valor):
        atual = self.raiz #no atual inicia com o valor da raiz

        #enquanto no atual for diferente do valor que procuro encontrar
        while atual.valor !=valor:

            #vai para esquerda
            if valor< atual.valor:
                atual = atual.esquerda #o novo atual vai receber o antigo atual.esquerda

            #vai para direita
            else:
                atual = atual.direita  #o novo atual vai receber o antigo atual.direita
            if atual ==None:
                return None #significa que na árvore, não tem nenhum elemento igual ao procurado
        return atual

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

valorPesquisa = arvore.pesquisar(4).valor

if valorPesquisa != None:
    print(valorPesquisa)
else:
    print("Não há esse elemento para mostrar")

#webGrafviz
#print(arvore.ligacoes)
#arvore.preOrdem(arvore.raiz)
#arvore.emOrdem(arvore.raiz)

