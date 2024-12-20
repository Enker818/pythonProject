def calculate_total(menu, order):
    total_cost = 0
    for item, quantity in order.items():
        if item in menu:
            total_cost += menu[item] * quantity
    return total_cost
def display_cost(menu, order):

    print("Kostnad for bestillingen:")
    for item, quantity in order.items():
        if item in menu:
            item_cost = menu[item] * quantity
            print(f"{item} - ({quantity}) - {item_cost:.2f} kr")
menu = {
    "Ribbe": 145.90,
    "Pinnekjøtt": 155.90,
    "Lutefisk": 135.90,
    "Nøttestek": 135.90,
    "Reinsdyrstek": 155.90
}
order = {
    "Ribbe": 2,
    "Reinsdyrstek": 2
}
total = calculate_total(menu, order)
print(f"Total kostnad: {total:.2f} kr")
display_cost(menu, order)
