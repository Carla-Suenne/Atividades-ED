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

        #Se a arvore estiver vazia
        if self.raiz ==None:
            self.raiz = novo

        #Se a arvore não estiver vazia
        else:
            atual = self.raiz #armazena o nó atual que estamos fazendo as verificações
            while True: #criamos um loop infinito e iremos parar quando enconrtrarmos a posição que iremos inserir o novo nó
                
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