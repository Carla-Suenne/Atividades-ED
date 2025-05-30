#abaixo é somente aquele quadradinho que possui um valor e o endereço do proximo elemento
class Celula(): #é a mesma coisa do Nó, imagine aquela caixa quadrada
    def __init__(self,valor):
        self.valor = valor
        self.enderecoProximoElemento = None #de inicio nao temos proximo elemento e por isso o valor é NONE

    def mostraValorCelula(self):
        print(self.valor)

class ListaEncadeada(): #aqui já é a lista completa
    def __init__(self):
        self.primeiroElemento = None #aqui é o primeiro elemento e ela inicia com NONE pq não foi definido nenhum valor para ela ainda (só será definido na função de inserir)

    def insereInicio(self,valor): #apesar do nome, todo elemento em uma lista encadeada, é inserido no início
        #para inserir um valor na lista, eu preciso criar toda a caixinha, por isso primeiro eu chamo a função da célula/Nó
        novaCelula = Celula(valor) #criando a caixinha com os valores dentro
        novaCelula.enderecoProximoElemento = self.primeiroElemento #tô dizendo que o endereco do proximo elemento da lista, é o endereço do primeiro
        self.primeiroElemento = novaCelula #primeiro elemento recebe o valor da novaCelula 

    def mostrar(self):
        atual = self.primeiroElemento
        while atual !=None: #se chegar em None, significa que está no fim da lista
            atual.mostraValorCelula()
            atual = atual.enderecoProximoElemento

    def removerInicio(self):
        if self.primeiroElemento == None: #significa que esse primeiro elemento está vazio
            print("A lista está vazia!")
            return None
        atual = self.primeiroElemento
        self.primeiroElemento = self.primeiroElemento.enderecoProximoElemento #significa que o primeiro elemento, vai apontar para o endereço do próximo então esse vai ser apagado
        return atual
    
    def pesquisaValor(self,valor):
        
        if self.primeiroElemento == None: #se atual for igual a None, significa que ja chegou no fim da lista
            print("A lista está vazia")
            return None
        atual = self.primeiroElemento
        while atual.valor != valor:
            if atual.enderecoProximoElemento ==None:
                print("Elemento não encontrado")
                return None
            else: 
                atual = atual.enderecoProximoElemento

            return atual


lista = ListaEncadeada()
#o primeiro elemento adicionado seá sempre o último a ser removido/mostrado/acessado
lista.insereInicio(5)
lista.insereInicio(8)
lista.insereInicio(3)

print("Mostrar")

lista.mostrar()
'''
print("Mostrar")
lista.mostrar()
lista.removerInicio()
print("Mostrar")
lista.mostrar() '''

pesquisa = lista.pesquisaValor(1)
if pesquisa !=None:
    print("Valor encontrado")
else:
    print("Valor não encontrado")