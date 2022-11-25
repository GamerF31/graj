i = 0
lista = []
while i < 10:
    x = input()
    while x in lista:
        print("podana wartosc jest juz na liscie")
        x = input()
    lista.append(x)
    i += 1
print(lista)