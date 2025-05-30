class Midia():
    def __init__(self,titulo,duracao):
        self.titulo = titulo
        self.duracao=duracao

    def exibeInformacoes(self):
        print(f"Titulo Midia: {self.titulo} e duração {self.duracao}")

class Foto(Midia):
    def __init__(self,titulo,duracao,resolucao,formato):
        super().__init__(titulo,duracao)
        self.resolucao = resolucao
        self.formato = formato
    def exibeInformacoes(self):
        print(f"Titulo Foto: {self.titulo}, duração {self.duracao}, resolucao {self.resolucao} e formato {self.formato}")

class Video(Midia):
    def __init__(self,titulo,duracao,resolucao):
        super().__init__(titulo,duracao)
        self.resolucao=resolucao

    def exibeInformacoes(self):
        print(f"Titulo Video: {self.titulo}, duração {self.duracao} e resolucao {self.resolucao}")

class Audio(Midia):
    def __init__(self,titulo,duracao,formato):
        super().__init__(titulo,duracao)
        self.formato=formato

    def exibeInformacoes(self):
        print(f"Titulo Audio: {self.titulo}, duração {self.duracao} e resolucao {self.formato}")

class Playlist():
    def __init__(self):
        self.playlist = []

    def adicionaMidia(self,midia):
        self.playlist.append(midia)
        print(f"Mídia {midia.titulo} adicionada com sucesso!")
    def removeMidia(self,midia):
        for midias in self.playlist:
            if (midias.titulo == midia.titulo):
                self.playlist.remove(midias)
                print(f"Mídia {midias.titulo} removida com sucesso!")
    def exibeInformacoes(self):
        for midias in self.playlist:
            midias.exibeInformacoes() #demonstrando o polimorfismo pois aqui vem toda a classe midia

class Usuario():
    def __init__(self,nome,id):
        self.nome=nome
        self.id=id
        self.playlist = Playlist()

    def adicionarMidiaPlaylist(self,midia):
        self.playlist.adicionaMidia(midia)
        

    def removerMidiaPlaylist(self,midia):
        self.playlist.removeMidia(midia)

    def visualizaTodaPlaylist(self):
        print("")
        print(f"Usuário de nome {self.nome} e ID {self.id} possui as seguintes Mídias")
        self.playlist.exibeInformacoes()

class Biblioteca():
    def __init__(self):
        self.usuarios=[]
    def adicionarUsuario(self,usuario):
        self.usuarios.append(usuario)

    def removerUsuario(self,usuario):
        for cadaUser in self.usuarios:
            if cadaUser.id == usuario.id:
                self.usuarios.remove(cadaUser)
                print(f"Usuário {cadaUser.nome} e id {cadaUser.id} foi removido com sucesso!")

    def listarUsuarios(self):
        for midias in self.usuarios:
            print(f"Usuário {midias.nome} - ID: {midias.id}")


user1 = Usuario("Carla","001")
user2 = Usuario("Madona","002")
user3 = Usuario("Lua","003")

gerenciarUsuarios = Biblioteca()
gerenciarUsuarios.adicionarUsuario(user1)
gerenciarUsuarios.adicionarUsuario(user2)
gerenciarUsuarios.adicionarUsuario(user3)

gerenciarUsuarios.listarUsuarios()

Anitta = Midia("Ensaios da Anitta", "1 hora")
RedHoT = Midia("Californication", "3 min 17 s")
PablloVittar = Midia("Fazer o P - Pabllo Vittar", "2 min 30 s")

midia1 =Midia("1° mídia","5 min")
midia2 =Midia("2° mídia","15 min")
midia3 =Midia("3° mídia","30 min")

foto1 = Foto("Viagem", "N/A", "1920x1080", "JPEG")
video1 = Video("Apresentação", "10 min", "1080p")
audio1 = Audio("Podcast", "30 min", "MP3")

user1.adicionarMidiaPlaylist(Anitta)
user1.adicionarMidiaPlaylist(foto1)
user1.adicionarMidiaPlaylist(video1)

user2.adicionarMidiaPlaylist(midia2)
user2.adicionarMidiaPlaylist(midia1)
user2.adicionarMidiaPlaylist(audio1)

user3.adicionarMidiaPlaylist(PablloVittar)
user3.adicionarMidiaPlaylist(RedHoT)
user3.adicionarMidiaPlaylist(midia3)

user1.visualizaTodaPlaylist()
user2.visualizaTodaPlaylist()
user3.visualizaTodaPlaylist()
