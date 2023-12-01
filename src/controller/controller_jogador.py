import pandas as pd
from model.jogadores import Jogadores
from conexion.mongo_queries import MongoQueries

class Controller_Jogador:
    def __init__(self):
        self.mongo = MongoQueries()
        
    def inserir_jogador(self) -> Jogadores:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuario o novo CPF
        cpf = input("CPF (Novo): ")

        if self.verifica_existencia_jogador(cpf):
            # Solicita ao usuario o novo jogador
            id_time = input("Id do Time: ")
            nome = input("Nome (Novo): ")
            numero = input("Posição: ")
            data_nascimento = input("Data_nascimento")
            posicao = input("posição: ")
            # Insere e persiste o novo jogador
            self.mongo.db["jogadores"].insert_one({"cpf": cpf, "nome": nome, "numero": numero, "data_nascimento": data_nascimento, "poiscao": posicao})
            # Recupera os dados do novo jogador criado transformando em um DataFrame
            df_jogador = self.recupera_jogador(cpf)
            # Cria um novo objeto Jogadores
            novo_jogador = Jogadores(df_jogador.cpf.values[0],df_jogador.id_time.valoues[0] ,df_jogador.nome.values[0], df_jogador.numero.values[0],df_jogador.data_nascimento.values[0], df_jogador.posicao.values[0] )
            # Exibe os atributos do novo jogador
            print(novo_jogador.to_string())
            self.mongo.close()
            # Retorna o objeto novo_jogador para utilização posterior, caso necessário
            return novo_jogador
        else:
            self.mongo.close()
            print(f"O CPF {cpf} já está cadastrado.")
            return None

    def atualizar_jogador(self) -> Jogadores:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o código do jogador a ser alterado
        cpf = input("CPF do jogador que deseja alterar o nome: ")

        # Verifica se o jogador existe na base de dados
        if not self.verifica_existencia_jogador(cpf):
            # Solicita a nova descrição do jogador
            novo_nome = input("Nome (Novo): ")
            # Atualiza o nome do jogador existente
            self.mongo.db["jogador"].update_one({"cpf": f"{cpf}"}, {"$set": {"nome": novo_nome}})
            # Recupera os dados do novo jogaores criado transformando em um DataFrame
            df_jogador = self.recupera_jogador(cpf)
            # Cria um novo objeto jogador
            Jogadores_atualizado = Jogadores(df_jogador.cpf.values[0],df_jogador.id_time.valoues[0] ,df_jogador.nome.values[0], df_jogador.numero.values[0],df_jogador.data_nascimento.values[0], df_jogador.posicao.values[0])
            # Exibe os atributos do novo jogador
            print(Jogadores_atualizado())
            self.mongo.close()
            # Retorna o objeto jogadores_atualizado para utilização posterior, caso necessário
            return Jogadores_atualizado
        else:
            self.mongo.close()
            print(f"O CPF {cpf} não existe.")
            return None

    def excluir_jogador(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o CPF do Cliente a ser alterado
        cpf = input("CPF do Jogador que irá excluir: ")

        # Verifica se o jogadir existe na base de dados
        if not self.verifica_existencia_jogador(cpf):            
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_jogador = self.recupera_jogador(cpf)
            # Revome o cliente da tabela
            self.mongo.db["jogador"].delete_one({"cpf":f"{cpf}"})
            # Cria um novo objeto Cliente para informar que foi removido
            Jogadores_excluido = Jogadores(df_jogador.cpf.values[0],df_jogador.id_time.valoues[0] ,df_jogador.nome.values[0], df_jogador.numero.values[0],df_jogador.data_nascimento.values[0], df_jogador.posicao.values[0])
            self.mongo.close()
            # Exibe os atributos do cliente excluído
            print("Cliente Removido com Sucesso!")
            print(Jogadores_excluido.to_string())
        else:
            self.mongo.close()
            print(f"O CPF {cpf} não existe.")

    def verifica_existencia_jogador(self, cpf:str=None, external:bool=False) -> bool:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_jogador = pd.DataFrame(self.mongo.db["jogadores"].find({"cpf":f"{cpf}"}, {"cpf": 1, "nome": 1, "_id": 0}))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_jogador.empty

    def recupera_jogador(self, cpf:str=None, external:bool=False) -> pd.DataFrame:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo cliente criado transformando em um DataFrame
        df_jogador = pd.DataFrame(list(self.mongo.db["jogadores"].find({"cpf":f"{cpf}"}, {"cpf": 1, "nome": 1, "_id": 0})))
        
        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_jogador