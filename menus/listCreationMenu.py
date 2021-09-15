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
