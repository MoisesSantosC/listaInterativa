from menus.funcionalidades.listCreation import list_dict
from menus.funcionalidades import backToMenu


def view():
    if not list_dict == {}:
        print('Selecione a lista pelo nome\n')
        print('SUAS LISTAS')

        # Mostrando os nomes das listas
        for indice, valor in enumerate(list_dict):
            print(f'[{indice + 1}] - {valor}')

        # Entrada do usuário para selecionar a lista
        select = input('\nNome da lista: ')

        # Visualizando os itens da lista selecionada
        for indice, valor in enumerate(list_dict[select]):
            print(valor.strip())

    else:
        print('Nenhuma lista foi criada ainda!\n')
        backToMenu.back()
