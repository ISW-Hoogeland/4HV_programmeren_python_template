naam = "Alex"

def begroet():
    naam = "Sam"
    print("Hallo", naam)

def groet_ander():
    print("Hoi", naam)

def verander_naam():
    global naam
    naam = "Jamie"
    print("Ik ben", naam)

print("De eerste persoon is", naam)

begroet()
groet_ander()
verander_naam()

print("Na functies ben ik", naam)
