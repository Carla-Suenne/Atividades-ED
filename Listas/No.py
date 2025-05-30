class Noh():
    def __init__(self,valor):
        self.valor=valor
        self.proximo = None

    def mostraNoh(self):
        print(self.valor)

#Criar uma classe para armazenar a estrutura de todos esses nós
class ListaEncadeada():
    def __init__(self):
        self.primeiro=None #é uma variável que vai apontar para o primeiro elemento que incluírmos na lista; ela inicia com None

    def insereInicio(self,valor):
        novo =Noh(valor)
        novo.proximo = self.primeiro
        self.primeiro = novo
    
    def mostrar(self):
        atual = self.primeiro
        while(atual !=None): #se chegar em none, significa que nao tem mais ninguem pra percorrer
            atual.mostraNoh()
            atual = atual.proximo

    def excluirInicio(self):
        if self.primeiro ==None:
            print("A lista está vazia")
            return None
        temporario = self.primeiro
        self.primeiro = self.primeiro.proximo
        return temporario
    
    def pesquisa(self,valor):
        if self.primeiro ==None:
            print("A lista está vazia")
            return None
        atual = self.primeiro
        while atual != valor:
            atual.mostraNoh()
            atual = atual.proximo


lista = ListaEncadeada()
lista.insereInicio(1) #observe que os enderecos de memoria mudam desse para o proximo pois ao inserir um objeto, o novo obj possui um endereço de memoria diferento do primeiro
#print(lista.primeiro)
lista.insereInicio(2)
#print(lista.primeiro)

lista.insereInicio(3)
lista.insereInicio(4)
lista.insereInicio(5)

print("Mostrar")
lista.mostrar()
#você vai observar que o valor está mostrando primeiro o ultimo elemento inserido e vai para o primeiro
#isso acontece pq ele sempre adiciona os elementos no inicio da lista

#para conferir os endereços de memória você pode:
'''
print(lista.primeiro) #elemento 5
print(lista.primeiro.proximo) #elemento 4
print(lista.primeiro.proximo.proximo) #elemento 3
print(lista.primeiro.proximo.proximo.proximo) #elemento 2
print(lista.primeiro.proximo.proximo.proximo.proximo)#elemento 1
'''
lista.excluirInicio()
print("Mostrar")
lista.mostrar()
lista.excluirInicio()
print("Mostrar")
lista.mostrar()
lista.excluirInicio()
print("Mostrar")
lista.mostrar()
lista.excluirInicio()
print("Mostrar")
lista.mostrar()
lista.excluirInicio()
print("Mostrar")
lista.mostrar()