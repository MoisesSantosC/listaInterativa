# Importando os Módulos
from menus.programExitMenu import programExit
from menus.funcionalidades.cleanMenu import clear

# Menu inicial
def menu():
    clear()
    msg_menu = f'{10*"="} Menu de Opções {10*"="}'
    
    print(msg_menu)
    print('[1] - Criar uma lista')
    print('[2] - Ver Listas')
    print('[3] - Sair')
    print(len(msg_menu) * "=")
    
    # Capturando o valor de entrada do usuário
    menu_op = input('Escolha sua opção (1, 2 ou 3): ')
    checkMenuOptions(menu_op)

# Verifica as opções digitadas do menu principal
def checkMenuOptions(op):
    op = op.strip()  # elimina os espaços no começo e final da string
    if op == '1':
        clear()  # limpa a tela do terminal
        print('Você selecionou a opção de Criar uma Lista\n')
        
    elif op == '2':
        clear()  # limpa a tela do terminal
        print('Você selecionou a opção de Ver Listas\n')
        
    elif op == '3':
        clear()  # limpa a tela do terminal
        print('Você selecionou a opção de Sair\n')
        programExit()  # Menu da terceira opção
        
    else:
        clear()
        print('Selecione uma das opções (1, 2 ou 3)\n')
        menu()  # Executando o menu
