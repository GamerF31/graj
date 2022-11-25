class tab_ros_g:
    pojemnosc: int
    zajetosc: int
    dane: list[str]

    def __init__(self,dane=[None,None]):

        self.dane = dane
        self.zajetosc = 0
        self.pojemnosc=2


    def __str__(self):
        return str(self.dane)
    def ustal(self,idx:int,wartosc:any):
        if self.zajetosc<idx+1:
            self.zajetosc=idx+1

        while self.pojemnosc<self.zajetosc:
            self.pojemnosc *= 2

        for i in range(self.pojemnosc-len(self.dane)):
            self.dane.append(None)

        for i in range(self.zajetosc):
            if self.dane[i] is None:
                self.dane[i]=''
            self.dane[idx]=wartosc


    def pobierz(self,idx: int)->str:
        if idx>len(self.dane):
            return "puste"
        return self.dane[idx]
    def dodaj_za_koniec(self,wartosc: any):
        if self.zajetosc<self.pojemnosc:
            self.dane.insert(self.zajetosc,wartosc)
            self.dane.pop(-1)
            self.zajetosc+=1
        elif self.zajetosc==self.pojemnosc:
            self.pojemnosc*=2
            for i in range(self.pojemnosc - len(self.dane)-1):
                self.dane.append(None)
            self.dane.insert(self.zajetosc, wartosc)
            self.zajetosc+=1
    def wstaw_przed(self,idx:int,wartosc:any):
        if self.zajetosc<self.pojemnosc:
            self.dane.insert(idx,wartosc)
            self.dane.pop(-1)
            self.zajetosc+=1
        elif self.zajetosc==self.pojemnosc:
            self.pojemnosc*=2
            for i in range(self.pojemnosc - len(self.dane)-1):
                self.dane.append(None)
            self.dane.insert(idx, wartosc)
            self.zajetosc+=1
        for i in range(self.zajetosc):
            if self.dane[i] is None:
                self.dane[i]=''
                self.zajetosc+=1
    def uprosc(self):
        while self.pojemnosc/2>self.zajetosc:
            x = self.pojemnosc-self.pojemnosc/2
            for i in range(int(x)):
                self.dane.pop(-1)
            self.pojemnosc/=2
    def find_min_index(self, lst, start): # funkcja do znajdowania minimum
        i = start # pobieramy pierwszy element z listy
        for j in range(i + 1, len(lst)): # tworzymy pętle która zaczyna się od 2 elementu i leci do końca listy
            if lst[j] < lst[i]: # jeśli lst[j] czyli którykolwiek element z listy będzie większy od lst[i] czyli naszego startowego elementu
                i = j # to zamieniamy je ze sobą
        return i # tym sposobem zwrócimy tutaj index(czyli miejsce w liście) na którym jest najmniejsza wartość

    def sortuj(self):
        temp = [] # tworzymy sobie chwilową listę
        for i in range(len(self.dane)): # pętla która leci do końca zawartości naszej głównej tablicy
            if isinstance(self.dane[i], int): # tutaj sprawdzamy czy nasza wartość jest liczbą całkowitą
                temp.append(self.dane[i]) # jeśli jest liczbą całkowitą to wrzucamy do naszej listy tymczasowej
                self.dane[i] = '' # a to miejsce gdzie była ta liczba zamieniamy narazie na pusty ciąg

        for i in range(len(temp)): # teraz pętla która będzie nam przechodziła po naszej liście tymczasowej
            idx_of_minimum = self.find_min_index(temp, i) # tutaj szukamy właśnie tego minimalnego elementu i potrzebujemy jego indeksu
            temp[i], temp[idx_of_minimum] = temp[i], temp[idx_of_minimum] # i teraz w tym miejscu dokonujemy sortowania, zamieniamy caly czas elementy ze soba az posortujemy wszystko
            # aktualny element zamieniamy z minimalnym, a na miejsce minimalnego wstawiamy ten w ktorym byliśmy aktualny to temp[i], a minimalny który chcemy wstawić w jego miejsce to temp[idx_of_minimum]

        del self.dane[0:len(temp)] # tutaj usuwamy z naszej tablicy tyle elementów ile znajduje się w naszej tymczasowej tablicy,
                                    # bo wczesniej zamienilismy miejsca gdzie byly cyfry na puste ciagi, to teraz je musimy usunac
        self.dane = temp + self.dane # w tym miejscu dodajemy na poczatek naszej głownej tablicy, te tablice posortowaną tymczasową
        return self.dane # i zwracamy nasza głowna tablice

    def print(self):
        for i in range(len(self.dane)):
            if self.dane[i] is not None:
                if self.dane[i]=='':
                    print(';',end=' ')
                else:
                    print(f'{self.dane[i]}',end=' ')
tab = tab_ros_g([])
tab = tab_ros_g()
tab.ustal(2,-1)
tab.ustal(1,4)
#tab.dodaj_za_koniec(4)
#tab.dodaj_za_koniec(5)

print(tab.pojemnosc)
print(tab.zajetosc)
print("---------------")
tab.print()
print(tab)
print('\n')
tab.print()
print("\n---------------")
print("\nPrzed sortowaniem")
print(tab)
tab.sortuj()
print("\nPo sortowaniu")
print(tab)


