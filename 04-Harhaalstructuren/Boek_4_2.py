# loop 1
t = 3
while t != 0:
    print("Tijd:", t)
    t -= 1

# loop 2
energie = 10
while energie > 0:
    print("Nog energie:", energie)
    energie = energie + 1

# loop 3
antwoord = input("Ja of nee? ")
while antwoord == "nee":
    print("Niet akkoord.")

# loop 4
levens = 3
teller = 0
while levens > 0:
    print("Nog", levens, "levens")
    teller += 1  

# loop 5
while True:
    cmd = input("Commando: ")
    if cmd == "exit":
        break
    print("Je koos:", cmd)