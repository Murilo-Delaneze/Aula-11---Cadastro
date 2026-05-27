banco_de_dados = []

def cadastrar_usuario(nome, idade):
    novo_usuario = {
        "nome": nome,
        "idade": idade,
    }
    banco_de_dados.append(novo_usuario)
    print(f"\n {nome} cadastrado com sucesso!\n")

# Loop principal de interação
while True:
    print("--- MENU DE CADASTRO ---")
    print("1. Cadastrar novo usuário")
    print("2. Sair")
    
    opcao = input("Escolha uma opção (1/2): ")

    if opcao == "1":
        # Coleta os dados do usuário pelo teclado
        nome_input = input("Digite o nome: ")
        idade_input = input("Digite a idade: ")
        
        # Envia os dados para a função
        cadastrar_usuario(nome_input, idade_input)
        
    elif opcao == "2":
        print("Saindo do sistema... Até logo!")
        exit()
    else:
        print("\n Opção inválida! Tente novamente.\n")