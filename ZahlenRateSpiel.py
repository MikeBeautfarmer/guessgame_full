import random
import json
import datetime


class Ergebnis:
    def __init__(self, spieler_name, alter, versuche, datum):
        self.spieler_name = spieler_name
        self.alter = alter
        self.versuche = versuche
        self.datum = datum


# Spielfunktion
def spiel_spielen():
    secret = random.randint(1, 50)
    versuche = 0
    punkte_zahl = get_punkte_liste()

    print("Bitte gib mir vor dem Spielantritt deine Daten!")

    spieler_name = input("Bitte gib deinen Namen ein: ")
    alter = input("Bitte gib dein Alter ein: ")

    print("\nViel Spaß beim Spielen!\n")

    while True:
        guess = int(input("Errate die geheime Zahl zwischen 1 und 50): "))
        versuche += 1

        if guess == secret:
            ergebnis_obj = Ergebnis(versuche=versuche, spieler_name=spieler_name, alter=alter, datum=str(datetime.datetime.now()))

            punkte_zahl.append(ergebnis_obj.__dict__)

            with open("punkte_zahl.txt", "w") as punkte_datei:
                punkte_datei.write(json.dumps(punkte_zahl))

            print("Glückwunsch - Du gast die richtige Zahl erraten! Es war die" + " " + str(secret))
            print("Versuche benötigt: " + str(versuche))
            break
        elif guess > secret:
            print("Falsch! .......... Versuche eine kleinere Zahl.")
        elif guess < secret:
            print("Falsch! .......... Versuche eine größere Zahl.")


# Liste der Punktzahl
def get_punkte_liste():
    with open("punkte_zahl.txt", "r") as punkte_datei:
        punkte_zahl = json.loads(punkte_datei.read())
        return punkte_zahl


# Beste Punktzahl
def get_beste_punkte():
    punkte_zahl = get_punkte_liste()
    beste_punkte = sorted(punkte_zahl, key=lambda k: k['versuche'])[:3]
    return beste_punkte


# Spielstart!
while True:
    auswahl = input("Möchtest (A) ein neues Spiel spielen, (B) die Hi-Scores einsehen, oder (C) beenden\n")

    if auswahl.upper() == "A":
        spiel_spielen()
    elif auswahl.upper() == "B":
        for punkte_dict in get_beste_punkte():
            ergebnis_obj = Ergebnis(versuche=punkte_dict.get("versuche"),
                                   spieler_name=punkte_dict.get("name", "Anonym"),
                                   alter=punkte_dict.get("alter"),
                                   datum=punkte_dict.get("datum"))
            print("Spieler: {name}; Versuche: {versuche}; Alter: {alter}, Datum: {datum}".format(name=ergebnis_obj.spieler_name,
                                                                                                 alter=ergebnis_obj.alter,
                                                                                                 versuche=ergebnis_obj.versuche,
                                                                                                 datum=ergebnis_obj.datum))


    else:
        break
