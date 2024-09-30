
def legg_til(liste):
    item = input("Hva vil du legge til i pakkelisten? ")
    liste.append(item)
    print(f"'{item}' er lagt til i listen.")

def slett_item(liste):
    item = input("Hva vil du slette fra pakkelisten? ")
    if item in liste:
        liste.remove(item)
        print(f"'{item}' er slettet fra listen.")
    else:
        print(f"'{item}' finnes ikke i listen.")

def skriv_ut(liste):
    if liste:
        print("Her er din pakkeliste:")
        i = 0
        while i < len(liste):
            print(f"{i + 1}. {liste[i]}")
            i += 1
    else:
        print("Pakkelisten er tom.")

def avslutt():
    print("Avslutter programmet...")
    exit()


def hovedprogram():
    pakkeliste = []


    while True:
        print("kommands:\n"
              "1 - Legg til i pakkelisten\n"
              "2 - Slett fra pakkelisten\n"
              "3 - Skriv ut pakkelisten\n"
              "4 - Avslutt\n")

        valg = input("Hva vil du gjøre? Skriv inn kommands (1-4): ")

        if valg == "1":
            legg_til(pakkeliste)
        elif valg == "2":
            slett_item(pakkeliste)
        elif valg == "3":
            skriv_ut(pakkeliste)
        elif valg == "4":
            avslutt()
        else:
            print("Ugyldig valg, velg mellom 1-4.\n")


hovedprogram()
