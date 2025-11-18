from datetime import datetime, timedelta

aantal = 0

def begroet():
    # Opdracht 1
    print()

# Opdracht 2
def registreer():
    print("Er zijn", aantal, "mensen nu.")

def weekend():
    now = datetime.now()
    target = now.replace(hour=17, minute=0, second=0, microsecond=0)

    days_ahead = 4 - now.weekday()
    if days_ahead < 0:
        days_ahead += 7

    target = target + timedelta(days=days_ahead)
    if target <= now:
        target += timedelta(days=7)

    uren = (target - now).total_seconds() / 3600
    print(f"Het is nog {uren:.2f} uur tot vrijdag 17:00.")

def einde_dag():
    tijd = input("Hoe laat ben je uit? bijvoorbeeld 16:00")

    uur_str, min_str = tijd.split(":")
    uur = int(uur_str)
    minuten = int(min_str)

while True:
    begroet()
    taak = input("""Wat wil je doen?
    1 - Registreren
    2 - Hoelang tot het weekend?
    3 - Stoppen\n""").lower()

    if taak == "registreren" or taak == "1":
        registreer()
    # Opdracht 3
    if taak == "weekend" or taak == "2":
        weekend()
    # Opdracht 4

