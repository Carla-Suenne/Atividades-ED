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
        atual = self.raiz 
        while atual.valor !=valor:
            if valor< atual.valor:
                atual = atual.esquerda
            else:
                atual = atual.direita  
            if atual ==None:
                return None 
        return atual
    
    def excluir(self,valor):
        if self.raiz ==None:
            print("A árvore está vazia")
            return #pra sair da função
        
        #Encontrar o nó
        atual = self.raiz
        pai = self.raiz
        esta_esquerda = True #vai servir para identificar se o elemento que estamos apagando está na esquerda ou direita

        while atual.valor !=valor:
            pai = atual
            #esquerda
            if valor < atual.valor:
                esta_esquerda = True #o nó está do lado esquerdo
                atual = atual.esquerda
            #direita
            else:
                esta_esquerda = False #o nó está do lado direito
                atual = atual.direita
            if atual ==None:
                print("Não foi encontrado o elemento que devemos excluir")
                return False
        
        #Condição que o nó encontrado é uma folha (sem filhos)
        if atual.esquerda == None and atual.direita == None:
            if atual == self.raiz: #a arvore só possui um elemento e ela vai ficar vazia
                self.raiz = None
            elif esta_esquerda ==True:
                self.ligacoes.remove(str(pai.valor)+"->"+str(atual.valor)) #excluindo o elemento da lista de ligações
                pai.esquerda = None
            else:
                self.ligacoes.remove(str(pai.valor)+"->"+str(atual.valor)) #excluindo o elemento da lista de ligações
                pai.direita = None
                 
        #O nó apagado possui filho à esquerda e não possui filho à direita
        elif atual.direita ==None: #não é necessário testar se o atual.esquerda !=None porque se fosse ==None ele teria entrado no if anterior
            if atual == self.raiz:
                self.raiz = atual.esquerda
            elif esta_esquerda == True:
                pai.esquerda = atual.esquerda
            else:
                pai.direita = atual.esquerda

        #O nó apagado possui filho à direita e não possui filho à esquerda
        elif atual.esquerda ==None:
            if atual == self.raiz:
                self.raiz = atual.direita
            elif esta_esquerda ==True:
                pai.esquerda = atual.direita
            else:
                pai.direita = atual.direita

        #Possui dois filhos
        else:
            sucessor = self.getSucessor(atual)

            if atual ==self.raiz:
                self.raiz = sucessor
            elif esta_esquerda ==True:
                pai.esquerda = sucessor
            else:
                pai.direita = sucessor
            sucessor.esquerda = atual.esquerda

        return True

        #O Nó a ser apagado possui dois filhos e ele deve ser substituido pelo seu sucessor em ordem
        #então ele vai procurar o valor que deseja apagar, ao encontrar ele vai para o lado direito 1x se o nó a direita tiver filho, ele vai para a esquerda até n conseguir mais
        
    def getSucessor(self,no): #aqui ele já encontrou o nó que devemos excluir e agora vamos buscar o sucessor mais perto (número menor) para ele
        paiSucessor = no
        sucessor = no
        atual = no.direita

        while atual != None:
            paiSucessor = sucessor
            sucessor = atual
            atual = atual.esquerda
            if sucessor != no.direita:
                paiSucessor.esquerda = sucessor.direita
                sucessor.direita = no.direita
            return sucessor
            


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

#webGrafviz
#print(arvore.ligacoes)
#arvore.preOrdem(arvore.raiz)
#arvore.emOrdem(arvore.raiz)

