def flaeche_rechteck(seite_a, seite_b):
    # Berechnen von Länge mal Breite
    return seite_a * seite_b

gesamtflaeche = 0  # Summe aller Räume

print("\n--- Gesamtflächen-Rechner ---")

while True:
    raumname = input("Gebe einen Raumnamen ein oder 'ende' zum Beenden: ")
    
    if raumname.lower() == "ende":
        break

    unterteilt = input("Besteht der Raum aus zwei Teilflächen? (y/n): ").lower()

    # Erste Fläche
    laenge1 = float(input("Länge der ersten Fläche in m: "))
    breite1 = float(input("Breite der ersten Fläche in m: "))
    raumflaeche = flaeche_rechteck(laenge1, breite1)

    # Zweite Fläche optional
    if unterteilt == "y":
        laenge2 = float(input("Länge der zweiten Fläche in m: "))
        breite2 = float(input("Breite der zweiten Fläche in m: "))
        raumflaeche += flaeche_rechteck(laenge2, breite2)

    # Ausgabe direkt
    print(f"{raumname}: {raumflaeche} m²\n")
    
    # Zur Gesamtsumme addieren
    gesamtflaeche += raumflaeche

print("------------------------------------")
print(f"Gesamte Wohnfläche: {gesamtflaeche} m²")