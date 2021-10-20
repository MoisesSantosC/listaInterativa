from menus import startMenu
from menus import programExitMenu
from menus.funcionalidades import cleanMenu


def back():
    while True:
        msg = '''O que deseja fazer agora?
        \r[1] Menu Principal
        \r[2] Sair do Programa
        '''

        print(msg)
        op = input('Sua opção: ')

        if not (op == '1' or op == '2'):
            print('\nVerifique a opção digitada e tente novamente\n')
            continue
        elif op == '1':
            startMenu.menu()
            break
        elif op == '2':
            cleanMenu.clear()
            programExitMenu.programExit()
            break
