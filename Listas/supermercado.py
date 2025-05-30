class Itens():
    def __init__(self,nomeItem,precoItem):
        self.nomeItem = nomeItem
        self.precoItem = precoItem
        self.proximo = None #inicia com none pq primeiro elemento da lista não tem proximo ainda
    def mostraItens(self):
        print(f"Item {self.nomeItem} e valor {self.precoItem}")
class supermercado():
    def __init__(self):
        self.inicio =None #inicia com None pq nao tem elemento ainda essa é a cabeça da lista

    def inserirInicio(self,nome,preco):
        novoItem = Itens(nome,preco)
        novoItem.proximo = self.inicio # aponta para o antigo primeiro item
        self.inicio = novoItem # agora o novo item é o primeiro
        print(f"Item '{nome}' inserido no início com sucesso!")

    def inserirFinal(self,nome,preco):
        novoItem = Itens(nome,preco)
        if self.inicio is None:
            self.inicio = novoItem #lista está vazia então ele tem que adicionar no inicio de qualquer forma
        else:
            atual = self.inicio #pegando a referencia de inicio (então se eu mudo o valor de atual.valor, o self.inicio.valor também é modificado pois eles apontam para o mesmo elemento)
            while atual.proximo != None: #ainda não chegou no final da lista
                atual = atual.proximo
            atual.proximo = novoItem #se acabou o while, é pq chegou no final da lista e então ele diz que o proximo elemento é o novo item
        print(f"Item '{nome}' inserido no final com sucesso!")
                
    def mostrar(self):
        if self.inicio is None:
            print("O estoque está vazio!")
        atual = self.inicio
        while atual !=None:
            atual.mostraItens()
            atual = atual.proximo


    def removerInicio(self,nomeItem):
        if self.inicio == None:
            print("A lista está vazia")
            return
        if self.inicio.nomeItem == nomeItem: #se o primeiro elemento da lista, for o elemento que estamos querendo remover
            self.inicio = self.inicio.proximo #o inicio vai receber o valor do proximo elemento, é uma espécie de exclusão
            print(f"Elemento {nomeItem} removido do início com sucesso!")   
            return
        anterior = self.inicio
        atual = self.inicio.proximo
        while atual !=None: #significa que não chegou no fim da lista
            if atual.nomeItem == nomeItem:
                anterior.proximo = atual.proximo
                print(f"Elemento {nomeItem} removido do início com sucesso")
            anterior = atual
            atual = atual.proximo

    def pesquisarItem(self,nomeItem):
        atual = self.inicio
        if atual ==None:
            print("A lista está vazia")
            return
        while atual.proximo !=None:
            if atual.nomeItem == nomeItem:
                print(f"Item {atual.nomeItem} está disponível no supermercado por apenas R${atual.precoItem}. Aproveite!")
                return True
            atual = atual.proximo
        print(f"O item {nomeItem} não está disponível no estoque!")
        return False
    
    def contadorItens(self):
        contador = 0
        if self.inicio is None:
            print("O estoque está vazio. Há 0 itens nele.")
            return None
        atual = self.inicio

        while atual != None:
            contador = contador +1
            atual= atual.proximo
            
        print(f"Há {contador} elementos no estoque!")

    def inverter_lista(self):
        anterior = None
        atual = self.inicio

        while atual is not None:
            proximo = atual.proximo     # guarda o próximo nó
            atual.proximo = anterior    # inverte o ponteiro
            anterior = atual            # move o "anterior" pra frente
            atual = proximo             # move o "atual" pra frente

        self.inicio = anterior   
    
    def inserir_ordenado(self, nome, preco):
        novo = Itens(nome, preco)
        
        # Se a lista está vazia ou o preço do novo é menor que o primeiro
        if self.inicio is None or preco < self.inicio.precoItem:
            novo.proximo = self.inicio
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo is not None and atual.proximo.preco < preco:
                atual = atual.proximo
            novo.proximo = atual.proximo
            atual.proximo = novo


marketplace = supermercado()
marketplace.inserirInicio("Arroz", 5.99)
marketplace.inserirInicio("Suco", 13.90)
marketplace.inserirFinal("Tomates",3.50)
marketplace.inserirInicio("Leite",8.95)
marketplace.inserirFinal("Pão",11.90)

print("--- mostrar ---")

marketplace.mostrar()
marketplace.removerInicio("Suco")

print("--- mostrar ---")
marketplace.mostrar()

marketplace.pesquisarItem("Tomates")
marketplace.pesquisarItem("Suco")

print("--- mostrar ---")
marketplace.mostrar()
marketplace.contadorItens()