# Importando Módulo
from menus.cleanMenu import clear
import menus.startMenu as inicio

# Menu de Criação de listas
def listCreation():
    msg_menu = f'{5*"="} Menu de Criação de Listas {5*"="}'
    print(msg_menu)
    print('[1] - Criar somente o nome da lista')
    print('[2] - Criar nome e adicionar item')
    print('[3] - Voltar ao menu inicial')
    print(len(msg_menu) * "=")
    
    # Capturando o valor de entrada do usuário
    create_op = input('Escolha sua opção (1, 2 ou 3): ')
    checkOptions(create_op)

# Verifica as opções digitadas do menu principal
def checkOptions(op):
    op = op.strip()  # elimina os espaços no começo e final da string
    if op == '1':
        clear()  # limpa a tela do terminal
        print('Você selecionou a opção de Criar somente o nome da lista\n')
        
    elif op == '2':
        clear()  # limpa a tela do terminal
        print('Você selecionou a opção de Criar nome e adicionar item\n')
        
    elif op == '3':
        clear()  # limpa a tela do terminal
        print('Você selecionou a opção de Voltar ao menu inicial\n')
        inicio.menu()  # Menu da terceira opção
        
    else:
        clear()
        print('Selecione uma das opções (1, 2 ou 3)\n')
        listCreation()  # Executando o menu para criar lista
