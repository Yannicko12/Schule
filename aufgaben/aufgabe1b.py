def zahlen_eingeben():
    global zahl1, zahl2
    zahl1 = input("Zahl 1 eingeben: ")
    zahl2 = input("Zahl 2 eingeben: ")

def zahlen_tauschen():
    global zahl1, zahl2
    hilf = zahl1
    zahl1 = zahl2
    zahl2 = hilf

def zahlen_ausgeben():
    global zahl1, zahl2
    print("Zahl 1:", zahl1)
    print("Zahl 2:", zahl2)

zahl1 = 0
zahl2 = 0
zahlen_eingeben()
zahlen_tauschen()
zahlen_ausgeben()
