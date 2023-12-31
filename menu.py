from Usuario import Usuario

# Leitura de banco de dados de um arquivo .txt das contas de usuario e seu historico
# essa leitura deve fornecer um dicionarío com email: objeto usuario
# preencher o dicionario resositorioUsuario

repositorioUsuario = {}
zezinExemploUsuario = Usuario("zezin@gmail.com","senhaZezin", "Zezin", "masculino",56, 66,165,"ganhar","sedentario")

repositorioUsuario["zezin@gmail.com"] = zezinExemploUsuario

def menuInicial():
    print("Bem vindo!")
    print("O que deseja fazer:\n 1-Login \n2-Cadastrar-se")
    opcao = input("Digite a opção 1, 2 ou enter para sair do programa:")

    if opcao == "1":
        return menuLogin()
    elif opcao == "2":
        return menuCadastrar()
    elif opcao == "":
        return
    else:
        menuInicial()

def menuLogin():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    # verificar se o email esta cadastrado
    if email in repositorioUsuario:
        # validar senha
        usuario = repositorioUsuario[email]
        if usuario.getSenha() == senha:
            print("logado")
            menuUsuario(usuario)

    # acessar menuUsuario passando as informações do usuário
    pass


def menuCadastrar():
    # recebe os dados necessário para o cadastro e válida essas entradas, caso alguma entrada nao seja valida pede novamente. Nao cadastra com entrada invalida.
    print("menuCadastrar")
    pass

def menuUsuario(usuario):

    # apresenta dados como nome e meta diária da dieta (água, carboidrato, gordura, proteína)
    print("menuUsuario")
    pass

# programa rodando

menuInicial()