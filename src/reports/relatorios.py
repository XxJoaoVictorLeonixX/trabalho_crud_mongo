from conexion.mongo_queries import MongoQueries
import pandas as pd
from pymongo import ASCENDING, DESCENDING

class Relatorio:
    
    def __init__(self):
        pass

    def get_relatorio_campeonato(self):
        mongo = MongoQueries()
        mongo.connect()
        relatorio_campeonato = mongo.db["campeonato"].aggregate(
            [
                {
                    "$project": {
                        "nome_campeonato": "$nome",
                        "premiacao": "$premiacao"
                    }
                },
                {
                    "$sort": {"premiacao": DESCENDING}
                },
                {
                    "$project": {
                        "_id": 0,
                        "nome_campeonato": "$nome_campeonato",
                        "premiacao": "$premiacao"
                    }
                }
            ]
        )
        df_relatorio_campeonato = pd.DataFrame(list(relatorio_campeonato))
        mongo.close()
        print(df_relatorio_campeonato)
        input("Pressione [Enter] para sair do relatório de campeonato...")

    def get_relatorio_tabela_campeonato(self):
        mongo = MongoQueries()
        mongo.connect()
        tabela_campeonato = mongo.db["tabelaCampeonato"].aggregate(
            [
                {
                    "$lookup": {
                        "from": "time",
                        "localField": "id_time",
                        "foreignField": "id_time",
                        "as": "time_info"
                    }
                },
                {
                    "$lookup": {
                        "from": "campeonato",
                        "localField": "id_campeonato",
                        "foreignField": "id_campeonato",
                        "as": "campeonato_info"
                    }
                },
                {
                    "$project": {
                        "nome_time": {"$arrayElemAt": ["$time_info.nome", 0]},
                        "nome_campeonato": {"$arrayElemAt": ["$campeonato_info.nome", 0]},
                        "vitorias": "$vitorias",
                        "derrotas": "$derrotas",
                        "empates": "$empates",
                        "gol_feito": "$gol_feito",
                        "gol_sofrido": "$gol_sofrido"
                    }
                },
                {
                    "$project": {
                        "_id": 0,
                        "nome_time": 1,
                        "nome_campeonato": 1,
                        "vitorias": 1,
                        "derrotas": 1,
                        "empates": 1,
                        "gol_feito": 1,
                        "gol_sofrido": 1
                    }
                }
            ]
        )
        df_relatorio_tabela_campeonato = pd.DataFrame(list(relatorio_tabela_campeonato))
        mongo.close()
        print(df_relatorio_tabela_campeonato)
        input("Pressione [Enter] para sair do relatório de tabelaCampeonato...")

    def get_relatorio_jogos(self):
        mongo = MongoQueries()
        mongo.connect()
        jogos = mongo.db["jogos"].aggregate(
            [
                {
                    "$lookup": {
                        "from": "campeonato",
                        "localField": "id_campeonato",
                        "foreignField": "id_campeonato",
                        "as": "campeonato_info"
                    }
                },
                {
                    "$project": {
                        "nome_campeonato": {"$arrayElemAt": ["$campeonato_info.nome", 0]},
                        "estadio": "$estadio",
                        "time_mandante": "$time_mandante",
                        "time_visitante": "$time_visitante",
                        "gol_mandante": "$gol_mandante",
                        "gol_visitante": "$gol_visitante"
                    }
                },
                {
                    "$project": {
                        "_id": 0,
                        "nome_campeonato": 1,
                        "estadio": 1,
                        "time_mandante": 1,
                        "time_visitante": 1,
                        "gol_mandante": 1,
                        "gol_visitante": 1
                    }
                }
            ]
        )
        df_relatorio_jogos = pd.DataFrame(list(relatorio_jogos))
        mongo.close()
        print(df_relatorio_jogos)
        input("Pressione [Enter] para sair do relatório de jogos...")

    def get_relatorio_times(self):
        mongo = MongoQueries()
        mongo.connect()
        times = mongo.db["times"].find(
            {},
            {"id_time": 1, "nome": 1, "_id": 0}
        ).sort("id_time", ASCENDING)
        df_time = pd.DataFrame(list(times))
        print(df_time)
        input("Pressione [Enter] para sair do relatório de Times...")
        mongo.close()

    def get_relatorio_jogadores(self):
        mongo = MongoQueries()
        mongo.connect()
        jogadores = mongo.db["jogadores"].find(
            {},
            {"CPF": 1, "id_time": 1, "nome": 1, "numero": 1, "data_nascimento": 1, "posicao": 1, "_id": 0}
        )
        df_time = pd.DataFrame(list(jogadores))
        print(df_time)
        input("Pressione [Enter] para sair do relatório de Jogadores...")
        mongo.close()