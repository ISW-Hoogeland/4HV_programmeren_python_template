def lees_leeftijd():
    txt = input("Hoe oud ben je? ")
    return int(txt)

def is_volwassen(leeftijd):
    return leeftijd >= 18

def begroet(naam):
    print(f"Hallo {naam}!")

def toestemming_bios(leeftijd):
    if leeftijd >= 16:
        return True
    return False

def mag_film_kijken(naam):
    leeftijd = lees_leeftijd()
    if is_volwassen(leeftijd) or toestemming_bios(leeftijd):
        print(f"{naam} mag naar binnen.")
    else:
        print(f"{naam} mag nog niet naar binnen.")

def bioscoop_robot():
    naam = input("Wat is je naam? ")
    begroet(naam)
    mag_film_kijken(naam)

