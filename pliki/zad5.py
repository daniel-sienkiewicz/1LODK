# Dodawanie wektorow

def dodaj(v1, v2):
    v = v1
    for i in range(0, len(v1)):
        v[i] += v2[i]
    return v

def main():
    v1 = [1, 2, 3, 4]
    v2 = [5, 6, 7, 8]

    m1 = [[1, 3], [2, -2], [-1, 4]]
    m2 = [[2, 1, 3], [-1, 2, 4]]

    print("Dodane: {0}".format(dodaj(v1, v2)))

if __name__ == '__main__':
    main()
