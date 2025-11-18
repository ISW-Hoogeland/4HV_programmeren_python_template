# escape_lib.py
# Tekstbibliotheek voor de Escape Room.
# Leerlingen hoeven dit bestand niet te bewerken.

INTRO_TEKST = """
==========================================
ESCAPE ROOM – START LEVEL
==========================================
Je wordt wakker in een onbekende kamer.
De deur is dicht. Er is geen raam.
Misschien kun je met programmeren ontsnappen.
"""

KAMER1_INTRO = """
KAMER 1: EERSTE ONDERZOEK

Je kijkt rond in de kamer.
Je ziet een groot schilderij aan de muur,
een zware houten deur en een oude tafel in de hoek.
"""

KAMER1_MENU = """
Wat wil je als eerste bekijken?
1. Het schilderij
2. De deur
3. De tafel
"""

KAMER1_HINT_SCHILDERIJ = """
Je stapt dichter naar het schilderij.
Onder het schilderij staat in kleine letters:
"Zoek niet te hoog, wat jij nodig hebt ligt lager dan je denkt."
"""

KAMER1_HINT_DEUR = """
Je loopt naar de deur.
De deur is stevig en lijkt op slot.
Er zit geen sleutelgat aan deze kant.
Misschien moet je eerst iets anders vinden.
"""

KAMER1_HINT_TAFEL = """
Je loopt naar de tafel.
Onder een stapel papieren zie je een kleine sleutel liggen.
Op het label staat: "Alleen voor wie goed gekeken heeft."
"""

KAMER1_NA_HINT = """
Je neemt afstand en denkt na over wat je gezien hebt.
Wat denk jij dat de juiste keuze is om verder te komen?
Je kunt kiezen uit: schilderij, deur of tafel.
"""

KAMER1_JUIST = """
Je loopt vastberaden naar de tafel.
Je pakt de sleutel en hoort een zacht klikgeluid in de deur.
Er is een doorgang vrijgekomen naar de volgende kamer.
"""

KAMER1_ONJUIST = """
Je probeert jouw keuze uit, maar er gebeurt niets.
Blijkbaar heb je de hint nog niet goed begrepen.
Je probeert het nog een keer.
"""

KAMER2_INTRO = """
KAMER 2: DE CODEDEUR

Achter de deur is een klein paneel met een tekstvak.
Boven het vak staat: "Alleen wie de juiste taal spreekt, mag door."
"""

KAMER2_GOED = """
Je hoort meerdere sloten open klikken.
De deur zwaait langzaam open naar een volgende ruimte.
"""

KAMER2_FOUT = """
Er verschijnt een rode tekst op het paneel: "Onjuist."
Je hoort de sloten weer dichtschuiven.
Je zult het opnieuw moeten proberen.
"""

KAMER3_INTRO = """
KAMER 3: KEUZES

Voor je zie je drie nieuwe deuren.
1. Een smalle deur met krassen.
2. Een trap omhoog met een luik.
3. Een lage tunnel waar geluiden uit komen.
"""

KAMER3_DEUR1 = """
Je duwt de smalle deur open.
Achter de deur blijkt een doodlopende gang te zitten.
Je keert terug naar de vorige ruimte.
"""

KAMER3_DEUR2 = """
Je gaat de trap op. Het luik geeft mee en er komt licht binnen.
Bovenaan lijkt een laatste uitdaging te wachten.
"""

KAMER3_DEUR3 = """
Je kruipt de lage tunnel in. De geluiden worden harder.
Plots klapt er achter je iets dicht. Het is te laat om terug te gaan.
"""

KAMER3_ONBEKEND = """
Je twijfelt te lang en doet niets.
Probeer opnieuw met een van de drie opties.
"""

KAMER4_INTRO = """
KAMER 4: EIGEN PUZZEL

Hier komt jouw eigen puzzel.
Pas deze functie aan volgens de opdracht.
Gebruik minstens een variabele, input() en een if/else beslissing.
"""

EINDE_WIN = """
==========================================
 EINDE VAN HET SPEL: JE BENT ONTSNAPT
==========================================
"""

EINDE_VERLIES = """
==========================================
 EINDE VAN HET SPEL: JE BLIJFT ACHTER
==========================================
"""

EINDE_AFRONDING = """
Het spel wordt afgesloten.
"""
