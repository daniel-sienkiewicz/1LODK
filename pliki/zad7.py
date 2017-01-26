# Baza danych

from prettytable import PrettyTable

class Auto(object):
    """A simple class"""

    count = 0

    def __init__(self, marka="", model="", rokProdukcji=""):
        self.marka = marka
        self.model = model
        self.rokProdukcji = rokProdukcji

def pokazBaze(bazaSamochodow):
    t = PrettyTable(['ID', 'Marka', 'Model', 'Rok Produkcji'])

    for auto in bazaSamochodow:
        t.add_row([auto.id, auto.marka, auto.model, auto.rokProdukcji])

    print t

def dodajAuto(auto, baza):
    auto.id = Auto.count
    baza.append(auto)
    Auto.count += 1

def szukajAuto(baza, klucz):
    wynik = []
    for auto in baza:
        if auto.model == klucz or auto.marka == klucz or auto.rokProdukcji == klucz:
            wynik.append(auto)

    return wynik

def usunAuto(baza, klucz):
    for auto in baza:
        if auto.model == klucz or auto.marka == klucz or auto.rokProdukcji == klucz:
            baza.remove(auto)
            Auto.count -= 1

def main():
    bazaSamochodow = []
    mojeAuto = Auto("Audi", "A3", 2001)
    dodajAuto(mojeAuto, bazaSamochodow)

    mojeAuto2 = Auto("Audi", "80", 1991)
    dodajAuto(mojeAuto2, bazaSamochodow)

    print "Cala baza:"
    pokazBaze(bazaSamochodow)

    wynik = szukajAuto(bazaSamochodow, "80")

    if wynik:
        print "\nSzukane Auta:"
        pokazBaze(wynik)
    else:
        print "\nNie znaleziono szukanego auta"

    usunAuto(bazaSamochodow, "A3")

    print "\nBaza po usunieciu:"
    pokazBaze(bazaSamochodow)

if __name__ == '__main__':
    main()
