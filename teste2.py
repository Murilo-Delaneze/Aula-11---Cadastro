banco_de_dados = []
cachorros = []

def cadastrar_pet(nome, idade, raca, situacao ):
    novo_pet = {
        "nome": nome,
        "idade": idade,
        "raca": raca,
        "situacao": situacao,
    }
    banco_de_dados.append(novo_pet)
    print(f"\n {nome} cadastrado com sucesso!\n")

# Loop principal de interação
while True:
    print("--- MENU DE CADASTRO ---")
    print("1. Cadastrar novo pet")
    print("2. Sair")
    
    opcao = input("Escolha uma opção (1/2): ")

    if opcao == "1":
        # Coleta os dados do usuário pelo teclado
        for i in cachorros:
            nome_input = input("Digite o nome: ")
            cachorros.append(nome_input)
        # Socorro
        idade_input = int(input("Digite a idade: "))
        raca_input = input ("Digite a raça de seu animal: ")
        situacao_input= input("Digite qual o estado que se animal está: ")
        
        # Envia os dados para a função
        cadastrar_pet(nome_input, idade_input, raca_input, situacao_input)
        
    elif opcao == "2":
        print("Saindo do sistema... Até logo!")
        exit()
    else:
        print("\n Opção inválida! Tente novamente.\n")
        