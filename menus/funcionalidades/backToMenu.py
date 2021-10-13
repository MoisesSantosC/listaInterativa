from menus import startMenu
from menus import programExitMenu


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
        elif op == '1':
            startMenu.menu()
        elif op == '2':
            programExitMenu.programExit()
