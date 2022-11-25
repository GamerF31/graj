tab1 = []
player = " P "
jablko = " o "

for i in range(25):
    tab1.append(' . ')

def plansza():

    for i in range(25):
        print(tab1[i], end="")
        if i in [4, 9, 14, 19]:
            print('\n')
    print('\n')

def Ruch():
    if x == "d":
        tab1.remove(player)
        tab1.insert(prev_pos + 1, player)

    elif x == "s":

        if player in tab1[20:25]:
            pass
        else:
            tab1.remove(player)
            tab1.insert(prev_pos + 5, player)

    elif x == "w":

        if player in tab1[0:5]:
            pass

        else:
            tab1.remove(player)
            tab1.insert(prev_pos - 5, player)

    elif x == "a":
        if player in tab1[0] or tab1[5] or tab1[10] or tab1[15] or tab1[20]:
            pass
        else:
            tab1.remove(player)
            tab1.insert(prev_pos - 1, player)

    if player in tab1[24]:
        tab1.remove(jablko)
tab1.insert(0,player)
tab1.insert(24,jablko)
plansza()
while jablko in tab1:
    x = input("Wybierz kierunek ruchu (W,A,S,D): ").lower()
    pos = tab1.index(player)
    prev_pos = pos
    Ruch()
    print('\n')
    plansza()
print("You won!")















