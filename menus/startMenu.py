# Importando os Módulos
from menus.listCreationMenu import listCreation
from menus.listViewMenu import listView
from menus.programExitMenu import programExit
from menus.cleanMenu import clear

# Menu inicial
def menu():
    print(f'{10*"="} Menu de Opções {10*"="}')
    print('[1] - Criar uma lista')
    print('[2] - Ver Listas')
    print('[3] - Sair')
    print(36*"=")
    
    # Capturando o valor de entrada do usuário
    menu_op = input('Escolha sua opção (1, 2 ou 3): ')
    checkMenuOptions(menu_op)

# Verifica as opções digitadas do menu principal
def checkMenuOptions(op):
    op = op.strip()  # elimina os espaços no começo e final da string
    if op == '1':
        clear()  # limpa a tela do terminal
        print('Você selecionou a opção de Criar uma Lista\n')
        listCreation()  # Menu da primeira opção
        
    elif op == '2':
        clear()  # limpa a tela do terminal
        print('Você selecionou a opção de Ver Listas\n')
        listView()  # Menu da segunda opção
        
    elif op == '3':
        clear()  # limpa a tela do terminal
        print('Você selecionou a opção de Sair\n')
        programExit()  # Menu da terceira opção
        
    else:
        clear()
        print('Selecione uma das opções (1, 2 ou 3)\n')
        menu()  # Executando o menu
