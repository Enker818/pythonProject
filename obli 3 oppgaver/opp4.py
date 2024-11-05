"""
Oppgave 4 – Funksjon – Volum

Lag en funksjon for å regne ut volumet av et tredimensjonalt objekt.
Vi lar ting være enkelt og forholder oss bare til enkle verdier for lengde, bredde og høyde.
Volumet kan da beregnes med følgende formel: lengde*bredde*høyde.
Du skal ta lengden, bredden og høyden som individuelle input-parametere for funksjonen, og returnere volumet. Kall funksjonen noen ganger med forskjellige verdier for lengde, bredde og høyde, og skriv ut resultatet av hver utregning.
"""

def volumkal(A,B,C):
    volum = A * B * C
    return volum

L = int(input("tast in lengde"))
B = int(input("tast in bredden"))
H = int(input("tast in høyden"))

V = volumkal(L,B,H)


print(f"volum er {V}")