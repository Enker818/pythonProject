"""
Oppgave 2 – Funksjon - Tallgenerering

Definer en funksjon som lager en fin utskrift med et tilfeldig generert tall mellom 0 og 100 (husk at du kan benytte random.randrange()). Funksjonen skal ikke ta noen parametere. Eksempelutskrift:

*********

***97***

*********

Kall denne funksjonen noen ganger.
"""

import random

def Rnumber():
    N = random.randrange(0,101)
    print(f"******\n******{N}******\n******")

for i in range(3):
    Rnumber()


