#include <stdio.h>
#include <stdlib.h>

int main()
{
    int binaryNum[32];
    int liczba;
    int nbit;
    printf("Podaj liczbe dziesietna: ");
    scanf("%d", &liczba);
    // Zmienna do przechowywania d³ugoœci liczby binarnej
    int i = 0;
    while (liczba > 0) {
        // Zapisywanie reszt z dzielenia przez 2
        binaryNum[i] = liczba % 2;
        liczba = liczba / 2;
        i++;
    }

    // Wyœwietlanie liczby binarnej od ty³u
    printf("Liczba binarna: ");
    for (int j = i - 1; j >= 0; j--)
        printf("%d", binaryNum[j]);
    printf("\nPodaj liczbe bitu: ");
    scanf("%d", &nbit);
    if(nbit < 0 || nbit > sizeof(binaryNum))
        printf("Bledny numer bitu");
    else
        printf("%d", binaryNum[nbit]);


    return 0;
}
