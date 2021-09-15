# Importando os Módulos
from menus.funcionalidades.cleanMenu import clear
from menus.funcionalidades.checkStartMenuOptions import checkMenuOptions

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
