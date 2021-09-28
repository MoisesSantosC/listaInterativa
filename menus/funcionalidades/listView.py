from menus.funcionalidades.listCreation import list_dict

def view():
    print('Selecione a lista pelo nome\n')
    
    print('SUAS LISTAS')
    print(' N° | NOME DA LISTA')
    
    # Contador de listas criadas
    count = 0
    
    # Mostrando os nomes das listas
    for key in list_dict:
        count += 1
        print(f'[{count}] {key.title()}')
    
    # Entrada do usuário para selecionar a lista
    select = input('\nNome da lista: ')

    # Visualizando os itens da lista selecionada
    if select in list_dict:
        print(list_dict[select])