# Wczytanie tablicy od uzytkownika (lub z pliku) i posortowanie jej wybranym algorytmem

def sortuj(tab):
    for i in range(len(tab), 0, -1):
        for j in range(0, len(tab) - 1):
            if int(tab[j]) > int(tab[j + 1]):
                tab[j], tab[j + 1] = tab[j + 1], tab[j]

def main():
    tab = []
    with open("data", "r") as f:
        tab = f.read().split(' ')
    print("Tablica przed posortowaniem: {0}".format(tab))
    sortuj(tab)
    print("Tablica po posortowaniu:     {0}".format(tab))
    print("Tablica po posortowaniu:     {0}".format(sorted(tab, key=int)))

if __name__ == '__main__':
    main()
