import pandas as pd
from model.jogos import Jogos
from conexion.mongo_queries import MongoQueries

class Controller_Jogo:
    def __init__(self):
        self.mongo = MongoQueries()
        
    def inserir_jogo(self) -> jogo:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuario o novo id_jogo
        id_jogo = input("id_jogo (Novo): ")

        if self.verifica_existencia_jogo(id_jogo):
            # Solicita ao usuario o novo estadio
            estadio = input("estadio (Novo): ")
            time_mandante = input("Time mandante: ")
            time_visitante = input("Time Visitante: ")
            gol_mandante = input("Gol mandante: ")
            gol_visitante = input("Gol visitante: ")
            id_campeonato = input("id do campeonato: ")
            # Insere e persiste o novo jogo
            self.mongo.db["jogos"].insert_one({"id_jogo": id_jogo, "estadio": estadio}, "time_mandante": time_mandante, "time_visitante": time_visitante, "gol_mandante": gol_mandante, "gol_visitante": gol_visitante, "Id_campeonato": Id_campeonato)
            # Recupera os dados do novo jogo criado transformando em um DataFrame
            df_jogo = self.recupera_jogo(id_jogo)
            # Cria um novo objeto jogo
            novo_jogo = jogo(df_jogo.id_jogo.values[0], df_jogo.estadio.values[0], df_jogo.estadio.values[0],df_time_mandante.values[0], df_time_visitante.values[0],df_gol_mandante.values[0], df_gol_visistante.values[0], df_id_campeonato.values[0])
            # Exibe os atributos do novo jogo
            print(novo_jogo.to_string())
            self.mongo.close()
            # Retorna o objeto novo_jogo para utilização posterior, caso necessário
            return novo_jogo
        else:
            self.mongo.close()
            print(f"O jogo {id_jogo} já está cadastrado.")
            return None

    def atualizar_jogo(self) -> jogo:
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o código do jogo a ser alterado
        id_jogo = input("id_jogo do jogo que deseja alterar o estadio: ")

        # Verifica se o jogo existe na base de dados
        if not self.verifica_existencia_jogo(id_jogo):
            # Solicita a nova descrição do jogo
            novo_estadio = input("estadio (Novo): ")
            # Atualiza o estadio do jogo existente
            self.mongo.db["jogos"].update_one({"id_jogo": f"{id_jogo}"}, {"$set": {"estadio": novo_estadio}})
            # Recupera os dados do novo jogo criado transformando em um DataFrame
            df_jogo = self.recupera_jogo(id_jogo)
            # Cria um novo objeto jogo
            jogo_atualizado = jogo(df_jogo.id_jogo.values[0], df_jogo.estadio.values[0], df_jogo.estadio.values[0],df_time_mandante.values[0], df_time_visitante.values[0],df_gol_mandante.values[0], df_gol_visistante.values[0], df_id_campeonato.values[0])
            # Exibe os atributos do novo jogo
            print(jogo_atualizado.to_string())
            self.mongo.close()
            # Retorna o objeto jogo_atualizado para utilização posterior, caso necessário
            return jogo_atualizado
        else:
            self.mongo.close()
            print(f"O jogo {id_jogo} não existe.")
            return None

    def excluir_jogo(self):
        # Cria uma nova conexão com o banco que permite alteração
        self.mongo.connect()

        # Solicita ao usuário o id_jogo do jogo a ser alterado
        id_jogo = input("id_jogo do jogo que irá excluir: ")

        # Verifica se o jogo existe na base de dados
        if not self.verifica_existencia_jogo(id_jogo):            
            # Recupera os dados do novo jogo criado transformando em um DataFrame
            df_jogo = self.recupera_jogo(id_jogo)
            # Revome o jogo da tabela
            self.mongo.db["jogos"].delete_one({"id_jogo":f"{id_jogo}"})
            # Cria um novo objeto jogo para informar que foi removido
            jogo_excluido = jogo(df_jogo.id_jogo.values[0], df_jogo.estadio.values[0], df_jogo.estadio.values[0],df_time_mandante.values[0], df_time_visitante.values[0],df_gol_mandante.values[0], df_gol_visistante.values[0], df_id_campeonato.values[0])
            self.mongo.close()
            # Exibe os atributos do jogo excluído
            print("jogo Removido com Sucesso!")
            print(jogo_excluido.to_string())
        else:
            self.mongo.close()
            print(f"O jogo {id_jogo} não existe.")

    def verifica_existencia_jogo(self, id_jogo:str=None, external:bool=False) -> bool:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo jogo criado transformando em um DataFrame
        df_jogo = pd.DataFrame(self.mongo.db["jogos"].find({"id_jogo":f"{id_jogo}"}, {"id_jogo": 1, "estadio": 1, "_id": 0}))

        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_jogo.empty

    def recupera_jogo(self, id_jogo:str=None, external:bool=False) -> pd.DataFrame:
        if external:
            # Cria uma nova conexão com o banco que permite alteração
            self.mongo.connect()

        # Recupera os dados do novo jogo criado transformando em um DataFrame
        df_jogo = pd.DataFrame(list(self.mongo.db["jogos"].find({"id_jogo":f"{id_jogo}"}, {"id_jogo": 1, "estadio": 1, "_id": 0})))
        
        if external:
            # Fecha a conexão com o Mongo
            self.mongo.close()

        return df_jogo