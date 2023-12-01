import pandas as pd
from model.times import Times
from conexion.mongo_queries import MongoQueries

class Controller_Time:
    def __init__(self):
        self.mongo = MongoQueries()
        
    def inserir_time(self) -> Times:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuario o novo id_time
        id_time = input("ID time (novo)  ")

        if self.verifica_existencia_time(id_time):
            # Solicita ao usuario o novo nome
            nome = input("Nome (Novo): ")
            # Insere e persiste o novo time
            self.mongo.db["Times"].insert_one({"id_time": id_time, "nome": nome})
            # Recupera os dados do novo time criado transformando em um DataFrame
            df_time = self.recupera_time(id_time)
            # Cria um novo objeto time
            novo_time = Times(df_time.id_time.values[0], df_time.nome.values[0])
            # Exibe os atributos do novo time
            print(novo_time.to_string())
            self.mongo.close()
            # Retorna o objeto novo_time para utilização posterior, caso necessário
            return novo_time
        else:
            self.mongo.close()
            print(f"O time {id_time} já está cadastrado.")
            return None

    def atualizar_time(self) -> Times:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o código do time a ser alterado
        id_time = input("id_time do time que deseja alterar o nome: ")

        # Verifica se o time existe na base de dados
        if not self.verifica_existencia_time(id_time):
            # Solicita a nova descrição do time
            novo_nome = input("Nome (Novo): ")
            # Atualiza o nome do time existente
            self.mongo.db["times"].update_one({"id_time": f"{id_time}"}, {"$set": {"nome": novo_nome}})
            # Recupera os dados do novo time criado transformando em um DataFrame
            df_time = self.recupera_time(id_time)
            # Cria um novo objeto time
            Time_atualizado = Times(df_time.id_time.values[0], df_time.nome.values[0])
            # Exibe os atributos do novo time
            print(Time_atualizado.to_string())
            self.mongo.close()
            # Retorna o objeto time_atualizado para utilização posterior, caso necessário
            return Time_atualizado
        else:
            self.mongo.close()
            print(f"O time {id_time} não existe.")
            return None

    def excluir_time(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o id_time do time a ser alterado
        id_time = input("id de time do time que irá excluir: ")

        # Verifica se o time existe na base de dados
        if not self.verifica_existencia_time(id_time):            
            # Recupera os dados do novo time criado transformando em um DataFrame
            df_time = self.recupera_time(id_time)
            # Revome o time da tabela
            self.mongo.db["Times"].delete_one({"id_time":f"{id_time}"})
            # Cria um novo objeto time para informar que foi removido
            time_excluido = time(df_time.id_time.values[0], df_time.nome.values[0])
            self.mongo.close()
            # Exibe os atributos do time excluído
            print("time Removido com Sucesso!")
            print(time_excluido.to_string())
        else:
            self.mongo.close()
            print(f"O id_time {id_time} não existe.")

    def verifica_existencia_time(self, id_time:str=None, external:bool=False) -> bool:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo time criado transformando em um DataFrame
        df_time = pd.DataFrame(self.mongo.db["Times"].find({"id_time":f"{id_time}"}, {"id_time": 1, "nome": 1, "_id": 0}))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_time.empty

    def recupera_time(self, id_time:str=None, external:bool=False) -> pd.DataFrame:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo time criado transformando em um DataFrame
        df_time = pd.DataFrame(list(self.mongo.db["Times"].find({"id_time":f"{id_time}"}, {"id_time": 1, "nome": 1, "_id": 0})))
        
        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_time