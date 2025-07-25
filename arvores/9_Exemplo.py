class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        novo_no = No(valor)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            atual = self.raiz
            while True:
                if valor < atual.valor:
                    if atual.esquerda is None:
                        atual.esquerda = novo_no
                        return
                    atual = atual.esquerda
                else:
                    if atual.direita is None:
                        atual.direita = novo_no
                        return
                    atual = atual.direita

    def mostrar_arvore(self, node=None, nivel=0):
        if node is None:
            node = self.raiz
        if node.direita:
            self.mostrar_arvore(node.direita, nivel + 1)
        print("   " * nivel + f"↳ {node.valor}")
        if node.esquerda:
            self.mostrar_arvore(node.esquerda, nivel + 1)

arvore = Arvore()
for valor in [120, 60, 300, 45, 200, 90, 20, 150]:
    arvore.inserir(valor)

arvore.mostrar_arvore()

