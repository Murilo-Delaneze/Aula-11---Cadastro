elif opcao == "2":
        print("\n--- USUÁRIOS CADASTRADOS ---")
        if not base_de_dados:
            print("Nenhum usuário cadastrado ainda.")
        for u in base_de_dados:
            print(f"Nome: {u['nome']} | Idade: {u['idade']}")