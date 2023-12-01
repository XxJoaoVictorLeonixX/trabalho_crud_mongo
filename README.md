# Trabalho c3

Repositorio para o trabalho da c3 de banco de Dados Ministrada Pelo Professor Howard Cruz 

## Tema - Campeonato de Futebol :soccer:

Este projeto é um sistema de gerenciamento de partidas de futebol desenvolvido em Python e SQL, criado como parte de um trabalho acadêmico da matéria de Banco de dados do professor Howard Cruz. Ele oferece uma solução  para controlar jogadores, times e resultados de partidas. Com este sistema, você pode cadastrar,cadastrar, visualizar e analisar informações sobre times, jogadores e partidas 

Com os dados fornecidos rodada a rodada todos os dados são convertidos em uma tabela com a classificação do campeonato e outros dados, gerando assim uma classificação na junção de todas as tabelas e é revelado quem foi o campeão e a classificação geral.

## Como Rodar a aplicação :hammer:

~$ python createCollectionsAndData.py
Atenção: tendo em vista que esse projeto é continuidade do example_crud_oracle, é importante que as tabelas do Oracle existam e estejam preenchidas, pois o script createCollectionsAndData.py irá realizar uma consulta em cada uma das tabelas e preencher as collections com os novos documents.

Para executar o sistema basta executar o script Python a seguir:

~$ python principal.py

# Exemplo de Sistema em Python fazendo CRUD no MongoDB

diagrams: Nesse diretório está o diagrama relacional (lógico) do sistema.

O sistema possui cinco entidades: CAMPEONATO, JOGADORES, JOGOS, TABELA_CAMPEONATO e TIMES

src: Nesse diretório estão os scripts do sistema

conexion: Nesse repositório encontra-se o módulo de conexão com o banco de dados Oracle e o módulo de conexão com o banco de dados Mongo. Esses módulos possuem algumas funcionalidades úteis para execução de instruções. O módulo do Oracle permite obter como resultado das queries JSON, Matriz e Pandas DataFrame. Já o módulo do Mongo apenas realiza a conexão, os métodos CRUD e de recuperação de dados são implementados diretamente nos objetos controladores (Controllers) e no objeto de Relatório (reports).

controller: Nesse diretório encontram-sem as classes controladoras, responsáveis por realizar inserção, alteração e exclusão dos registros das tabelas.

model: Nesse diretório encontram-ser as classes das entidades descritas no diagrama relacional

reports Nesse diretório encontra-se a classe responsável por gerar todos os relatórios do sistema

utils: Nesse diretório encontram-se scripts de configuração e automatização da tela de informações iniciais

createCollectionsAndData.py: Script responsável por criar as tabelas e registros fictícios. Esse script deve ser executado antes do script principal.py para gerar as tabelas, caso não execute os scripts diretamente no SQL Developer ou em alguma outra IDE de acesso ao Banco de Dados.

principal.py: Script responsável por ser a interface entre o usuário e os módulos de acesso ao Banco de Dados. Deve ser executado após a criação das tabelas.

# Bibliotecas Utilizadas

requirements.txt: pip install -r requirements.txt

## Organização 📁 
- [diagrams](diagrams): Nesse diretório está o [diagrama relacional](diagrams/DIAGRAMA_RELACIONAL_PEDIDOS.pdf) (lógico) do sistema.
    * O sistema possui cinco entidades: PRODUTOS, CLIENTES, FORNECEDORES, PEDIDOS e ITENS_PEDIDO
- [src](src): Nesse diretório estão os scripts do sistema
    * [conexion](src/conexion): Nesse repositório encontra-se o [módulo de conexão com o banco de dados Oracle](src/conexion/oracle_queries.py) e o [módulo de conexão com o banco de dados Mongo](src/conexion/mongo_queries.py). Esses módulos possuem algumas funcionalidades úteis para execução de instruções. O módulo do Oracle permite obter como resultado das queries JSON, Matriz e Pandas DataFrame. Já o módulo do Mongo apenas realiza a conexão, os métodos CRUD e de recuperação de dados são implementados diretamente nos objetos controladores (_Controllers_) e no objeto de Relatório (_reports_).
      - Exemplo de utilização para consultas simples no Oracle:

        ```python
        def listar_clientes(self, oracle:OracleQueries, need_connect:bool=False):
            query = """
                    select c.cpf
                        , c.nome 
                    from clientes c
                    order by c.nome
                    """
            if need_connect:
                oracle.connect()
            print(oracle.sqlToDataFrame(query))
        ```
      - Exemplo de utilização para alteração de registros no Oracle

        ```python
        from conexion.oracle_queries import OracleQueries
        def inserir_cliente(self) -> Cliente:
            # Cria uma nova conexão com o banco que permite alteração
            oracle = OracleQueries(can_write=True)
            oracle.connect()

            # Solicita ao usuario o novo CPF
            cpf = input("CPF (Novo): ")

            if self.verifica_existencia_cliente(oracle, cpf):
                # Solicita ao usuario o novo nome
                nome = input("Nome (Novo): ")
                # Insere e persiste o novo cliente
                oracle.write(f"insert into clientes values ('{cpf}', '{nome}')")
                # Recupera os dados do novo cliente criado transformando em um DataFrame
                df_cliente = oracle.sqlToDataFrame(f"select cpf, nome from clientes where cpf = '{cpf}'")
                # Cria um novo objeto Cliente
                novo_cliente = Cliente(df_cliente.cpf.values[0], df_cliente.nome.values[0])
                # Exibe os atributos do novo cliente
                print(novo_cliente.to_string())
                # Retorna o objeto novo_cliente para utilização posterior, caso necessário
                return novo_cliente
            else:
                print(f"O CPF {cpf} já está cadastrado.")
                return None
        ```
      - Caso esteja utilizando na máquina virtual antiga, você precisará alterar o método connect de:
          ```python
          self.conn = cx_Oracle.connect(user=self.user,
                                  password=self.passwd,
                                  dsn=self.connectionString()
                                  )
          ```
        Para:
          ```python
          self.conn = cx_Oracle.connect(user=self.user,
                                  password=self.passwd,
                                  dsn=self.connectionString(in_container=True)
                                  )
          ```
      - Exemplo de utilização para conexão no Mongo;
      ```python
            # Importa o módulo MongoQueries
            from conexion.mongo_queries import MongoQueries
            
            # Cria o objeto MongoQueries
            mongo = MongoQueries()

            # Realiza a conexão com o Mongo
            mongo.connect()

            """<inclua aqui suas declarações>"""

            # Fecha a conexão com o Mong
            mongo.close()
      ```
      - Exemplo de criação de um documento no Mongo:
      ```python
            from conexion.mongo_queries import MongoQueries
            import pandas as pd
            
            # Cria o objeto MongoQueries
            mongo = MongoQueries()

            # Realiza a conexão com o Mongo
            mongo.connect()

            # Solicita ao usuario o novo CPF
            cpf = input("CPF (Novo): ")
            # Solicita ao usuario o novo nome
            nome = input("Nome (Novo): ")
            # Insere e persiste o novo cliente
            mongo.db["clientes"].insert_one({"cpf": cpf, "nome": nome})
            # Recupera os dados do novo cliente criado transformando em um DataFrame
            df_cliente = pd.DataFrame(list(mongo.db["clientes"].find({"cpf":f"{cpf}"}, {"cpf": 1, "nome": 1, "_id": 0})))
            # Exibe os dados do cliente em formato DataFrame
            print(df_cliente)

            # Fecha a conexão com o Mong
            mongo.close()
      ```
    * [controller](src/controller/): Nesse diretório encontram-sem as classes controladoras, responsáveis por realizar inserção, alteração e exclusão dos registros das tabelas.
    * [model](src/model/): Nesse diretório encontram-ser as classes das entidades descritas no [diagrama relacional](diagrams/DIAGRAMA_RELACIONAL_PEDIDOS.pdf)
    * [reports](src/reports/) Nesse diretório encontra-se a [classe](src/reports/relatorios.py) responsável por gerar todos os relatórios do sistema
    * [utils](src/utils/): Nesse diretório encontram-se scripts de [configuração](src/utils/config.py) e automatização da [tela de informações iniciais](src/utils/splash_screen.py)
    * [createCollectionsAndData.py](src/createCollectionsAndData.py): Script responsável por criar as tabelas e registros fictícios. Esse script deve ser executado antes do script [principal.py](src/principal.py) para gerar as tabelas, caso não execute os scripts diretamente no SQL Developer ou em alguma outra IDE de acesso ao Banco de Dados.
    * [principal.py](src/principal.py): Script responsável por ser a interface entre o usuário e os módulos de acesso ao Banco de Dados. Deve ser executado após a criação das tabelas.

### Bibliotecas Utilizadas
- [requirements.txt](src/requirements.txt): `pip install -r requirements.txt`

## Integrantes
* João Victor Leoni dos santos
* Lucas Fraga de Andrade
* Daniel José Holz 
* Gabriel dos Santos
* Jhean Virginio Perim Pazetto
* Guilherme Barbosa Medici Loureiro 
* Maria Eduarda André Carlete 

