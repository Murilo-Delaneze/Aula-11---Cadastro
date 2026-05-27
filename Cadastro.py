banco_de_dados = []
banco_de_dados_animal = []

def cadastrar_usuario(nome, idade):
    novo_usuario = {
        "nome": nome,
        "idade": idade
    }
    banco_de_dados.append(novo_usuario)
    print(f"\n {nome} cadastrado com sucesso!\n")

def cadastrar_animal(nome_animal, idade_animal, raca):
    novo_animal = {
        "nome":nome_animal,
        "idade":idade_animal,
        "raça":raca
    }
    banco_de_dados_animal.append(novo_animal)
    print(f"\n {nome_animal} cadastrado com sucesso!\n")

while True:
    print("--- MENU DE CADASTRO ---")
    print("1. Cadastrar novo usuário")
    print('2. Cadastrar novo animal ')
    print("3. Sair")
    
    opcao = input("Escolha uma opção (1/2/3): ")

    if opcao == "1":
        # Coleta os dados do usuário pelo teclado
        nome = input("Digite o nome: ")
        idade = input("Digite a idade: ")
        
        # Envia os dados para a função
        cadastrar_usuario(nome, idade)

    elif opcao == "2":
        # Coleta os dados do usuário pelo teclado
        nome_animal = input("Digite o nome do animal: ")
        idade_animal = input("Digite a idade do animal: ")
        raca_animal = input("Digite a raça do animal: ")
        
        cadastrar_animal(nome_animal, idade_animal, raca_animal)
        
    elif opcao == "3":
        print("Saindo do sistema... Até logo!")
        exit()
    else:
        print("\n Opção inválida! Tente novamente.\n")