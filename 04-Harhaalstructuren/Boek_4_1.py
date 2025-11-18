# voorbeeld 1
levens = 3
while levens > 0:
    print("Je speelt nog!")
    levens = levens - 1

# voorbeeld 2
score = 0
while score < 100:
    print("Score:", score)
    score += 10

# voorbeeld 3
while True:
    naam = input("Wat is je naam? (typ 'stop' om te stoppen) ")

    if naam == "stop":
        break

    print("Hallo,", naam)

