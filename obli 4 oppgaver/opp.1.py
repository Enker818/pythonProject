"""
Oppgave 1 - Klasser og objekter

Opprett en klasse for filmer med inneholder instansvariabler for filmtittel, utgivelsesår og score.

Bruk denne klassen til å opprette et objekt for hver av de følgende filmene:

Inception - Utgivelsesår: 2010, Score: 8.8
The Martian - Utgivelsesår: 2015, Score: 8.0
Joker - Utgivelsesår: 2019, Score: 8.4

Skriv ut all informasjon om hver film med formatet; "<title> was released in <year> and currently has a score of <score>", ved å benytte de opprettede objektene.
"""
class F:
    def __init__(self, tittel, utgivelsesår, score):
        self.tittel = tittel
        self.utgivelsesår = utgivelsesår
        self.score = score


    def info(self):
        return f"{self.tittel} was released in {self.utgivelsesår} and currently has a score of {self.score}"


    def info2(self):
        if True:
            print(f"{self.tittel} was released in {self.utgivelsesår} and currently has a score of {self.score}")


F1 = F("Inception", 2010, 8.8)
F2 = F("The Martian", 2015, 8.0)
F3 = F("Joker", 2019, 8.4)

print("methode 1")
print(F1.info())
print(F2.info())
print(F3.info())

"""
B) Metoder

Opprett en metode i filmklassen som returnerer en tekststreng med all informasjon om en gitt film på samme format som i forrige deloppgave. Igjen, skriv ut all informasjon om filmobjektene opprettet i forrige deloppgave, men denne gangen ved å benytte den nylig opprettede metoden.
"""
print("methode 2")x| #jeg skjønnte ikke oppgaven helt, jeg tenker dette er det du mente.
F1.info2()
F2.info2()
F3.info2()
