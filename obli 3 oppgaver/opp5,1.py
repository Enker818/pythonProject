"""
A) Opprett en liste med filmer (hvor hver film er en egen dictionary med dataene om én film). Dataene om en film skal minst være: name, year og rating. Legg til filmene:

Inception – 2010 – 8.7
Inside Out – 2015 – 8.1
Con Air – 1997– 6.9
B) Opprett en funksjon som legger til en film i filmlisten. Denne funksjonen skal være definert slik at den minst tar følgende parametere:

Listen filmen skal legges til i
name
year
rating
 Benytt funksjonen til å legge til 3 filmer du selv bestemmer.

C) Modifiser funksjonen fra forrige deloppgave til å sette default-ratingen til 5.0 hvis det ikke gis noen rating som argument til funksjonen. Test at dette fungerer ved å legge til en film uten å spesifisere dens rating.

student = {
    "A": "Ola",
    "B": "Nordmann",
    "C": "Programmering 1"}
"""
filmer = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 6.9}
]
def addny():
    Navn = input("navn til filmen?")
    år = int(input("Når kom den ut?"))

    rate = input("Rating til filmen?, hvis ikke finnes skip den, hopp over (trykk Enter):")

    ikke_rate = float(rate) if rate else 5.0

    nyfilm = {"name": Navn, "year": år, "rating": ikke_rate}
    filmer.append(nyfilm)

addny()
print(filmer)
