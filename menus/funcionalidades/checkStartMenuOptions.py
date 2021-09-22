# Importando Módulos
from menus.funcionalidades.cleanMenu import clear
from menus.programExitMenu import programExit
import menus.startMenu as home
from menus.funcionalidades import listCreation


# Verifica as opções digitadas do menu principal
def checkMenuOptions(op):
    op = op.strip()  # elimina os espaços no começo e final da string
    if op == '1':
        clear()  # limpa a tela do terminal
        print('Você selecionou a opção de Criar uma Lista\n')
        listCreation.create()        
        
    elif op == '2':
        clear()  # limpa a tela do terminal
        print('Você selecionou a opção de Ver Listas\n')
        
    elif op == '3':
        clear()  # limpa a tela do terminal
        print('Você selecionou a opção de Sair\n')
        programExit()  # Menu da terceira opção
        
    else:
        print('Selecione uma das opções (1, 2 ou 3)\n')
        home.menu()  # Executando o menu
