"""
Raumrechner Programm
----------------------
Dieses Programm ermöglicht die Eingabe von Raummaßen und Raumbezeichnungen.
Es berechnet die Fläche einzelner Räume sowie die Gesamtfläche aller Räume.

Version 1.0
"""


def berechne_flaeche(laenge, breite):
    """Berechnet die Fläche eines Raumes."""
    return laenge*breite

def raum_eingebenb():
    """Fragt Benutzereingaben für einen Raum ab"""
    name = input("Raumbezeichnung eingeben: ")

    while True:
        try:
            laenge = float(input("Länge in Metern"))
            breite = float(input("Breite in Metern"))
            if laenge <= 0 or breite <= 0:
                print("Bitte nur positive Zahlen eingeben")
                continue
            break
        except ValueError:
            print("Ungültige Eingabe. Bitte Zahl eingeben.")

    flaeche = berechne_flaeche(laenge, breite)
    return name, flaeche

def hauptprogramm():
    """Steuert den Ablauf des Programmes"""
    raeume = []
    gesamtflaeche = 0

    print("=== Raumflächen Rechner ===")

    while True:
        name, flaeche = raum_eingeben()
        raeume.append((name,flaeche))
        gesamtflaeche += flaeche

        weitere = input("Weiteren Raum eingeben?(j/n):").lower()
        if weitere !="j":
            break

    print("\n---Ergebnis---")
    for name, flaeche in raeume:
        print(f"[name]: [flaeche:.2f] m²")

    print(f"\nGesamtfläche: [gesamtflaeche:.2f] m²")


    #Startpunkt des Programms
    if__name__="__main__":
      hauptprogramm()