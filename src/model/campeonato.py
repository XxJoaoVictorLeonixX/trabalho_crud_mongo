class Campeonato:
    def __init__(self,
                 id_campeonato: int = None,
                 nome: str = None,
                 premiacao: float = None
                 ):
        self.set_id_campeonato(id_campeonato)
        self.set_nome(nome)
        self.set_premiacao(premiacao)

    # Métodos de acesso (getters)
    def get_id_campeonato(self) -> int:
        return self.id_campeonato

    def get_nome(self) -> str:
        return self.nome

    def get_premiacao(self) -> float:
        return self.premiacao

    # Métodos de modificação (setters)
    def set_id_campeonato(self, id_campeonato: int):
        self.id_campeonato = id_campeonato

    def set_nome(self, nome: str):
        self.nome = nome

    def set_premiacao(self, premiacao: float):
        self.premiacao = premiacao

    def to_string(self):
        return f"Campeonato(Campeonato N°: {self.get_id_campeonato()}, Nome: {self.get_nome()}, Premiação: {self.get_premiacao()})"