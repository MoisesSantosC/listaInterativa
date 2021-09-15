from menus import startMenu

# Variáveis
list_dict = {}
items_list = []

# Função para criar a lista
def create():
    key = input('Digite o nome da lista: ').strip().capitalize()
    while True:
        item = input('Digite o nome do item: ')
        add_more_item = input('Deseja adicionar mais item? [s]im ou [n]ão: ').strip().lower()
        
        if add_more_item == 's':
            items_list.append(item)
        else:
            items_list.append(item)
            list_dict[key] = items_list
            
            startMenu.menu()
            break
