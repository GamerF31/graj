samogloski = 'aeiouy'

def zlicz_spolgloski_iter(napis):
    wynik = 0
    for x in napis:
        if x.isalpha() and x.lower() not in samogloski:
            wynik = wynik + 1
    return wynik

def zlicz_spolgloski_rekur(napis):
    if len(napis) == 0:
        return 0
    if napis[0].isalpha() and napis[0].lower() not in samogloski:
        return 1 + zlicz_spolgloski_rekur(napis[1:])
    return zlicz_spolgloski_rekur(napis[1:])
lista = ['tunczyk','kapuś','xddddddddd']

for x in lista:
    print(zlicz_spolgloski_rekur(x))
    print(zlicz_spolgloski_iter(x))


