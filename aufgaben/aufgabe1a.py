def zahlen_eingeben():
    zahl1 = input("Zahl 1: ")
    zahl2 = input("Zahl 2: ")

def zahlen_tauschen():
    hilf = zahl1
    zahl1 = zahl2
    zahl2 = hilf

def zahlen_ausgeben():
    print("Zahl 1: ", zahl1)
    print("Zahl 2: ", zahl2)

zahlen_eingeben()
zahlen_tauschen()
zahlen_ausgeben()

# Das Problem ist, dass es keine globalen Variablen gibt und 
# die Variablen immer direkt verworfen werden.