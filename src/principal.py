from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_campeonato import Controller_Campeonato
from controller.controller_jogador import Controller_Jogador
from controller.controller_jogo import Controller_Jogo
from controller.controller_tabelaCampeonato import Controller_tabelaCampeonato
from controller.controller_time import Controller_Time

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_campeonato = Controller_Campeonato()
ctrl_jogador = Controller_Jogador()
ctrl_jogo = Controller_Jogo()
ctrl_tabelaCampeonato = Controller_tabelaCampeonato()
ctrl_time = Controller_Time()

def reports(opcao_relatorio:int=0):

    if opcao_relatorio == 1:
        relatorio.get_relatorio_campeonato()            
    elif opcao_relatorio == 2:
        relatorio.get_relatorio_tabela_campeonato()
    elif opcao_relatorio == 3:
        relatorio.get_relatorio_jogos()
    elif opcao_relatorio == 4:
        relatorio.get_relatorio_times()
    elif opcao_relatorio == 5:
        relatorio.get_relatorio_jogadores()

def inserir(opcao_inserir:int=0):

    if opcao_inserir == 1:                               
        novo_campeonato = ctrl_campeonato.inserir_campeonato()
    elif opcao_inserir == 2:
        novo_jogador = ctrl_jogador.inserir_jogador()
    elif opcao_inserir == 3:
        novo_jogo = ctrl_jogo.inserir_jogo()
    elif opcao_inserir == 4:
        novo_tabelaCampeonato = ctrl_tabelaCampeonato.inserir_tabelaCampeonato()
    elif opcao_inserir == 5:
        novo_time = ctrl_time.inserir_time()

def atualizar(opcao_atualizar:int=0):

    if opcao_atualizar == 1:
        relatorio.get_relatorio_campeonato()
        campeonato_atualizado = ctrl_campeonato.atualizar_campeonato()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_jogadores()
        jogador_atualizado = ctrl_jogador.atualizar_jogador()
    elif opcao_atualizar == 3:
        relatorio.get_relatorio_jogos()
        jogo_atualizado = ctrl_jogo.atualizar_jogo()
    elif opcao_atualizar == 4:
        relatorio.get_relatorio_tabela_campeonato()
        tabelaCampeonato_atualizado = ctrl_tabelaCampeonato.atualizar_tabelaCampeonato()
    elif opcao_atualizar == 5:
        relatorio.get_relatorio_itens_pedidos()
        time_atualizado = ctrl_time.atualizar_time()

def excluir(opcao_excluir:int=0):

    if opcao_excluir == 1:
        relatorio.get_relatorio_campeonato()
        ctrl_campeonato.excluir_campeonato()
    elif opcao_excluir == 2:                
        relatorio.get_relatorio_jogadores()
        ctrl_jogador.excluir_jogador()
    elif opcao_excluir == 3:                
        relatorio.get_relatorio_jogos()
        ctrl_jogo.excluir_jogo()
    elif opcao_excluir == 4:                
        relatorio.get_relatorio_tabela_campeonato()
        ctrl_tabelaCampeonato.excluir_tabelaCampeonato()
    elif opcao_excluir == 5:
        relatorio.get_relatorio_times()
        ctrl_time.excluir_time()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)
        
        if opcao == 1: # Relatórios
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2: # Inserir Novos Registros
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3: # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4:

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()