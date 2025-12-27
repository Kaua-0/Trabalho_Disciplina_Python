# -----------------------------------------
# SISTEMA DE CONTROLE DA FORTALEZATECH
# Trabalho final da disciplina do curso de Computational Logic Using Python
# -----------------------------------------

produtos = []

def adicionar_produto():
    print("\n=== Informe o nome do Produto ===")
    nome = input("Nome do produto: ").strip()


    for p in produtos:
        if p["nome"].lower() == nome.lower():
            print("Produto já cadastrado!")
            return
    
    try:
        preco = float(input("informe o preço do produto: "))
        quantidade = int(input("Quantidade em estoque: "))
    except ValueError:
        print("Valores inválidos! Tente novamente.")
        return

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)
    print("Produto adicionado com sucesso!")


def atualizar_produto():
    print("\n=== Atualizar Produto ===")
    nome = input("Nome do produto que você quer atualizar: ").strip()

    for p in produtos:
        if p["nome"].lower() == nome.lower():
            try:
                novo_preco = float(input("Novo preço: "))
                nova_quantidade = int(input("Nova quantidade: "))
            except ValueError:
                print("Valores inválidos!")
                return

            p["preco"] = novo_preco
            p["quantidade"] = nova_quantidade
            print("Produto atualizado com sucesso!")
            return

    print("Produto não encontrado!")


def excluir_produto():
    print("\n=== Excluir Produto ===")
    nome = input("Nome do produto você quer excluir: ").strip()

    for p in produtos:
        if p["nome"].lower() == nome.lower():
            produtos.remove(p)
            print("Produto removido com sucesso!")
            return
    
    print("Produto não encontrado!")


def visualizar_estoque():
    print("\n=== Estoque atual da Filial Fortaleza ===")

    if not produtos:
        print("Estoque da filial vazio!")
        return

    for p in produtos:
        print(f"\nProduto: {p['nome']}")
        print(f"Preço: R$ {p['preco']:.2f}")
        print(f"Quantidade: {p['quantidade']}")

def menu():
    while True:
        print("\n==============================")
        print("   SISTEMA DE CONTROLE DE ESTOQUE DA FORTALEZATECH")
        print("==============================")
        print("1 - Adicionar produto")
        print("2 - Atualizar produto")
        print("3 - Excluir produto")
        print("4 - Visualizar estoque")
        print("5 - Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            atualizar_produto()
        elif opcao == "3":
            excluir_produto()
        elif opcao == "4":
            visualizar_estoque()
        elif opcao == "5":
            print("Saindo do sistema de controle de estoque..")
            break
        else:
            print("Opção inválida! Tente novamente.")


menu()