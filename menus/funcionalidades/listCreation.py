from menus import startMenu

# Variáveis
list_dict = {}
items_list = []


# Função para criar a lista
def create():
    key = input('Digite o nome da lista: ').strip().capitalize()

    print('\nDigite todos os itens da lista separados por vírgula')
    print('Exemplo: Item 1, Item 2, Item 3\n')

    # Deixando cada item digitado com a primeira letra maiúscula
    items = input('Digite os itens: ').title()

    # Adicionando na lista todos os itens separados por vírgula
    items_list = items.split(',')

    while True:
        add_more_item = input(
            'Deseja adicionar mais item? [s]im ou [n]ão: ').strip().lower()

        if add_more_item == 's':
            item = input('Digite o nome do item: ').strip()
            items_list.append(item)
        elif add_more_item == 'n':
            list_dict[key] = items_list
            startMenu.menu()
            break
        else:
            print('Verifique a opção digitada e tente novamente!\n')
            continue
