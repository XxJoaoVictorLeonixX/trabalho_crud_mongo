import pandas as pd
from model.tabelaCampeonato import tabelaCampeonato
from conexion.mongo_queries import MongoQueries

class Controller_tabelaCampeonato:
    def __init__(self):
        self.mongo = MongoQueries()
        
    def inserir_tabelaCampeonato(self) -> tabelaCampeonato:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuario o novo id_campeonato
        id_campeonato = input("id_campeonato (Novo): ")

        if self.verifica_existencia_tabelaCampeonato(id_campeonato):
            id_time = input("id_time (Novo): ")
            vitoria = input("Vitorias? ")
            derrota = input("Derrotas: ")
            gol_feito = input("Gol feitos: ")
            gol_sofrido = input("Gols Sofridos:")
            # Insere e persiste o novo tabelaCampeonato
            self.mongo.db["tabelaCampeonatos"].insert_one({"id_campeonato": id_campeonato, "id_time": id_time}, "vitorias" : vitoria, "derrota": derrota, "gol feito": gol_feito, "Gol tomado": gol_sofrido)
            # Recupera os dados do novo tabelaCampeonato criado transformando em um DataFrame
            df_tabelaCampeonato = self.recupera_tabelaCampeonato(id_campeonato)
            # Cria um novo objeto tabelaCampeonato
            novo_tabelaCampeonato = tabelaCampeonato(df_tabelaCampeonato.id_campeonato.values[0], df_tabelaCampeonato.id_time.values[0], df_tabelaCampeonato.vitoria.values[0], df_tabelaCampeonato.derota.values[0], df_tabelaCampeonato.gol_feito.values[0], df_tabelaCampeonato.gol_sofrido.values[0])
            # Exibe os atributos do novo tabelaCampeonato
            print(novo_tabelaCampeonato.to_string())
            self.mongo.close()
            # Retorna o objeto novo_tabelaCampeonato para utilização posterior, caso necessário
            return novo_tabelaCampeonato
        else:
            self.mongo.close()
            print(f"O id_campeonato {id_campeonato} já está cadastrado.")
            return None

    def atualizar_tabelaCampeonato(self) -> tabelaCampeonato:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o código do tabelaCampeonato a ser alterado
        id_campeonato = input("id_campeonato do tabelaCampeonato que deseja alterar o id_time: ")

        # Verifica se o tabelaCampeonato existe na base de dados
        if not self.verifica_existencia_tabelaCampeonato(id_campeonato):
            # Solicita a nova descrição do tabelaCampeonato
            novo_id_time = input("id_time (Novo): ")
            # Atualiza o id_time do tabelaCampeonato existente
            self.mongo.db["tabelaCampeonatos"].update_one({"id_campeonato": f"{id_campeonato}"}, {"$set": {"id_time": novo_id_time}})
            # Recupera os dados do novo tabelaCampeonato criado transformando em um DataFrame
            df_tabelaCampeonato = self.recupera_tabelaCampeonato(id_campeonato)
            # Cria um novo objeto tabelaCampeonato
            tabelaCampeonato_atualizado = tabelaCampeonato(df_tabelaCampeonato.id_campeonato.values[0], df_tabelaCampeonato.id_time.values[0], df_tabelaCampeonato.vitoria.values[0], df_tabelaCampeonato.derota.values[0], df_tabelaCampeonato.gol_feito.values[0], df_tabelaCampeonato.gol_sofrido.values[0])
            # Exibe os atributos do novo tabelaCampeonato
            print(tabelaCampeonato_atualizado.to_string())
            self.mongo.close()
            # Retorna o objeto tabelaCampeonato_atualizado para utilização posterior, caso necessário
            return tabelaCampeonato_atualizado
        else:
            self.mongo.close()
            print(f"O id_campeonato {id_campeonato} não existe.")
            return None

    def excluir_tabelaCampeonato(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o id_campeonato do tabelaCampeonato a ser alterado
        id_campeonato = input("id_campeonato do tabelaCampeonato que irá excluir: ")

        # Verifica se o tabelaCampeonato existe na base de dados
        if not self.verifica_existencia_tabelaCampeonato(id_campeonato):            
            # Recupera os dados do novo tabelaCampeonato criado transformando em um DataFrame
            df_tabelaCampeonato = self.recupera_tabelaCampeonato(id_campeonato)
            # Revome o tabelaCampeonato da tabela
            self.mongo.db["tabelaCampeonatos"].delete_one({"id_campeonato":f"{id_campeonato}"})
            # Cria um novo objeto tabelaCampeonato para informar que foi removido
            tabelaCampeonato_excluido = tabelaCampeonato(df_tabelaCampeonato.id_campeonato.values[0], df_tabelaCampeonato.id_time.values[0])
            self.mongo.close()
            # Exibe os atributos do tabelaCampeonato excluído
            print("tabelaCampeonato Removido com Sucesso!")
            print(tabelaCampeonato_excluido.to_string())
        else:
            self.mongo.close()
            print(f"O id_campeonato {id_campeonato} não existe.")

    def verifica_existencia_tabelaCampeonato(self, id_campeonato:str=None, external:bool=False) -> bool:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo tabelaCampeonato criado transformando em um DataFrame
        df_tabelaCampeonato = pd.DataFrame(self.mongo.db["tabelaCampeonatos"].find({"id_campeonato":f"{id_campeonato}"}, {"id_campeonato": 1, "id_time": 1, "_id": 0}))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_tabelaCampeonato.empty

    def recupera_tabelaCampeonato(self, id_campeonato:str=None, external:bool=False) -> pd.DataFrame:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo tabelaCampeonato criado transformando em um DataFrame
        df_tabelaCampeonato = pd.DataFrame(list(self.mongo.db["tabelaCampeonatos"].find({"id_campeonato":f"{id_campeonato}"}, {"id_campeonato": 1, "id_time": 1, "_id": 0})))
        
        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_tabelaCampeonato