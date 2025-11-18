from libraries import escape_lib as el


def toon_tekst(tekst):
    """Hulpfunctie om tekst netjes met lege regels eromheen te tonen."""
    print()
    print(tekst.strip())
    print()


def start_spel():
    print(el.INTRO_TEKST)
    naam = input("Wat is jouw naam? ")

    print()
    print("Welkom,", naam)
    print("------------------------------------------")

    kamer_1()


def kamer_1():
    toon_tekst(el.KAMER1_INTRO)
    print(el.KAMER1_MENU)
    keuze = input("Typ 1, 2 of 3: ")

    if keuze == "1":
        toon_tekst(el.KAMER1_HINT_SCHILDERIJ)
    elif keuze == "2":
        toon_tekst(el.KAMER1_HINT_DEUR)
    elif keuze == "3":
        toon_tekst(el.KAMER1_HINT_TAFEL)
    else:
        print()
        print("Ongeldige keuze. Probeer opnieuw.")
        kamer_1()
        return

    toon_tekst(el.KAMER1_NA_HINT)
    poging = input("Typ jouw keuze: ").lower()
    juiste_antwoord = "tafel" 

    if poging == juiste_antwoord:
        toon_tekst(el.KAMER1_JUIST)
        kamer_2()
    else:
        toon_tekst(el.KAMER1_ONJUIST)
        kamer_1()


def kamer_2():
    toon_tekst(el.KAMER2_INTRO)
    geheim = "python"
    invoer = input("Typ het geheime codewoord: ")

    if invoer.lower() == geheim:
        toon_tekst(el.KAMER2_GOED)
        kamer_3()
    else:
        toon_tekst(el.KAMER2_FOUT)
        kamer_2()


def kamer_3():
    toon_tekst(el.KAMER3_INTRO)
    keuze = input("Welke kies je? (1, 2 of 3): ")

    if keuze == "1":
        toon_tekst(el.KAMER3_DEUR1)
        kamer_2()
    elif keuze == "2":
        toon_tekst(el.KAMER3_DEUR2)
        einde_spel(True)
    elif keuze == "3":
        toon_tekst(el.KAMER3_DEUR3)
        einde_spel(False)
    else:
        toon_tekst(el.KAMER3_ONBEKEND)
        kamer_3()


def einde_spel(gewonnen):
    if gewonnen:
        print(el.EINDE_WIN)
    else:
        print(el.EINDE_VERLIES)

    print(el.EINDE_AFRONDING)

start_spel()
