import random

def zahlenraten():
    # Der Computer wählt eine zufällige Zahl zwischen 1 und 100
    geheimzahl = random.randint(1, 100)
    versuche = 0
    max_versuche = 10

    print("Willkommen zum Zahlenraten-Spiel!")
    print(f"Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht. Du hast {max_versuche} Versuche, sie zu erraten.")

    while versuche < max_versuche:
        tipp = int(input("Gib deinen Tipp ein: "))
        versuche += 1

        if tipp < geheimzahl:
            print("Meine Zahl ist höher.")
        elif tipp > geheimzahl:
            print("Meine Zahl ist niedriger.")
        else:
            print(f"Glückwunsch! Du hast die Zahl {geheimzahl} in {versuche} Versuchen erraten!")
            break
    else:
        print(f"Schade, du hast die Zahl nicht erraten. Die Zahl war {geheimzahl}.")

# Das Spiel starten
zahlenraten()

