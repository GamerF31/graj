lista = [i for i in range(1,11)]
print(lista)
listab = [x for x in range(0,21,2)]
print(listab)
listac = [x*x for x in range(1,10)]
print(listac)
listad = [x*0 for x in range(1,10)]
print(listad)
listae = [1 if x%2==0 else 0 for x in range(1,10)]
print(listae)
listaf=[x%5 for x in range(0,10)]
print(listaf)
print("-----------------")

lista2 = []
i = 1
while i<11:
    lista2.append(i)
    i+=1

print(lista2)
lista2b = []
i = 0
while i < 21:
    lista2b.append(i)
    i = i + 2
print(lista2b)
lista2c = []
i = 1
while i < 11:
    lista2c.append(i*i)
    i+=1
print(lista2c)

lista2d = []
i = 1
while i < 11:
    lista2d.append(i*0)
    i+=1
print(lista2d)
lista2e = []
i = 0
while i < 10:
    if i%2==0:
        lista2e.append(i*0)
    else:
        lista2e.append(1)
    i+=1
print(lista2e)
lista2f = []
i = 0
while i < 10:
    lista2f.append(i%5)
    i+=1
print(lista2f)

def ile_ujemnych(lista):
    lista = [1,2,3,4,-12,-4]
    suma = 0
    for x in range(0,len(lista)):
        if lista[x]<0:
            suma+=1
    return suma
print(ile_ujemnych(lista))

def iloczyn(lista):
    lista = [1,2,3,4,-12,-4]
    ilo = 1
    for x in range(len(lista)):

        ilo=ilo*lista[x]
    return ilo
print(iloczyn(lista))

def minmax(lista):
    lista = [1, 2, 3, 4, -12, -4]
    for x in range(len(lista)):

        y=min(lista)
        z=max(lista)
        krotka=(y,z)
    return krotka
print(minmax(lista))

def przemienna(list):
    suma = 0
    sign = 1
    lista = [1,4,16,9,9,7,4,9,11]
    for x in lista:
        suma+= x*sign
        sign = -sign
    return suma
print(przemienna(lista))

def wyswietl(lista):
    lista = []
    i=0
    while i<10:
        x = input()
        while x in lista:
            print("podana wartosc jest z psa")
            x = input()
        lista.append(x)
        i+=1

    return lista
print(wyswietl(lista))



