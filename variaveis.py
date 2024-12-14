# comentarios com "hashtag", daorinha

# como declarar uma variavel?

idade = 18

numero_pi = 3.14 # snake case
CONSTANTE = 2 # constante tudo maiusculo

# print(idade)

# tipos de dados:

# PRIMITIVOS
numero = 2 # inteiro, int
area = 2.5 # real, float
maior_de_idade = True # False or True (é com "t" maiusculo), booleano, bool
# (valor, endereço)

# COMPOSTOS

lista_de_numeros = [1, 2, 3]
lista_de_nomes = ["Mateus", "Jake"]
lista_de_floats = [1.23, 1.43, 3.4]

# de forma simples, é uma variavel que aponta para cada um dos valores, tipo um "grafico"

for numero in lista_de_numeros:
    print(numero)
    # cara, isso achei bizarro, tipo, ele reconhece o "numero" como se fosse um "endereço" para casa item na "lista de numeros"
    # e pode mudar para qualquer um (o codigo acima imprime os valor dentro do negócio)

# e o mais doido ainda:

pessoa = "José Do Frango"

for letra in pessoa:
    print(letra)
    # e sim, ele vai imprimir cada letra de pessoa.
    # pq é como uma lista, cada letra é uma posição na memória

