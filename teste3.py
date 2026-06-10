usuarios = []


def cadastrar():
    print("\n--- CADASTRO ---")

    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    for u in usuarios:
        if u[0] == usuario:
            print("Usuário já cadastrado!")
            return

    usuarios.append([usuario, senha])

    print("Usuário cadastrado com sucesso!")

def cadastrarPet():
    print("\n--- CADASTRO ---")

    Pet = input("Digite o Nome do Pet ")
    PetIdade = input("Digite a Idade do Pet: ")
    PetTipo = input("Digite o Tipo de Pet: ")

    print("Usuário cadastrado com sucesso!"


def login():
    print("\n--- LOGIN ---")

    while True:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        encontrado = False

        for u in usuarios:
            if u[0] == usuario and u[1] == senha:
                encontrado = True
                break

        if encontrado:
            print(f"Bem-vindo, {usuario}!")
            menuLogado()
            break
        else:
            print("Usuário não encontrado ou senha incorreta!")
            print("Tente novamente.\n")


def menu():
    while True:
        print("\n---- MENU ----")
        print("1 - Login")
        print("2 - Cadastrar")
        print("3 - Cadastrar Pet")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            login()

        elif opcao == "2":
            cadastrar()

        elif opcao == "4":
            cadastrarPet()

        elif opcao == "4":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida!")

