"""

Projeto guiado: Calculadora

Nível de dificuldade: Fácil

Requisitos Técnicos: Laços de repetição, condicionais, entrada e saída de dados, operações matemáticas, coleções de dados.

Descrição Geral:

Desenvolver um aplicativo de calculadora que funcione via linha de comando (terminal).
O usuário deve ser capaz de escolher entre diferentes operações matemáticas, inserir números para realizar os cálculos,
e navegar no menu do aplicativo.

Requisitos Funcionais:

    Menu Principal:
    Ao iniciar, o aplicativo deve exibir um menu principal com as seguintes opções:

        1 - Soma
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
        s - Sair

    O usuário escolhe uma operação digitando o número correspondente.

    Se o usuário digitar "s", o aplicativo deve exibir uma mensagem de agradecimento e encerrar.

    Execução da Operação:

        Após escolher uma operação, o usuário deve ser solicitado a inserir dois números, um por vez,
        pressionando "Enter" após cada um.
        O aplicativo calcula e exibe o resultado da operação escolhida com os números fornecidos.

Dica: tome cuidado com divisões por zero!

Após exibir o resultado, o aplicativo retorna automaticamente ao menu principal.

"""

# vamos definir a função principal:

def calculadora(): # na descrição, pede que executou, volta pro menu, ou seja, é tipo uma coisa infinita -> loop!
    while True:
        print("Calculadora Simples")
        print()
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("s - Sair")
        operacao = input("Selecione uma opção ou digite 's' para sair:") # Definindo um norte para dar inicio, uma pergunta para o usuário

        # Definindo a ação de sair:
        if operacao == 's' or operacao == 'S':
            print("Obrigado por utilizar a Calculadora Simples!")
            break # Break é o que faz sair do loop

        # definindo operações do menu:
        # Percebe que temos uma lista de opção, 1, 2, 3, 4 e s, ou seja, uma lista. Caso o usuário não digitar algo desta lista, temos um erro, certo?

        if operacao not in ['1', '2', '3', '4']:
            print("Opção inválida! Tente novamente.")
            continue # volta o loop

        # Certo, agora, para termos as operações, percisamos de numeros!

        numero_1 = float(input("Primeiro Número:")) # Convertemos string para numero, o float é pq queremos numeros quebrados
        numero_2 = float(input("Segundo Número:"))

        # SOMA
        if operacao == '1':
            resultado = numero_1 + numero_2
            print("O resultado da soma entre ",numero_1," e ",numero_2," é: ", resultado)

        # SUBTRAÇÃO
        elif operacao == '2':
            resultado = numero_1 - numero_2
            print("O resultado da subtração entre ",numero_1," e ",numero_2," é: ", resultado)

        # MULTIPLICAÇÃO
        elif operacao == '3':
            resultado = numero_1 * numero_2
            print("O resultado da multiplicação entre ",numero_1," e ",numero_2," é: ", resultado)

        # DIVISÃO
        else:
            if numero_2 == 0: # LEMBRA: ele transformou o input em numero, aqui, não coloque como texto, ou seja, entre aspas, mas o numero em si!
                print("Divisões por '0' não são possiveis, tente novamente.")
                continue
            else:
                resultado = numero_1 / numero_2
                print("O resultado da divisão entre ",numero_1," e ",numero_2," é: ", resultado)

# Agora, vamos chamar a função:

calculadora()
