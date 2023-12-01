class Times:
    def __init__(self,
                 id_time: int = None,
                 nome: str = None
                 ):
        self.set_id_time(id_time)
        self.set_nome(nome)

    def get_id_time(self) -> int:
        return self.id_time

    def get_nome(self) -> str:
        return self.nome

    def set_id_time(self, id_time: int):
        self.id_time = id_time

    def set_nome(self, nome: str):
        self.nome = nome

    def to_string(self):
        return f"Times: (Time N°: {self.get_id_time()}, Nome: {self.get_nome()})"