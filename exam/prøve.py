menu = {
    "Ribbe": 145.90,
    "Pinnekjøtt": 155.90,
    "Lutefisk": 135.90,
    "Nøttestek": 135.90,
    "Reinsdyrstek": 155.90
}
def display_menu_item(menu):
    print("Meny:")
    for item, price in menu.items():
        print(f"{item} - {price:.2f} kr")
display_menu_item(menu)

