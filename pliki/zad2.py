# Wyliczenie max, min i sredniej arytmetycznej z tablicy

def licz(tab):
    srednia = 0
    minVal, maxVal = int(tab[0]), int(tab[0])
    for i in tab:
        i = int(i)
        srednia += i
        if i > maxVal:
            maxVal = i
        if i < minVal:
            minVal = i

    print("Srednia {0}".format(srednia/len(tab)))
    print("Min: {0}".format(minVal))
    print("Max: {0}".format(maxVal))

def main():
    tab = []
    with open("data", "r") as f:
        tab = f.read().split(' ')
    print("Tablica: {0}".format(tab))
    licz(tab)

if __name__ == '__main__':
    main()
