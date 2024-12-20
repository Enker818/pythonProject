def place_order(ribbe=0, pinne=0, lute=0, nut=0, rein=0):
    order = {
        "Ribbe": ribbe,
        "Pinnekjøtt": pinne,
        "Lutefisk": lute,
        "Nøttestek": nut,
        "Reinsdyrstek": rein
    }
    if rein > 0:
        print("Buhuu")
    return order
bestilling = place_order(ribbe=2, pinne=1, rein=1)
print(bestilling)
