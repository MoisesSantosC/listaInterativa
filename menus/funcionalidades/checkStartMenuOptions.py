# Importando Módulos
from menus.funcionalidades.cleanMenu import clear
from menus.programExitMenu import programExit
import menus.startMenu as home
from menus.funcionalidades import listCreation
from menus.funcionalidades import listView


# Verifica as opções digitadas do menu principal
def checkMenuOptions(op):
    if op == '1':
        clear()  # limpa a tela do terminal
        listCreation.create()

    elif op == '2':
        clear()  # limpa a tela do terminal
        listView.view()

    elif op == '3':
        clear()  # limpa a tela do terminal
        programExit()

    else:
        print('Selecione uma das opções (1, 2 ou 3)\n')
        home.menu()  # Executando o menu
