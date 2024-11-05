"""
Utvid forrige oppgave med noen funksjoner og benytt dem i koden din.

A) Opprett en funksjon som tar en liste med filmer, og filnavn som parameter. Benytt denne funksjonen til å skrive alle filmene i lista til en fil du selv velger navnet på f.eks. "movies.txt". Hvis filen allerede eksisterer, skal den overskrives. Legg gjerne til hver film som en egen linje i filen med et fint format. For eksempel:

The Lion King - 1994 has a rating of 8.5

B) Lag en funksjon som leser den samme filen (filnavn som input-parameter til funksjonen) og skriver ut innholdet til terminalen.
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

def filmer_FromToAnd(liste, År):
    return [film for film in liste if film["year"] >= År]

def skriv_til_fil(liste, filnavn):
    with open(filnavn, 'w') as f:
        for A in liste:
            f.write(f"{A['name']} - {A['year']} has a rating of {A['rating']}\n")


def les(filnavn):
        with open(filnavn, 'r') as f: #'r' står for read mode,
            innhold = f.read()
            print("Innholdet i filen er:")
            print(innhold)





addny()
FA2010 = filmer_FromToAnd(filmer,2010)
navn(FA2010)
A = gjennom()
print(f"Gjennomsnittsratingen er {A:.1f}")
filnavn = "movies.txt"
skriv_til_fil(filmer, filnavn)
les(filnavn)