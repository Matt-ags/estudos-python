"""
Desafio: A Lista de Compras

Imagine que um cliente contrata você para criar uma aplicação de lista de compras simples.
Essa lista deverá ter uma série de funcionalidades que precisam ser implementadas e que, ao final,
deverá permitir que o usuário manipule os produtos na lista.
Portanto, você precisará elencar o que será necessário para que a lista seja implementada,
de acordo com as necessidades do cliente, utilizando seus conhecimentos em programação e implementá-las utilizando Python.

Para realizar este desafio você precisar ter noção dos seguintes conceitos:

Laços de repetição;
Condicionais;
Entrada e saída de dados;
Manipulação de listas, dicionários e strings;

Objetivo do desafio:
Desenvolver um aplicativo que gerencie uma lista de compras que permita adicionar, remover e listar os produtos adicionados nela.

Para isso, o seu aplicativo precisa ter as seguintes funcionalidades:

Menu de Opções:

O sistema deve fornecer um menu de opções para o usuário interagir.
As opções devem ser as seguintes:

Adicionar produto
Remover produto
Pesquisar produtos
Sair do programa

Adicionar Produto:
O usuário deve poder adicionar um novo produto à lista de compras.
O sistema deve solicitar informações sobre o nome, unidade de medida, quantidade e descrição do produto.

As opções de unidade devem ser:

Quilograma
Grama
Litro
Mililitro
Unidade
Metro
Centímetro

Essas opções devem aparecer quando o sistema perguntar a unidade de medida.

Controle de ID Automático:
O sistema deve atribuir automaticamente um ID único para cada produto adicionado à lista.

Remover Produto: O usuário deve poder remover um produto da lista com base ID do produto.
O sistema deve solicitar o ID do produto que o usuário deseja remover.

Pesquisar Produtos por Nome: O usuário deve poder pesquisar produtos na lista com base no nome ou parte do nome.
O sistema deve exibir os resultados correspondentes e fornecer a contagem total de produtos encontrados.

Listar Todos os Produtos: O sistema deve ser capaz de exibir todos os produtos presentes na lista de compras, se houver.
Contudo, o menu não deve mostrar uma opção de “Listar produtos”.
A exibição deverá ocorrer toda vez que o menu principal for executado,
acima dele.

Cabeçalho do Aplicativo: Deve ser exibido um cabeçalho ao iniciar o aplicativo para fornecer uma saudação e indicar
que é uma Lista de Compras Simples.

Feedback de Ação: Após a execução de uma ação (como adicionar ou remover um produto), o sistema deve fornecer feedback
indicando o resultado da ação.

Tratamento de Entradas Inválidas: O sistema deve ser capaz de lidar com entradas inválidas do usuário e fornecer
mensagens de erro apropriadas para orientar o usuário.

Encerramento do Programa: O usuário deve poder encerrar o programa de forma adequada, escolhendo a opção de saída no menu.
"""

def lista():
    lista = [] # Importante deixar fora do loop, para que não de reset e tira os itens
    id_produto = 1
    while True:

        print("Lista de Compras Simples")
        print()
        print("Seja bem-vindo(a), esta é uma lista de compras simples. Abaixo você encontra a sua lista atual:")
        print()
        print("////////")
        if len(lista) == 0:
            print("Opa, parece que sua lista está vazia! Digite 1 para começar a adicionar.")
        else:
            # Pelo que eu vi, para deixar mensagens bonitinhas com o dicionario, tem que usar o f-string, só deixar o f na frente:
            for item in lista: # É meio confuso esta relção do for e in, mas tente lembrar da função "f(x)" que só estamos dando nomes pro x e pro y
                print(f"ID: {item['id']} | Item: {item['nome']}, Quantidade: {item['quantidade']} {item['unidade']}, Descrição: {item['descricao']};")

        print("////////")
        print()
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Pesquisar produtos")
        print("s - Sair do programa")
        acao = input("Selecione uma opção ou digite 's' para sair: ")

        if acao == 's' or acao == 'S':
            print("Obrigado por utilizar a Lista de Compras Simples!")
            break # Break é o que faz sair do loop

        if acao not in ['1', '2', '3']:
            print("Opção inválida! Tente novamente.")
            continue # volta o loop

        # ADICIONAR PRODUTO:
        if acao == '1':
            # para realizar aquelas outras informaçoes, que levam ao mesmo produto, são "dicionarios", mesma coisa que "objetos" em javascript
            nome = input("Digite o nome do produto: ")

            while True:
                # Uma dica: Tem menu? Temos loop!
                print("1 - Quilograma(s)")
                print("2 - Grama(s)")
                print("3 - Litro(s)")
                print("4 - Mililitro(s)")
                print("5 - Unidade(s)")
                print("6 - Metro(s)")
                print("7 - Centímetro(s)")

                unidade = (input("Qual a unidade de medida? (Digite o número correspondente): "))

                if unidade == '1': # Deixei em aspas pois a unidade vem como string, podiamos transformar em número, mas pra facilitar, deixei desta forma
                    unidade = "Quilograma(s)"
                    break
                elif unidade == '2':
                    unidade = "Grama(s)"
                    break
                elif unidade == '3':
                    unidade = "Litro(s)"
                    break
                elif unidade == '4':
                    unidade = "Mililitro(s)"
                    break
                elif unidade == '5':
                    unidade = "Unidade(s)"
                    break
                elif unidade == '6':
                    unidade = "Metro(s)"
                    break
                elif unidade == '7':
                    unidade = "Centímetro(s)"
                    break
                else:
                    print("Opção inválida! Tente novamente.")
                    continue  # volta o loop

            quantidade = input("Digite a quantidade: ")
            descricao = input("Digite uma descrição para o produto: ")

            produto = { # dicionario do produto:
                "id": id_produto,
                "nome": nome,
                "unidade": unidade,
                "quantidade": quantidade,
                "descricao": descricao
            }
            lista.append(produto)
            print(produto, " adicionado!")
            print(lista) # Tirar depois, é para listar os produtos na lista, tem os objetros na lista

            id_produto = id_produto + 1

        # REMOVER PRODUTO:
        if acao == '2':
            while True:
                print()
                print("////////")
                if len(lista) == 0:
                    print("Opa, parece que sua lista está vazia! Digite 1 para começar a adicionar.")
                    break
                else:
                    # Pelo que eu vi, para deixar mensagens bonitinhas com o dicionario, tem que usar o f-string, só deixar o f na frente:
                    for item in lista:  # É meio confuso esta relção do for e in, mas tente lembrar da função "f(x)" que só estamos dando nomes pro x e pro y
                        print(f"ID: {item['id']} | Item: {item['nome']}, Quantidade: {item['quantidade']} {item['unidade']}, Descrição: {item['descricao']};")

                print("////////")
                print()

                id_do_produto_removido = (input("Qual produto deseja remover? (Digite o ID correspondente): "))

                produto_encontrado = False
                for item in lista:
                    if str(item['id']) == id_do_produto_removido: # Esse str é para transformar o id em String, pq de alguma forma ele transforma em número aqui!
                        lista.remove(item)
                        print(f"Produto {item['nome']} removido com sucesso!")
                        produto_encontrado = True
                        break

                if not produto_encontrado:
                    print("Produto não encontrado! Tente novamente.")
                    continue

                break




lista()