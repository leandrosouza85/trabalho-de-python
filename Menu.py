def menusecundario():
    opcao = -1
    while opcao != 0:
        print("="*60)
        print('LOGADO')
        print("="*60)
        print()
        print('1 - MOSTRAR USUARIOS CADASTRADOS')
        print('2 - MOSTRAR USUARIO LOGADO')
        print('3 - DELETAR USUARIO LOGADO')
        print('4 - DELETAR TODOS USUARIOS CADASTRADOS')
        print('0 - VOLTAR MENU PRINCIPAL')
        print()
        opcao = int(input('DIGITE A OPÇÃO DESEJADA: '))
        print()
        print("="*60)
        if (opcao == 1):
            mostrarUsuarioCadastrados()
        elif (opcao == 2):
            mostrarUsuarioLOgado()
        elif (opcao == 3):
            deletarUsuarioLogado()
        elif (opcao == 4):
            deletarTodosUsuarios()
        elif (opcao != 0):
            print('\n{0} OPÇÃO INVALIDA'.format(opcao))

        print()
    print('ENCERRANDO......')


def menuprincipal():
    opcao = -1
    while opcao != 0:
        print("="*60)
        print('MENU PRINCIPAL')
        print("="*60)
        print()
        print('1 - CADASTRAR USUARIO)')
        print('2 - LOGIN')
        print('0 - SAIR')
        print()
        opcao = int(input('DIGITE A OPÇÃO DESEJADA: '))
        print()
        print("="*60)
        if (opcao == 1):
            cadastrarUsuario()
        elif (opcao == 2):
            login()
        elif (opcao != 0):
            print('\n{0} OPÇÃO INVALIDA'.format(opcao))
        print("="*60)
        print()
    print('ENCERRANDO......')

def main ():
    menuprincipal()
    
main()
