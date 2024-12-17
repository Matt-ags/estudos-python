"""
    Vamos descrever uma pessoa e sua função:
    NOME: José
    FUNÇÃO: Carimbar contratos
    pega um contrato => carimba ele => devolve o contrato carimbado

    f(x) = 2x = y-> Função na matemática

    Uma forma de entrada, o que ele faz, e o resultado disso!
"""

# Como definimos uma função? com def

def multiplica(numero, multiplicador): # entrada
    resultado = numero * multiplicador # ação
    return resultado # devolve o valor

# observe que na função consigo ir chamando varios parametros

print(multiplica(3, 2)) # bem parecido com o f(x) da matemática, show!
print(multiplica(4, 3)) # bem parecido com o f(x) da matemática, show!
print(multiplica(5, 5)) # bem parecido com o f(x) da matemática, show!
print(multiplica(6, 2)) # bem parecido com o f(x) da matemática, show! (ctrl + d duplica linha)

def imprima(texto):
    print("O texto é", texto)

imprima("josé")

