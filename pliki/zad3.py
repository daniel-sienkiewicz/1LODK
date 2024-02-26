# Zamiana liczby binarnej na dziesietna / dziesietnej na binarna

def decToBin(liczba):
    if not liczba:
        return 0

    wynik = ''

    while liczba:
        print(liczba)
        if liczba % 2:
            wynik += '1'
        else:
            wynik += '0'
        liczba //= 2

    return wynik[::-1]

def binToDec(liczba):
    wynik = 0
    pot = 0
    while liczba > 0:
        wynik += (liczba % 10) * 2**pot
        pot += 1
        liczba //= 10

    return wynik

def main():
    liczba = int(input("Podaj liczbe dziesietna "))
    print("Binarnie: {0}".format(decToBin(liczba)))
    liczba = int(input("Podaj liczbe binarna "))
    print("Dziesietnie: {0}".format(binToDec(int(liczba))))

if __name__ == '__main__':
    main()
