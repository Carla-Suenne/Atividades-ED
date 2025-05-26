class Livro():
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor 
        self.disponibilidade = True

class Biblioteca():
    def __init__(self):
        self.acervo = []
    
    def adicionarLivros(self,livro):
        self.acervo.append(livro)

    def verificaDisponiveis(self):
        for cadaLivro in self.acervo:
            if cadaLivro.disponibilidade:
                print(cadaLivro.autor ,'-', cadaLivro.titulo)

    def verTodoAcervo(self):
        print('------------Todo o acervo da biblioteca-------------')
        for cadaLivro in self.acervo:
            print(f'{cadaLivro.titulo} - Disponível: {cadaLivro.disponibilidade}')
            print()
    
    def emprestarLivro(self,livro):
        for cadaLivro in self.acervo:
            if cadaLivro.titulo == livro.titulo and cadaLivro.disponibilidade:
                cadaLivro.disponibilidade = False

    def removeLivroAcervo(self,livro):
        for cadaLivro in self.acervo:
            if livro.titulo == cadaLivro.titulo:
                self.acervo.remove(cadaLivro)
                
            

L1 = Livro("Dom Casmurro","Machado de Assis")
L2= Livro("Auto da Compadecida","Ariano Suassuna")
L3 = Livro("Vidas Secas","Graciliano Ramos")
L4 = Livro("O Ateneu","Raul Pompeia")
biblioteca = Biblioteca()

biblioteca.adicionarLivros(L1)
biblioteca.adicionarLivros(L2)
biblioteca.adicionarLivros(L3)
biblioteca.adicionarLivros(L4)

biblioteca.verTodoAcervo()

biblioteca.emprestarLivro(L1)

biblioteca.verificaDisponiveis()
biblioteca.removeLivroAcervo(L3)
biblioteca.verTodoAcervo()