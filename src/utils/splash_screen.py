from utils import config

class SplashScreen:

    def __init__(self):
        # Nome(s) do(s) criador(es)
        self.created_by = "João Victor Leoni dos santos\n"
        + "Lucas Fraga de Andrade\n"
        + "Daniel José Holz\n"
        + "Gabriel dos Santos\n"
        + "Jhean Virginio Perim Pazetto\n"
        + "Guilherme Barbosa Medici Loureiro\n"
        + "Maria Eduarda Carlete"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"

    def get_documents_count(self, collection_name):
        # Retorna o total de registros computado pela query
        df = config.query_count(collection_name=collection_name)
        return df[f"total_{collection_name}"].values[0]

    def get_updated_screen(self):
        return f"""
        ########################################################
        #            GERENCIAR CAMPEONATO DE FUTEBOL                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - TIMES:         {str(self.get_documents_count(collection_name="times")).rjust(5)}
        #      2 - JOGADORES:      {str(self.get_documents_count(collection_name="jogadores")).rjust(5)}
        #      3 - CAMPEONATO:     {str(self.get_documents_count(collection_name="campeonato")).rjust(5)}
        #      4 - TABELA DO CAMPEONATO:        {str(self.get_documents_count(collection_name="tabelaCampeonato")).rjust(5)}
        #      5 - JOGOS: {str(self.get_documents_count(collection_name="jogos")).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """