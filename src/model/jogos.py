from model.campeonato import Campeonato

class Jogos:
    def __init__(self,
                 id_jogo: int = None,
                 estadio: str = None,
                 time_mandante: str = None,
                 time_visitante: str = None,
                 gol_mandante: int = None,
                 gol_visitante: int = None,
                 id_campeonato: Campeonato = None
                 ):
        self.set_id_jogo(id_jogo)
        self.set_estadio(estadio)
        self.set_time_mandante(time_mandante)
        self.set_time_visitante(time_visitante)
        self.set_gol_mandante(gol_mandante)
        self.set_gol_visitante(gol_visitante)
        self.set_id_campeonato(id_campeonato)

    # Métodos de acesso (getters)
    def get_id_jogo(self) -> int:
        return self.id_jogo

    def get_estadio(self) -> str:
        return self.estadio

    def get_time_mandante(self) -> str:
        return self.time_mandante

    def get_time_visitante(self) -> str:
        return self.time_visitante

    def get_gol_mandante(self) -> int:
        return self.gol_mandante

    def get_gol_visitante(self) -> int:
        return self.gol_visitante
    
    def get_id_campeonato(self) -> Campeonato:
        return self.id_campeonato

    # Métodos de modificação (setters)
    def set_id_jogo(self, id_jogo: int):
        self.id_jogo = id_jogo

    def set_estadio(self, estadio: str):
        self.estadio = estadio

    def set_time_mandante(self, time_mandante: str):
        self.time_mandante = time_mandante

    def set_time_visitante(self, time_visitante: str):
        self.time_visitante = time_visitante

    def set_gol_mandante(self, gol_mandante: int):
        self.gol_mandante = gol_mandante

    def set_gol_visitante(self, gol_visitante: int):
        self.gol_visitante = gol_visitante

    def set_id_campeonato(self, id_campeonato: Campeonato):
        self.id_campeonato = id_campeonato

    def to_string(self):
        return f"Jogos(Código do Jogo: {self.get_id_jogo()}, Estádio: {self.get_estadio()}, " \
               f"Mandante: {self.get_time_mandante()}, Visitante{self.get_time_visitante()}, " \
               f"Gol Mandante: {self.get_gol_mandante()}, Gol Visitante: {self.get_gol_visitante()}, " \
               f"Campeonato N°: {self.get_id_campeonato()})"