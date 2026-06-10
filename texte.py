import os
import platform
banco_de_dados = []
banco_de_dados_animal = []

def limpar_tela():
    # Se for Windows
    if platform.system() == "Windows":
        os.system('cls')
    # Se for Linux ou macOS
    else:
        os.system('clear')

def cadastrar_usuario(nome, idade, email, senha):
    novo_usuario = {
        "nome": nome,
        "idade": idade,
        "email": email,
        "senha": senha
    }
    banco_de_dados.append(novo_usuario)
    print(f"\n {nome} cadastrado com sucesso!\n")

def excluir_usuario(nome, idade):
    for usuario in banco_de_dados:
        if usuario["nome"] == nome and usuario["idade"] == idade:
            banco_de_dados.remove(usuario)
            print(f"Usuário {nome} excluído com sucesso!")
            return

    print(f"Erro: Usuário {nome} não foi encontrado.")

def cadastrar_animal(nome_animal, idade_animal, raca):
    novo_animal = {
        "nome":nome_animal,
        "idade":idade_animal,
        "raça":raca
    }
    banco_de_dados_animal.append(novo_animal)
    print(f"\n {nome_animal} cadastrado com sucesso!\n")

def login():
    usuario = input('Digite o usuario(Email): ')
    senha = input('Senha: ')

    for u in banco_de_dados:
        if u['email'] == usuario and u['senha'] == senha:

            limpar_tela()
            print('Login realizado com sucesso')
            login_realizado()
        else:
            limpar_tela()
            print('User ou senha incorreto')
            

def login_realizado():
    print('----Tela de Login----')
    print('1. Cadastrar novo animal ')
    print('2. Lista de Animais Cadastrados ')
    print('3. Lista de Usuários Cadastrados ')
    print('4. Excluir Usuário ')
    print("0. Sair")

    opcao_login = input("Escolha uma opção (0/1/2/3/4): ")

    if opcao_login == "1":
        limpar_tela()
        nome_animal = input("Digite o nome do animal: ")
        idade_animal = input("Digite a idade do animal: ")
        raca_animal = input("Digite a raça do animal(Qual animal e Raça): ")
        
        limpar_tela()
        cadastrar_animal(nome_animal, idade_animal, raca_animal)
        login_realizado()

    elif opcao_login == "2":
        limpar_tela()
        print("\n--- Animais CADASTRADOS ---")
        if not banco_de_dados_animal:

            print("Nenhum Animal cadastrado ainda.")
        for u in banco_de_dados_animal:
            print(f"Nome: {u["nome"]} | Idade: {u["idade"]} | Raça: {u["raça"]} ")
        login_realizado()

    elif opcao_login == "3":
        limpar_tela()
        print("\n--- USUÁRIOS CADASTRADOS ---")
        if not banco_de_dados:
            print("Nenhum usuário cadastrado ainda.")
        for u in banco_de_dados:
            print(f"Nome: {u['nome']} | Idade: {u['idade']}")
        login_realizado()

    elif opcao_login == "4":
        
        nome = input("Digite o nome que deseja excluir: ")
        idade = input("Digite a idade do usuário: ")

        excluir_usuario(nome, idade)
        limpar_tela
        login_realizado()

    elif opcao_login == "0":
    
        print("Saindo do sistema... Até logo!")
        limpar_tela()
        exit()
    else:
        print("\n Opção inválida! Tente novamente.\n")

while True:
    limpar_tela()
    print("--- MENU DE CADASTRO ---")
    print("1. Cadastrar novo usuário")
    print('2. Fazer Login ')
    print("0. Sair")
    
    opcao = input("Escolha uma opção (0/1/2): ")

    if opcao == "1":
        limpar_tela()
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        email = input('Digite seu email: ')
        senha = input('Digite sua senha: ')
        
        cadastrar_usuario(nome, idade, email, senha)

    elif opcao == "2":
        limpar_tela()
        login()

    elif opcao == "0":
        print("Saindo do sistema... Até logo!")
        limpar_tela()
        exit()
    else:
        print("\n Opção inválida! Tente novamente.\n")