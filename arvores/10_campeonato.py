class Time:
    def __init__(self, nome,ranking):
        self.nome= nome
        self.ranking = ranking
        self.esquerda = None
        self.direita = None

class Campeonato:
    def __init__(self):
        self.raiz =None

    def inserir_time(self,nome,ranking):
        novo_time = Time(nome,ranking)

        if self.raiz is None:
            self.raiz =novo_time
        else:
            time_atual = self.raiz

            while True:
                if ranking <time_atual.ranking:
                    if time_atual.esquerda is None:
                        time_atual.esquerda = novo_time
                        return
                    time_atual = time_atual.esquerda
                else:
                    if time_atual.direita is None:
                        time_atual.direita = novo_time
                        return
                    time_atual = time_atual.direita

    def mostrar_arvore_campeonato(self, time=None, nivel=0):
        if time is None:
            time = self.raiz
        if self.raiz is None:
            return
        if time.direita:
            self.mostrar_arvore_campeonato(time.direita, nivel + 1)
        print("   " * nivel + f"↳ {time.ranking} - {time.nome}") #anteriormente, era node.valor
        if time.esquerda:
            self.mostrar_arvore_campeonato(time.esquerda, nivel + 1)

    def excluir_time_campeonato(self,ranking):
        if self.raiz ==None:
            print("A árvore está vazia")
            return 
        
        time_atual = self.raiz
        time_pai = self.raiz
        esta_esquerda = True 

        while time_atual.ranking !=ranking:
            time_pai = time_atual

            if ranking < time_atual.ranking:
                esta_esquerda = True
                time_atual = time_atual.esquerda

            else:
                esta_esquerda = False 
                time_atual = time_atual.direita

            if time_atual ==None:
                print("Não foi encontrado este ranking na arvore")
                return False
        
        #Condição que o nó encontrado é uma folha (sem filhos)
        if time_atual.esquerda == None and time_atual.direita == None:
            if time_atual == self.raiz: 
                self.raiz = None #arvore vazia
            elif esta_esquerda ==True:
                time_pai.esquerda = None
            else:
                time_pai.direita = None
                 
        #O nó apagado possui filho à esquerda e não possui filho à direita
        elif time_atual.direita ==None: 
            if time_atual == self.raiz:
                self.raiz = time_atual.esquerda
            elif esta_esquerda == True:
                time_pai.esquerda = time_atual.esquerda
            else:
                time_pai.direita = time_atual.esquerda

        #O nó apagado possui filho à direita e não possui filho à esquerda
        elif time_atual.esquerda ==None:
            if time_atual == self.raiz:
                self.raiz = time_atual.direita
            elif esta_esquerda ==True:
                time_pai.esquerda = time_atual.direita
            else:
                time_pai.direita = time_atual.direita

        #possui dois filhos
        else:
            sucessor = self.getSucessor(time_atual)

            if time_atual ==self.raiz:
                self.raiz = sucessor
            elif esta_esquerda ==True:
                time_pai.esquerda = sucessor
            else:
                time_pai.direita = sucessor
            sucessor.esquerda = time_atual.esquerda
            return True
        
    def getSucessor(self,time):
        paiSucessor = time
        sucessor = time
        time_atual = time.direita

        while time_atual != None:
            paiSucessor = sucessor
            sucessor = time_atual
            time_atual = time_atual.esquerda
        if sucessor != time.direita:
                paiSucessor.esquerda = sucessor.direita
                sucessor.direita = time.direita
        return sucessor
        
    def achar_proximo_combatente(self,ranking):
        if self.raiz ==None:
            print("A árvore está vazia")
            return 
        
        time_atual = self.raiz
        time_pai = self.raiz
        esta_esquerda = True 

        while time_atual.ranking !=ranking:
            time_pai = time_atual

            if ranking < time_atual.ranking:
                esta_esquerda = True
                time_atual = time_atual.esquerda

            else:
                esta_esquerda = False 
                time_atual = time_atual.direita

            if time_atual ==None:
                print("Não foi encontrado este ranking na arvore")
                return False
        
        #Condição que o nó encontrado é uma folha (sem filhos)
        if time_atual.esquerda == None and time_atual.direita == None:
            if time_atual == self.raiz: 
                print("Não existe combate")
            elif esta_esquerda ==True:
                print(f"{time_atual.nome} X {time_pai.nome}")
            else:
                print(f"{time_atual.nome} X {time_pai.nome}")

        #O nó combatente possui filho à esquerda e não possui filho à direita
        elif time_atual.direita ==None: 
            #time atual x time atual.esquerda
            if esta_esquerda == True:
                #time atual x time atual. esq
                print(f"{time_atual.nome} X {time_atual.esquerda.nome}")
            else:
                print(f"{time_atual.nome} X {time_atual.direita.nome}")

        elif time_atual.esquerda ==None:
            if esta_esquerda ==True:
                print(f"{time_atual.nome} X {time_atual.esquerda.nome}")
            else:
                print(f"{time_atual.nome} X {time_atual.direita.nome}")
        else:
            #os filhos deverão brigar
            print(f"{time_atual.esquerda.nome} X {time_atual.direita.nome}")
campeonato = Campeonato()

campeonato.inserir_time("Fla",7)
campeonato.inserir_time("Rus",8)
campeonato.inserir_time("Cur",6)
campeonato.inserir_time("Bay",5)

campeonato.mostrar_arvore_campeonato()

campeonato.achar_proximo_combatente(8)

campeonato.excluir_time_campeonato(7)
campeonato.mostrar_arvore_campeonato()