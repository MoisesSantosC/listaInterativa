from menus.funcionalidades import backToMenu
from menus.funcionalidades import cleanMenu


# Menu de saída do programa
def programExit():
    while True:
        msg_menu = '== Deseja realmente sair do programa? =='

        print(f'''{msg_menu}
             \r[1] - Sim
             \r[2] - Não
             \r{len(msg_menu) * "="}''')

        # Capturando o valor de entrada do usuário
        quit_op = input('Escolha sua opção (1 ou 2): ')

        # Verificando as opções digitadas
        if not (quit_op == '1' or quit_op == '2'):
            cleanMenu.clear()
            print('Opção não encontrada. Por favor, tente novamente!\n')
            continue
        elif quit_op == '1':
            cleanMenu.clear()
            print('Programa Finalizado!')
            break
        elif quit_op == '2':
            cleanMenu.clear()
            backToMenu.back()
            break
