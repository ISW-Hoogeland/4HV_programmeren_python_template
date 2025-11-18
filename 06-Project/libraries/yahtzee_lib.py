# yahtzee_lib.py
# ---------------------------------------------------------
# Deze library bevat de "regels van Yahtzee".
# Leerlingen mogen dit bestand gebruiken,
# maar NIET aanpassen.
# ---------------------------------------------------------

import random

AANTAL_DOBBELSTENEN = 5
MAX_WORPEN = 3

# De categorieen van de scorekaart
BOVENSTE_CATEGORIEEN = ["enen", "tweeen", "drieen", "vieren", "vijven", "zessen"]
ALLE_CATEGORIEEN = BOVENSTE_CATEGORIEEN + [
    "kans",
    "drie_dezelfde",
    "vier_dezelfde",
    "full_house",
    "kleine_straat",
    "grote_straat",
    "yahtzee",
]

# ---------------------------------------------------------
# FUNCTIES VOOR DOBBELEN
# ---------------------------------------------------------

def rol_dobbelstenen(aantal=AANTAL_DOBBELSTENEN):
    """
    Rol dobbelstenen.

    Parameters:
        aantal (int): hoeveel dobbelstenen worden gegooid

    Return:
        list[int]: lijst met dobbelstenen (waarden 1 t/m 6)
    """
    return [random.randint(1, 6) for _ in range(aantal)]


def toon_dobbelstenen(dobbelstenen):
    """
    Laat de huidige worp zien.
    """
    print("Huidige worp:")
    for i in range(len(dobbelstenen)):
        print(f"Steen {i + 1}: {dobbelstenen[i]}")
    print()

def parse_dobbel_invoer(invoer):
    """
    Zet een invoer zoals '1 3 5' om in een lijst indexen (0 t/m 4)

    Parameters:
        invoer (str): string van de gebruiker

    Return:
        list[int]: bijvoorbeeld [0, 2, 4]
    """
    indexen = []
    delen = invoer.strip().split()
    for deel in delen:
        if deel.isdigit():
            nummer = int(deel)
            if 1 <= nummer <= AANTAL_DOBBELSTENEN:
                indexen.append(nummer - 1)
    return indexen

# ---------------------------------------------------------
# FUNCTIES VOOR SCOREBEREKENING
# ---------------------------------------------------------

def tel_frequenties(dobbelstenen):
    """
    Tel hoe vaak elke dobbelsteenwaarde voorkomt.

    Parameters:
        dobbelstenen (list[int]): de worp

    Return:
        list[int]: frequenties per waarde (index 1 t/m 6)
    """
    freq = [0] * 7
    for v in dobbelstenen:
        freq[v] += 1
    return freq


def is_yahtzee(f):
    """True als er 5 dezelfde zijn."""
    return 5 in f


def is_vier_dezelfde(f):
    """True als er 4 (of 5) dezelfde zijn."""
    return 4 in f or 5 in f


def is_drie_dezelfde(f):
    """True als er 3 (of 5) dezelfde zijn."""
    return 3 in f or 5 in f


def is_full_house(f):
    """True als er 3 dezelfde en 2 dezelfde zijn."""
    return (3 in f and 2 in f) or 5 in f


def is_kleine_straat(d):
    """
    True bij een kleine straat:
    1-2-3-4 of 2-3-4-5 of 3-4-5-6
    """
    s = sorted(set(d))
    mogelijke = [{1,2,3,4}, {2,3,4,5}, {3,4,5,6}]
    return any(m.issubset(s) for m in mogelijke)


def is_grote_straat(d):
    """
    True bij een grote straat:
    1-2-3-4-5 of 2-3-4-5-6
    """
    s = set(d)
    return s == {1,2,3,4,5} or s == {2,3,4,5,6}


def bereken_mogelijke_scores(dobbelstenen):
    """
    Bepaal alle scores die deze worp kan opleveren.

    Parameters:
        dobbelstenen (list[int]): de worp

    Return:
        dict: categorie -> score voor deze worp
    """
    f = tel_frequenties(dobbelstenen)
    totaal = sum(dobbelstenen)

    scores = {
        # Bovenste helft
        "enen":   f[1] * 1,
        "tweeen": f[2] * 2,
        "drieen": f[3] * 3,
        "vieren": f[4] * 4,
        "vijven": f[5] * 5,
        "zessen": f[6] * 6,

        # Overig
        "kans":           totaal,
        "drie_dezelfde":  totaal if is_drie_dezelfde(f) else 0,
        "vier_dezelfde":  totaal if is_vier_dezelfde(f) else 0,
        "full_house":     25 if is_full_house(f) else 0,
        "kleine_straat":  30 if is_kleine_straat(dobbelstenen) else 0,
        "grote_straat":   40 if is_grote_straat(dobbelstenen) else 0,
        "yahtzee":        50 if is_yahtzee(f) else 0,
    }
    return scores

def toon_scorekaart(scorekaart):
    """
    Toon de scorekaart en de totaalscore.
    """
    print("===== SCOREKAART =====")
    for categorie, score in scorekaart.items():
        if score is None:
            print(f"{categorie:13}: (nog leeg)")
        else:
            print(f"{categorie:13}: {score:2} punten")
    print(f"Totaal (incl. bonus): {totaal_met_bonus(scorekaart)} punten")
    print("======================\n")

# ---------------------------------------------------------
# FUNCTIES VOOR SCOREKAART
# ---------------------------------------------------------

def maak_scorekaart():
    """
    Maak een lege scorekaart voor alle categorieen.

    Elke categorie krijgt de waarde None,
    omdat er nog geen score is ingevuld.

    Return:
        dict: categorie (str) → score (None)
              voorbeeld:
              {
                  "enen": None,
                  "tweeen": None,
                  ...
                  "yahtzee": None
              }
    """
    return {cat: None for cat in ALLE_CATEGORIEEN}


def is_categorie_beschikbaar(scorekaart, categorie):
    """
    Controleer of een categorie nog vrij is.

    Parameters:
        scorekaart (dict): de huidige scorekaart
        categorie (str): naam van de categorie

    Return:
        bool: True als de score nog niet is ingevuld
    """
    return categorie in scorekaart and scorekaart[categorie] is None


def vul_categorie_in(scorekaart, categorie, score):
    """
    Vul een score in op de scorekaart.

    Parameters:
        scorekaart (dict): de huidige scorekaart
        categorie (str): naam van de categorie
        score (int): behaalde score voor deze categorie

    Return:
        None
    """
    scorekaart[categorie] = score


# ---------------------------------------------------------
# BONUS
# ---------------------------------------------------------

def bereken_bonus(scorekaart):
    """
    Bereken de bonus voor de bovenste helft.

    Bonus:
        Als enen t/m zessen samen 63 of meer zijn
        én alle zes categorieen zijn ingevuld,
        dan krijg je 35 bonuspunten.

    Parameters:
        scorekaart (dict): de huidige scorekaart

    Return:
        int: 35 of 0
    """
    if not all(scorekaart[c] is not None for c in BOVENSTE_CATEGORIEEN):
        return 0
    som_boven = sum(scorekaart[c] for c in BOVENSTE_CATEGORIEEN)
    return 35 if som_boven >= 63 else 0


def totaal_met_bonus(scorekaart):
    """
    Bereken de totaalscore inclusief bonus.

    Parameters:
        scorekaart (dict): de huidige scorekaart

    Return:
        int: totaalscore (alle categorieen + bonus)
    """
    basis = sum(s for s in scorekaart.values() if s is not None)
    return basis + bereken_bonus(scorekaart)
