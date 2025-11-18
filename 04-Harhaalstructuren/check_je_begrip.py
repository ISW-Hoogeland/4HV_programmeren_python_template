print("=== Snackautomaat ===\n")

voorraad = 5
bestellingen = 0

# Opdracht 4 
print("Startvoorraad:", voorraad)
while voorraad >= 0:
    print("Nog", voorraad, "snacks over.")  
    # Opdracht 1 
    input("Wil je wat kopen? Het kost 2 euro (ja/nee)") 

    # Opdracht 2 
    prijs = 2.00
    totaal = 0
    while totaal <= prijs:
        invoer = float(input("Voer munt in (bijv. 0.50): "))
        totaal = invoer
        print("Huidig totaal:", totaal)

    # Opdracht 3 
    print("Genoeg betaald!")
    bestellingen += 1
    voorraad -= 1

# Opdracht 5
print("\n--- Bonnetjes ---")
for i in range(bestellingen):
    print("Bonnetje nummer") 
    print("Totaal prijs:")
    print("Snack uitgegeven!")
    print("Bedankt voor je aankoop!\n")