'''
Exercício 1: Cadastro de Livros em uma Biblioteca Digital

Você está desenvolvendo um sistema para cadastro de livros em uma biblioteca digital. Cada livro tem um título e um código de classificação decimal (número inteiro de 1 a 1000).

Os livros devem ser armazenados em uma Árvore Binária de Busca (BST) com ordenação pelo código de classificação.

O sistema deve permitir:

Inserir novos livros
Remover livros pelo código
Buscar livro pelo título ou código
Mostrar os livros em ordem:
In-ordem
Pré-ordem
Pós-ordem
'''

class Livro:
    def __init__(self, codigo,titulo):
        self.codigo = codigo
        self.titulo = titulo
        self.esquerda = None
        self.direita = None

class Biblioteca:
    def __init__(self):
        self.raiz = None

    def inserir_livro(self, codigo,titulo):
        novo_livro = Livro(codigo,titulo)

        if self.raiz is None:
            self.raiz = novo_livro
        else:
            atual = self.raiz
            while True:
                if codigo < atual.codigo:
                    if atual.esquerda is None:
                        atual.esquerda = novo_livro
                        return
                    atual = atual.esquerda
                else:
                    if atual.direita is None:
                        atual.direita = novo_livro
                        return
                    atual = atual.direita

        
    def mostrar_arvore(self, node=None, nivel=0):
        if node is None:
            node = self.raiz
        if node.direita:
            self.mostrar_arvore(node.direita, nivel + 1)
        print("   " * nivel + f"↳ {node.codigo} {node.titulo}") #anteriormente, era node.valor
        if node.esquerda:
            self.mostrar_arvore(node.esquerda, nivel + 1)

    #raiz, esquerda, direita 
    def preOrdem(self,livro):
        if livro != None:
            print(f"{livro.codigo} - {livro.titulo}")
            self.preOrdem(livro.esquerda)
            self.preOrdem(livro.direita)
    
    def pos_ordem(self, livro):
        if livro is not None:
            self.pos_ordem(livro.esquerda)
            self.pos_ordem(livro.direita)
            print(f"{livro.codigo} - {livro.titulo}")

    def em_ordem(self, livro):
        if livro is not None:
            self.em_ordem(livro.esquerda)
            print(f"{livro.codigo} - {livro.titulo}")
            self.em_ordem(livro.direita)


    def buscar_por_codigo(self,codigo):
        atual = self.raiz #no atual inicia com o valor da raiz

        #enquanto no atual for diferente do valor que procuro encontrar
        while atual.codigo !=codigo:

            #vai para esquerda
            if codigo< atual.codigo:
                atual = atual.esquerda #o novo atual vai receber o antigo atual.esquerda

            #vai para direita
            else:
                atual = atual.direita  #o novo atual vai receber o antigo atual.direita

            if atual ==None:
                return None #significa que na árvore, não tem nenhum elemento igual ao procurado
        return atual
    
    def buscar_por_titulo(self,livro,titulo):
        if livro != None:
            if livro.titulo ==titulo:
                return livro.codigo
            
            resultado_esquerdo = self.buscar_por_titulo(livro.esquerda,titulo)
            if resultado_esquerdo is not None:
                return resultado_esquerdo
            
            resultado_direito = self.buscar_por_titulo(livro.direita,titulo)
            if resultado_direito is not None:
                return resultado_direito

    def excluir(self,codigo):
        if self.raiz ==None:
            print("A árvore está vazia")
            return 
        
        livro_atual = self.raiz
        pai = self.raiz
        esta_esquerda = True 

        while livro_atual.codigo !=codigo:
            pai = livro_atual

            if codigo < livro_atual.codigo:
                esta_esquerda = True
                livro_atual = livro_atual.esquerda

            else:
                esta_esquerda = False 
                livro_atual = livro_atual.direita
            if livro_atual ==None:
                print("Não foi encontrado o elemento que devemos excluir")
                return False
        
        #Condição que o nó encontrado é uma folha (sem filhos)
        if livro_atual.esquerda == None and livro_atual.direita == None:
            if livro_atual == self.raiz: 
                self.raiz = None
            elif esta_esquerda ==True:
                pai.esquerda = None
            else:
                pai.direita = None
                 
        #O nó apagado possui filho à esquerda e não possui filho à direita
        elif livro_atual.direita ==None: 
            if livro_atual == self.raiz:
                self.raiz = livro_atual.esquerda
            elif esta_esquerda == True:
                pai.esquerda = livro_atual.esquerda
            else:
                pai.direita = livro_atual.esquerda

        #O nó apagado possui filho à direita e não possui filho à esquerda
        elif livro_atual.esquerda ==None:
            if livro_atual == self.raiz:
                self.raiz = livro_atual.direita
            elif esta_esquerda ==True:
                pai.esquerda = livro_atual.direita
            else:
                pai.direita = livro_atual.direita

        #Possui dois filhos
        else:
            sucessor = self.getSucessor(livro_atual)

            if livro_atual ==self.raiz:
                self.raiz = sucessor
            elif esta_esquerda ==True:
                pai.esquerda = sucessor
            else:
                pai.direita = sucessor
            sucessor.esquerda = livro_atual.esquerda
        return True

    def getSucessor(self,livro):
        paiSucessor = livro
        sucessor = livro
        livro_atual = livro.direita

        while livro_atual != None:
            paiSucessor = sucessor
            sucessor = livro_atual
            livro_atual = livro_atual.esquerda
            if sucessor != livro.direita:
                paiSucessor.esquerda = sucessor.direita
                sucessor.direita = livro.direita
            return sucessor
        
biblioteca = Biblioteca()
biblioteca.inserir_livro(15,"HP")
biblioteca.inserir_livro(25,"MA")
biblioteca.inserir_livro(10,"CS")
biblioteca.inserir_livro(12,"AM")
biblioteca.inserir_livro(8,"KL")
biblioteca.inserir_livro(18,"GT")
biblioteca.inserir_livro(20,"YO")



'''
#caso você queira procurar por um elemento que não seja a raiz, você procura assim:
subarvore = biblioteca.raiz.direita
biblioteca.mostrar_arvore(subarvore)
'''

'''
#Procurar um valor com base no código ou titulo, caso não seja encontrado, vai retornar None e ele vai mostrar toda a árvore
valor_procurado = biblioteca.buscar_por_codigo(5)
biblioteca.mostrar_arvore(valor_procurado)
'''

#biblioteca.preOrdem(biblioteca.raiz.direita)
#print(biblioteca.procurar_por_titulo("SP"))
#biblioteca.buscar_por_titulo(biblioteca.raiz,"CS")

'''
#Buscando por titulo
busca = biblioteca.buscar_por_titulo(biblioteca.raiz,"GT") 
print(busca) '''
biblioteca.mostrar_arvore()
excluir = biblioteca.excluir(10)
print("----------")
biblioteca.mostrar_arvore()