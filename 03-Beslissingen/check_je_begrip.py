print("=== Digitale Studiecoach ===\n")

naam = input("Wat is je naam? ")
gem_wiskunde      = float(input("Gemiddelde Wiskunde: "))
gem_natuurkunde   = float(input("Gemiddelde Natuurkunde: "))
gem_biologie      = float(input("Gemiddelde Biologie: "))
gem_geschiedenis  = float(input("Gemiddelde Geschiedenis: "))
interesse_stem        = input("Interesse in natuur/techniek (ja/nee): ").lower()
interesse_economie    = input("Interesse in economie (ja/nee): ").lower()
interesse_taal_kunst  = input("Interesse in taal/kunst (ja/nee): ").lower()


# Opdracht 1
advies = "E&M"
if (gem_wiskunde >= 6 and gem_natuurkunde >= 6) or (interesse_stem == "ja"):
    advies = "N&T"
if (gem_biologie >= 6.5 and gem_wiskunde >= 5) or (interesse_taal_kunst == "nee" and gem_biologie >= 6.5):
    advies = "N&G"
if (gem_geschiedenis >= 6) or (interesse_economie == "ja"):
    advies = "C&M"
print("\n— Profieladvies:", advies)


# Opdracht 2
wiskunde = "geen"
if gem_wiskunde > 7:
    wiskunde = "Wiskunde B"
else:
    if gem_wiskunde > 5.5:
        wiskunde = "Wiskunde A"
    if gem_wiskunde < 5.5:
        wiskunde = "Vergeet het maar..."
print("\n— Wiskundeadvies:", wiskunde)


# Opdracht 3
toekomst = input("\nWat wil je later studeren (techniek/geneeskunde/economie/creatief/weetniet)? ").lower()
if toekomst == "techniek" and not advies == "N&T":
    print("Techniek zonder N&T is misschien niet handig.")



