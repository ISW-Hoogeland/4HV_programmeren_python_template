# Loop 1
print("=== loop 1 ===")
scores = [3, 6, 9]
for s in scores:
    print(s * 2)

# Loop 2
boodschappen = []
boodschappen.append("brood")
boodschappen.append("kaas")

for item in boodschappen:
    print(item)

# Loop 3
namen = ["Ali", "Bo", "Cem", "Dana"]
aantal = 0

for n in namen:
    # len() kijkt naar de lengte van een lijst of string
    if len(n) == 3: 
        aantal = aantal + 1

print(aantal)

# Loop 4
letters = ["a", "b", "c"]
nieuw = []

for l in letters:
    nieuw.append(l.upper())

print(letters)
print(nieuw)
