l = []
l.append(4)
l.append(1)
l.append(7)
l.append(5)
d = len(l)
print(l)
print(d)


a = 6


if a % 2 == 0 or a > 18:
    print('duza liczba parzysta')
elif a % 2 == 0 and a <= 18:
    print('mala liczba parzysta')
else:
    print('liczba nieparzysta')

l = [6, 9, 4, 8, 10, 7, 13, 17]

for element in l:
    if element % 2 != 0:
         print(element ** 2)
print("--------")
def foo():
    return 4

print(foo())

def foo(x, y):
    if x > y:
        print('wieksze jest x')
    elif y > x:
        print('wieksze jest y')
    else:
        print('obie liczby sa rowne')

foo(5,4)