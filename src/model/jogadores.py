class Jogadores:
    def __init__(self,
                 CPF: int = None,
                 id_time: Times = None,
                 nome: str = None,
                 numero: int = None,
                 data_nascimento: str = None,
                 posicao: str = None
                 ):
        self.set_CPF(CPF)
        self.set_id_time(id_time)
        self.set_nome(nome)
        self.set_numero(numero)
        self.set_data_nascimento(data_nascimento)
        self.set_posicao(posicao)

    # Métodos de acesso (getters)
    def get_CPF(self) -> int:
        return self.CPF
    
    def get_id_time(self) -> Times:
        return self.id_time

    def get_nome(self) -> str:
        return self.nome

    def get_numero(self) -> int:
        return self.numero

    def get_data_nascimento(self) -> str:
        return self.data_nascimento

    def get_posicao(self) -> str:
        return self.posicao

    # Métodos de modificação (setters)
    def set_CPF(self, CPF: int):
        self.CPF = CPF

    def set_id_time(self, id_time: Times):
        self.id_time = id_time

    def set_nome(self, nome: str):
        self.nome = nome

    def set_numero(self, numero: int):
        self.numero = numero

    def set_data_nascimento(self, data_nascimento: str):
        self.data_nascimento = data_nascimento

    def set_posicao(self, posicao: str):
        self.posicao = posicao

    def to_string(self):
        return f"Jogadores(CPF: {self.get_CPF()}, Código Time: ={self.get_id_time()}, Nome: {self.get_nome()}, " \
               f"Número: {self.get_numero()}, Nascimento: {self.get_data_nascimento()}, Posição: {self.get_posicao()})"