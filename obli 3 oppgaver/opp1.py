"""
Oppgave 1 - Dictionaries

Lag en dictionary med informasjon om en student:

student = {
    "first name" : "Ola",
    "last name" : "Nordmann,
    "favourite course" : "Programmering 1"
}

Skriv ut studentens fullstendige navn (fornavn og etternavn).
Programmatisk endre studentens favorittkurs til å inkludere kursets emnekode: "ITF10219 Programmering 1"
Programmatisk legg til en alder for studenten i dictionarien. Du kan selv velge hva alderen skal være.
"""
student = {
    "A": "Ola",
    "B": "Nordmann",
    "C": "Programmering 1"}

print(student.get("A"), student.get("B"))
student["C"] = "ITF10219 Programmering 1"
student.update({"D":"21"})
print(student)



