class No:
    def __init__(self,valor):
        self.valor = valor
        self.esquerda =None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None
        self.ligacoes =[]
    
    def inserir(self,valor):
        novo_no = No(valor)

        if(self.raiz ==None):
            self.raiz =novo_no
        else:
            no_atual = self.raiz
            while True:
                no_pai = no_atual
                if valor <no_atual.valor:
                    #o valor que eu devo inserir está a minha esquerda
                    no_atual = no_atual.esquerda
                    if no_atual ==None: #então eu devo adicionar o novo_no aqui
                        no_pai.esquerda = novo_no
                        self.ligacoes.append(str(no_pai.valor)+"->"+str(novo_no.valor))
                        return
                else:
                    #o valor que eu devo inserir está à minha direita
                    no_atual = no_atual.direita
                    if no_atual ==None:
                        no_pai.direita = novo_no
                        self.ligacoes.append(str(no_pai.valor)+"->"+str(novo_no.valor))
                        return
    def em_ordem(self,no):
        #esquerda,raiz,direita
        if no !=None:
            self.em_ordem(no.esquerda)
            print(no.valor)
            self.em_ordem(no.direita)

    def pre_ordem(self,no):
        #raiz,esquerda,direita
        if no !=None:
            print(no.valor)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    def pos_ordem(self,no):
        #esquerda,direita,raiz
        if no !=None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.valor)

arvoreValve = Arvore()
arvoreValve.inserir(120)
arvoreValve.inserir(60)
arvoreValve.inserir(300)
arvoreValve.inserir(45)
arvoreValve.inserir(200)
arvoreValve.inserir(90)
arvoreValve.inserir(20)
arvoreValve.inserir(150)

print(arvoreValve.ligacoes)

#arvoreValve.em_ordem(arvoreValve.raiz)
arvoreValve.pre_ordem(arvoreValve.raiz)