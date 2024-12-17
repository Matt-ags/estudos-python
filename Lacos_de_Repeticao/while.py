# while -> enquanto -> enquanto uma afirmação for verdadeira, faz tal coisa.

numero = 0

# while numero < 10:
#     print("Número:", numero)
#     numero = numero + 1

# Para fazer um loop infinito, podemos só colocar o "True"

while True:
    print("Número:", numero)
    numero = numero + 1
    if numero == 10:
        print("Fim:", numero)
        break # sai do loop

        # Uma coisa que é chatinha, tem que deixar bem aninhado, pois trocando a posição, ja da erro

# No pycharm, temos a ferramenta de debug, que fica ao lado do botão de executar, serve para encontrarmos erros
# <- aqui ao lado, ao passar o mouse em cima, podemos clicar em uma bolinha vermelha, que ao clicar, marca, que serve como orientador ao debuger,
# tipo assim: "Ei mano, para de debugar aqui beleza?"
# Ele da tipo um pause, e apertando a tecla "F8", VAI EXECUTANDO LINHA POR LINHA, INTERESSANTE. "F9" DA TIPO UM SALTO