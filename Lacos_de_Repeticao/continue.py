numero = 0

while True:
    if numero == 10:
        break # sai do loop
    numero = numero + 1
    if numero % 2 == 0:
        print(numero , "é PAR")
        continue #é o contrario do break, ele volta pro loop, RECOMEÇA ELE
    print(numero ,"é IMPAR")
