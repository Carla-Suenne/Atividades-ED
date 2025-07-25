class No:
    def __init__(self, sintoma):
        self.sintoma = sintoma
        self.esquerda = None  # Sim
        self.direita = None   # NÃ£o

class ArvoreDecisao:
    def __init__(self):
        self.root = None

    def mostrar_arvore(self, node=None, prefixo=""):
        if node is None:
            node = self.root
        if node is not None:
            print(prefixo + node.sintoma)
            if node.esquerda is not None or node.direita is not None:
                self.mostrar_arvore(node.esquerda, prefixo + "  [Sim] ")
                self.mostrar_arvore(node.direita, prefixo + "  [NÃ£o] ")

    def diagnosticar(self, node=None):
        if node is None:
            node = self.root
        # Checa se Ã© um nÃ³ folha (diagnÃ³stico)
        if node.esquerda is None and node.direita is None:
            print("DiagnÃ³stico:", node.sintoma)
            return
        resposta = input(node.sintoma + " (s/n): ").strip().lower()
        if resposta == "s":
            self.diagnosticar(node.esquerda)
        else:
            self.diagnosticar(node.direita)

# CriaÃ§Ã£o da Ã¡rvore de decisÃ£o
arvore = ArvoreDecisao()
arvore.root = No("O paciente tem febre?")
arvore.root.esquerda = No("O paciente sente dor no corpo?")
arvore.root.esquerda.esquerda = No("InfecÃ§Ã£o viral")
arvore.root.esquerda.direita = No("InfecÃ§Ã£o bacteriana")
arvore.root.direita = No("Resfriado comum")

# Mostrar toda a Ã¡rvore
print("Ãrvore de decisÃ£o:")
arvore.mostrar_arvore()

# Simular entrada do usuÃ¡rio
print("\nIniciando diagnÃ³stico...")
arvore.diagnosticar()