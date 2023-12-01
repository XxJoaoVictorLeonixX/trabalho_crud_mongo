from model.times import Times
from model.campeonato import Campeonato

class TabelaCampeonato:
    def __init__(self,
                 vitorias: int = None,
                 derrotas: int = None,
                 empates: int = None,
                 gol_feito: int = None,
                 gol_sofrido: int = None,
                 id_time: Times = None,
                 id_campeonato: Campeonato = None
                 ):
        self.set_vitorias(vitorias)
        self.set_derrotas(derrotas)
        self.set_empates(empates)
        self.set_gol_feito(gol_feito)
        self.set_gol_sofrido(gol_sofrido)
        self.set_id_time(id_time)
        self.set_id_campeonato(id_campeonato)

    # Métodos de acesso (getters)
    def get_vitorias(self) -> int:
        return self.vitorias

    def get_derrotas(self) -> int:
        return self.derrotas

    def get_empates(self) -> int:
        return self.empates

    def get_gol_feito(self) -> int:
        return self.gol_feito

    def get_gol_sofrido(self) -> int:
        return self.gol_sofrido
    
    def get_id_time(self) -> Times:
        return self.id_time
    
    def get_id_campeonato(self) -> Campeonato:
        return self.id_campeonato

    # Métodos de modificação (setters)
    def set_vitorias(self, vitorias: int):
        self.vitorias = vitorias

    def set_derrotas(self, derrotas: int):
        self.derrotas = derrotas

    def set_empates(self, empates: int):
        self.empates = empates

    def set_gol_feito(self, gol_feito: int):
        self.gol_feito = gol_feito

    def set_gol_sofrido(self, gol_sofrido: int):
        self.gol_sofrido = gol_sofrido

    def set_id_time(self, id_time: Times):
        self.id_time = id_time

    def set_id_campeonato(self, id_campeonato: Campeonato):
        self.id_campeonato = id_campeonato

    def to_string(self):
        return f"Tabela Campeonato (Vitorias: {self.get_vitorias}, Derrotas: {self.get_derrotas}, Empates: {self.get_empates}, " \
               f"GP: {self.get_gol_feito}, GC: {self.get_gol_sofrido}, " \
               f"Time N°: {self.get_id_time}, Campeonato N:{self.get_id_campeonato})"