from menus.funcionalidades import backToMenu
from menus.funcionalidades import cleanMenu


# Menu de saída do programa
def programExit():
    while True:
        msg_menu = '== Deseja realmente sair do programa? =='

        print(msg_menu)
        print('[1] - Sim')
        print('[2] - Não')
        print(len(msg_menu) * "=")

        # Capturando o valor de entrada do usuário
        quit_op = input('Escolha sua opção (1 ou 2): ')

        # Verificando as opções digitadas
        if not (quit_op == '1' or quit_op == '2'):
            print('Opção não encontrada. Por favor, tente novamente!')
        elif quit_op == '1':
            break
        elif quit_op == '2':
            cleanMenu.clear()
            backToMenu.back()
            break
