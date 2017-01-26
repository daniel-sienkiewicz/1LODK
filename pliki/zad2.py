# Wyliczenie max, min i sredniej arytmetycznej z tablicy

def licz(tab):
    srednia = 0
    minVal, maxVal = tab[0], tab[0]

    for i in range(0, len(tab)):
        srednia += int(tab[i])
        if tab[i] > maxVal:
            maxVal = tab[i]
        if tab[i] < minVal:
            minVal = tab[i]

    print "Srednia {0}".format(srednia/len(tab))
    print "Min: {0}".format(minVal)
    print "Max: {0}".format(maxVal)

def main():
    tab = []
    with open("data", "r") as f:
        tab = f.read().split(' ')
    print "Tablica: {0}".format(tab)
    licz(tab)

if __name__ == '__main__':
    main()
