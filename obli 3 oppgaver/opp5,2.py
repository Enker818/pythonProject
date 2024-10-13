"""
Oppgave 5.2 - Mer funksjoner

Utvid forrige oppgave med noen funksjoner og benytt dem i koden din.

A) Lag en funksjon som printer ut alle filmene i en gitt liste med filmer slik at formatet for hver filmutskrift blir seende slik ut:

The Lion King - 1994 has a rating of 8.5

B) Lag en funksjon som tar en liste med filmer som parameter og regner ut gjennomsnittsratingen for alle filmene i lista og returnerer dette. Test funksjonen og skriv ut gjennomsnittet.
C) Lag en funksjon som tar en liste med filmer og et årstall som parametere, og returnerer en ny liste med alle filmer fra og med det gitte årstallet.
Benytt funksjonen, og print ut informasjon om alle filmer fra og med 2010 (Kan vi  bruke en av funksjonene vi har laget tidligere til å hjelpe oss med noe av dette?).
"""

filmer = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]

def navn(liste):
    for A in liste:
        print(f"{A['name']} - {A['year']} has a rating of {A['rating']}")
def addny():
    Navn = input("navn til filmen?")
    år = int(input("Når kom den ut?"))

    rate = input("Rating til filmen?, hvis ikke finnes skip den, hopp over (trykk Enter):")

    ikke_rate = float(rate) if rate else 5.0

    nyfilm = {"name": Navn, "year": år, "rating": ikke_rate}
    filmer.append(nyfilm)

def gjennom():
    totalR = sum(A["rating"] for A in filmer)
    totalF = len(filmer)
    G = totalR / totalF
    return G




addny()
navn(filmer)
A = gjennom()
print(f"Gjennomsnittsratingen er {A:.1f}")