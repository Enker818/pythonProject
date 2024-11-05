filmer = [
    {"name": "Inception", "year": 2010, "rating": 8.7},
    {"name": "Inside Out", "year": 2015, "rating": 8.1},
    {"name": "Con Air", "year": 1997, "rating": 7.9}
]

def skriv_til_fil(liste, filnavn):
    with open(filnavn) as f:  # 'w' for å overskrive hvis filen allerede eksisterer
        for film in liste:
            f.write(f"{film['name']} - {film['year']} has a rating of {film['rating']}\n")

# Bruk funksjonen til å skrive filmene til en fil, for eksempel "movies.txt"
filnavn = "movies.txt"
skriv_til_fil(filmer, filnavn)