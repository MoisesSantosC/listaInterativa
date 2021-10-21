from menus import startMenu
from menus import programExitMenu
from menus.funcionalidades import cleanMenu


def back():
    while True:
        print(f'''O que deseja fazer agora?
        \r[1] Menu Principal
        \r[2] Sair do Programa
        \r{31 * "="}''')

        op = input('Escolha sua opção (1 ou 2): ')

        if not (op == '1' or op == '2'):
            cleanMenu.clear()
            print('Verifique a opção digitada e tente novamente!\n')
            print(31 * '=')
            continue
        elif op == '1':
            startMenu.menu()
            break
        elif op == '2':
            cleanMenu.clear()
            programExitMenu.programExit()
            break
