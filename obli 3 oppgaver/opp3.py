"""
Oppgave 3 – Funksjon – Printe liste
Definer en funksjon som heter print_list().
Denne funksjonen skal ta i mot en liste som parameter, og printe ut hvert element i denne listen en etter en.
Lag deretter kort liste med dine 3 favorittmatretter, og kall funksjonen din med denne listen som parameter.
"""
def print_list(fav_food):
    for A in fav_food:
        print(A)

Mat = ["pizza","Ris","burger"]

print_list(Mat)