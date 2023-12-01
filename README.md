# Exemplo de Sistema em Python fazendo CRUD no MongoDB
Esse sistema de exemplo é composto por um conjunto de coleções(collections) que representam pedidos de vendas, contendo coleções como: campeonato, jogadores, jogos, tabela do campeonato e times.

O sistema exige que as coleções existam, então basta executar o script Python a seguir para criação das coleções e preenchimento de dados de exemplos:

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
