class Midia:
    def __init__(self,titulo,duracao):
        self.titulo=titulo
        self.duracao = duracao

    def exibeInformacoes(self):
        print(f'Título {self.titulo} - Duração {self.duracao}')

class Playlist():
    def __init__(self):
        self.playlist = []

    def adicionaMidiaPlaylist(self,midia):
        self.playlist.append(midia)
    
    def removeMidiaPlaylist(self,midia):
        for midiaRemover in self.playlist:
            if midia.titulo == midiaRemover.titulo:
                self.playlist.remove(midiaRemover)

    def verPlaylistCompleta(self):
        for midias in self.playlist:
            print(f'Titulo: {midias.titulo} - Duração: {midias.duracao}')

class Usuario():
    def __init__(self,nome,id):
        self.nome=nome
        self.id=id
        self.playlist = Playlist()
    
    def adicionaMidiasMinhaPlaylist(self,midia):
        self.playlist.adicionaMidiaPlaylist(midia)
    
    def visualizarTodaPlaylist(self):
        return self.playlist.verPlaylistCompleta()

midia1 =Midia("1° mídia","5 min")
midia2 =Midia("2° mídia","15 min")
midia3 =Midia("3° mídia","30 min")

'''
minhaPlaylist = Playlist()
minhaPlaylist.adicionaMidiaPlaylist(midia1)
minhaPlaylist.adicionaMidiaPlaylist(midia2)
minhaPlaylist.adicionaMidiaPlaylist(midia3)
'''
#minhaPlaylist.verPlaylistCompleta()

usuario1 = Usuario("Carla","001")
usuario1.adicionaMidiasMinhaPlaylist(midia1)
usuario1.adicionaMidiasMinhaPlaylist(midia2)
usuario1.adicionaMidiasMinhaPlaylist(midia3)

usuario1.visualizarTodaPlaylist()