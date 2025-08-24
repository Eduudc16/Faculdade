def menu():
    print("\nAGENDA TELEFÔNICA")
    print("1 - Incluir contato")
    print("2 - Alterar contato")
    print("3 - Excluir contato")
    print("4 - Listar contatos")
    print("5 - Sair")
    return input("Escolha uma opção: ")

agenda = {}  

while True:
    opcao = menu()

   
    if opcao == "1":
        nome = input("Digite o nome: ").strip()
        telefone = input("Digite o telefone: ").strip()

        if nome == "" or telefone == "":
            print(" Erro: Nome e telefone não podem estar vazios.")
        elif telefone in agenda:
            print(" Erro: Telefone já cadastrado na agenda.")
        else:
            agenda[telefone] = nome
            print(" Contato adicionado com sucesso!")

  
    elif opcao == "2":
        telefone = input("Digite o telefone do contato a alterar: ").strip()
        if telefone in agenda:
            novo_nome = input("Digite o novo nome: ").strip()
            if novo_nome == "":
                print(" Erro: Nome não pode estar vazio.")
            else:
                agenda[telefone] = novo_nome
                print(" Contato alterado com sucesso!")
        else:
            print(" Erro: Telefone não encontrado na agenda.")

   
    elif opcao == "3":
        telefone = input("Digite o telefone do contato a excluir: ").strip()
        if telefone in agenda:
            del agenda[telefone]
            print(" Contato excluído com sucesso!")
        else:
            print(" Erro: Número de telefone não existente.")

   
    elif opcao == "4":
        if len(agenda) == 0:
            print(" Agenda vazia.")
        else:
            print("\n Lista de contatos:")
            for telefone, nome in agenda.items():
                print(f"Nome: {nome} | Telefone: {telefone}")

    elif opcao == "5":
        print(" Saindo da agenda...")
        break

    else:
        print(" Opção inválida. Tente novamente.")
