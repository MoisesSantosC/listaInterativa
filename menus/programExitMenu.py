# Menu de saída do programa
def programExit():
    msg_menu = '== Deseja realmente sair do programa? ==' 
    
    print(msg_menu)
    print('[1] - Sim')
    print('[2] - Não')
    print(len(msg_menu) * "=")
    
    # Capturando o valor de entrada do usuário
    quit_op = input('Escolha sua opção (1 ou 2): ')
