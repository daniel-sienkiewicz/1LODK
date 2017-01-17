# Mnozenie dwoch macierzy / dodawanie wektorow

def dodaj(v1, v2):
    for i in range(0, len(v1)):
        v1[i] += v2[i]
    return v1

def mnozenie(a, b):
    c = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]

    return c

def main():
    v1 = [1, 2, 3, 4]
    v2 = [5, 6, 7, 8]

    print "Dodane: {0}".format(dodaj(v1, v2))
    print "Mnozenie: {0}".format(mnozenie(m1, m2))

if __name__ == '__main__':
    main()
