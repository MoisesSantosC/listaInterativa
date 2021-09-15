# Menu de Visualização de lista
def listView():
    msg_menu = f'{5 * "="} Menu de Visualização de lista {5 * "="}'
    
    print(msg_menu)
    print('[1] - Ver todas as listas')
    print('[2] - Editar listas')
    print('[3] - Pesquisar lista')
    print('[4] - Voltar ao menu inicial')
    print(len(msg_menu) * "=")
    
    # Capturando o valor de entrada do usuário
    view_op = input('Escolha sua opção (1, 2, 3 ou 4): ')
