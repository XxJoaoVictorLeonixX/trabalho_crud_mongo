import pandas as pd
from model.campeonato import Campeonato
from conexion.mongo_queries import MongoQueries

class Controller_Campeonato:
    def __init__(self):
        self.mongo = MongoQueries()
        
    def inserir_campeonato(self) -> campeonato:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuario o novo id_campeonato
        id_campeonato = input("id_campeonato (Novo): ")

        if self.verifica_existencia_campeonato(id_campeonato):
            # Solicita ao usuario o novo nome
            nome = input("Nome (Novo): ")
            premiacao = input("premiacao:")
            # Insere e persiste o novo campeonato
            self.mongo.db["campeonatos"].insert_one({"id_campeonato": id_campeonato, "nome": nome})
            # Recupera os dados do novo campeonato criado transformando em um DataFrame
            df_campeonato = self.recupera_campeonato(id_campeonato)
            # Cria um novo objeto campeonato
            novo_campeonato = campeonato(df_campeonato.id_campeonato.values[0], df_campeonato.nome.values[0], df.premiacao.values[0])
            # Exibe os atributos do novo campeonato
            print(novo_campeonato.to_string())
            self.mongo.close()
            # Retorna o objeto novo_campeonato para utilização posterior, caso necessário
            return novo_campeonato
        else:
            self.mongo.close()
            print(f"O id_campeonato {id_campeonato} já está cadastrado.")
            return None

    def atualizar_campeonato(self) -> campeonato:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o código do campeonato a ser alterado
        id_campeonato = input("id_campeonato do campeonato que deseja alterar o nome: ")

        # Verifica se o campeonato existe na base de dados
        if not self.verifica_existencia_campeonato(id_campeonato):
            # Solicita a nova descrição do campeonato
            novo_nome = input("Nome (Novo): ")
            # Atualiza o nome do campeonato existente
            self.mongo.db["campeonatos"].update_one({"id_campeonato": f"{id_campeonato}"}, {"$set": {"nome": novo_nome}})
            # Recupera os dados do novo campeonato criado transformando em um DataFrame
            df_campeonato = self.recupera_campeonato(id_campeonato)
            # Cria um novo objeto campeonato
            campeonato_atualizado = campeonato(df_campeonato.id_campeonato.values[0], df_campeonato.nome.values[0], df_premiacao.values[0])
            # Exibe os atributos do novo campeonato
            print(campeonato_atualizado.to_string())
            self.mongo.close()
            # Retorna o objeto campeonato_atualizado para utilização posterior, caso necessário
            return campeonato_atualizado
        else:
            self.mongo.close()
            print(f"O campeonato {id_campeonato} não existe.")
            return None

    def excluir_campeonato(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o id_campeonato do campeonato a ser alterado
        id_campeonato = input("id_campeonato do campeonato que irá excluir: ")

        # Verifica se o campeonato existe na base de dados
        if not self.verifica_existencia_campeonato(id_campeonato):            
            # Recupera os dados do novo campeonato criado transformando em um DataFrame
            df_campeonato = self.recupera_campeonato(id_campeonato)
            # Revome o campeonato da tabela
            self.mongo.db["campeonatos"].delete_one({"id_campeonato":f"{id_campeonato}"})
            # Cria um novo objeto campeonato para informar que foi removido
            campeonato_excluido = campeonato(df_campeonato.id_campeonato.values[0], df_campeonato.nome.values[0])
            self.mongo.close()
            # Exibe os atributos do campeonato excluído
            print("campeonato Removido com Sucesso!")
            print(campeonato_excluido.to_string())
        else:
            self.mongo.close()
            print(f"O campeonato {id_campeonato} não existe.")

    def verifica_existencia_campeonato(self, id_campeonato:str=None, external:bool=False) -> bool:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo campeonato criado transformando em um DataFrame
        df_campeonato = pd.DataFrame(self.mongo.db["campeonatos"].find({"id_campeonato":f"{id_campeonato}"}, {"id_campeonato": 1, "nome": 1, "_id": 0}))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_campeonato.empty

    def recupera_campeonato(self, id_campeonato:str=None, external:bool=False) -> pd.DataFrame:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo campeonato criado transformando em um DataFrame
        df_campeonato = pd.DataFrame(list(self.mongo.db["campeonatos"].find({"id_campeonato":f"{id_campeonato}"}, {"id_campeonato": 1, "nome": 1, "_id": 0})))
        
        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_campeonato