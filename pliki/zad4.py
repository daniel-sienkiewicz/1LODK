# Funkcja liczaca miejsca zerowe i delte funkcji kwadratowej

def delta(a, b, c):
    return b**2 - 4*a*c

def zerowe(a, b, c):
    if delta(a, b, c) >= 0:
        x1 = (b * -1 - d) / 2 * a
        x2 = (b * -1 + d) / 2 * a
    else:
        return None

    return [x1, x2]

def main():
    a, b, c = 1, 2, 3
    print "Delta: {0}".format(delta(a, b, c))
    print "miejsca zerowe: {0}".format(zerowe(a, b, c))

if __name__ == '__main__':
    main()
