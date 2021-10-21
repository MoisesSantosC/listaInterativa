from menus.funcionalidades.listCreation import list_dict
from menus.funcionalidades import backToMenu


def view():
    if not list_dict == {}:
        print('SUAS LISTAS'.center(29))
        print(29 * '=')

        # Mostrando os nomes das listas
        for indice, valor in enumerate(list_dict):
            print(f'[{indice + 1}] - {valor}')

        print(29 * '=')

    else:
        msg = 'Nenhuma lista foi criada ainda!'

        print(f'{len(msg) * "="}')
        print(msg)
        print(f'{len(msg) * "="}')
        backToMenu.back()
