class Midia():
    def __init__(self,titulo,duracao):
        self.titulo = titulo
        self.duracao = duracao

    def exibeInformacoes(self):
        print("----------Midia----------")
        print(f'Título: {self.titulo} - Duração: {self.duracao}')

class Video(Midia):
    def __init__(self,titulo,duracao,resolucao):
        self.resolucao = resolucao
        super().__init__(titulo,duracao)
    def exibeInformacoes(self):
        print('----------Vídeo----------')
        print(f'Título: {self.titulo} - Duração: {self.duracao} - Resolução: {self.resolucao}')

class Audio(Midia):
    def __init__(self, titulo, duracao,formato):
        super().__init__(titulo, duracao)
        self.formato = formato

    def exibeInformacoes(self):
        print('----------Áudio----------')
        print(f'Título: {self.titulo} - Duração: {self.duracao} - Formato: {self.formato}')

class Playlist():
    def __init__(self):
        self.playlist = []
    
    def adicionaMidia(self,midia):
        self.playlist.append(midia)
    
    def verPlaylist(self):
        for midias in self.playlist:
            #print(f"Título: {midias.titulo} - {midias.duracao}")

            #ADICIONANDO POLIMORFISMO
            midias.exibeInformacoes() #Midias vem no formato titulo e duracao e voce chama o método 
    
    def removeMidia(self,midia):
        for midias in self.playlist:
            if midias.titulo == midia.titulo:
                self.playlist.remove(midias)

class Foto(Midia):
    def __init__(self, titulo, duracao,resolucao,formato):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao
        self.formato = formato

    def exibeInformacoes(self):
        print(f"Titulo {self.titulo} - Duração {self.duracao} - Resolução {self.resolucao} - Formato: {self.formato}")

class Podcast(Audio):
    def __init__(self, titulo, duracao, formato,episodio):
        super().__init__(titulo, duracao, formato)
        self.episodio = episodio
    
    def exibeInformacoes(self):
        print(f"Titulo {self.titulo} - Duração {self.duracao} - Resolução {self.resolucao} - Formato: {self.formato} - Episódio: {self.episodio}")

class Usuario():
    def __init__(self, nome,id):
        self.nome = nome
        self.id=id
        self.playlist = Playlist()
    def adicionarMidias(self,midia):
        self.playlist.adicionaMidia(midia)

midia1 = Midia("Mídia Aleatória", "5 min")
midia2 = Midia("Outra Mídia", "8 min")
midia3 = Midia("Mais uma Mídia", "2 min")
#midia1.exibeInformacoes()
'''
video1 = Video("ASMR","2hrs 45 min", "1040px")
#video1.exibeInformacoes()

audio1 = Audio("Ocean Eyes","3:20 min","Mp4")
#audio1.exibeInformacoes()

Elemento1 = Playlist()
print()
print('Adicionando Mídia\n')
Elemento1.adicionaMidia(midia1)
Elemento1.adicionaMidia(midia2)
Elemento1.adicionaMidia(midia3)
Elemento1.verPlaylist()
print()
print('Removendo Mídia \n')
Elemento1.removeMidia(midia2)
Elemento1.verPlaylist()
'''

Pessoa1 = Usuario("Carla","02")
Pessoa1.adicionarMidias(midia1)
Pessoa1.adicionarMidias(midia2)
Pessoa1.adicionarMidias(midia3)


