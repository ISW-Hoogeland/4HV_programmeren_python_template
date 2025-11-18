import random

def speel_hoger_lager():
    print("Welkom bij Hoger-Lager!")
    print("De computer heeft een geheim getal gekozen...")

    geheim_getal = random.randint(1, 100)
    geraden = False

    while not geraden:
        invoer = input("Raad een getal tussen 1 en 100: ")
        gok = int(invoer)

        if gok < geheim_getal:
            print("Het geheime getal is hoger.")
        elif gok > geheim_getal:
            print("Het geheime getal is lager.")
        else:
            print("Goed geraden!")
            geraden = True

    print("Einde van het spel.")

print("We gaan een potje Hoger-Lager spelen.")
speel_hoger_lager()
print("Bedankt voor het spelen!")

