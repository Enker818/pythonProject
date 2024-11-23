import webshop as ws
from wallet import Wallet


all_wares = {
    "amd_processor": {
        "name": "AMD Ryzen 9 5900X Processor",
        "price": 5590.0,
        "number_in_stock": 50,
        "ratings": [4.5, 4.0, 5.0, 5.0, 4.5, 3.0],
        "description": "All the cores and threads you'll need!",
    },
    "playstation_5": {
        "name": "PlayStation 5",
        "price": 5999.0,
        "number_in_stock": 0,
        "ratings": [5.0, 5.0, 4.5, 2.0, 5.0, 4.5, 4.0],
        "description": "Next generation console, never in stock! like never",
    },
    "hdmi_cable": {
        "name": "Belkin Ultra High Speed HDMI Cable",
        "price": 349.0,
        "number_in_stock": 3,
        "ratings": [5.0, 5.0, 4.5, 5.0, 5.0, 5.0],
        "description": "A high speed overpriced HDMI cable!",
    },
}


all_wares_in_stock = ws.get_all_wares_in_stock(all_wares)
for ware in all_wares_in_stock.values():
    ws.print_ware_information(ware)


shopping_cart = {}
wallet = Wallet(10000)


ws.add_number_of_ware_to_shopping_cart("amd_processor", all_wares["amd_processor"], shopping_cart, 1)
ws.add_number_of_ware_to_shopping_cart("playstation_5", all_wares["playstation_5"], shopping_cart, 2)
ws.add_number_of_ware_to_shopping_cart("hdmi_cable", all_wares["hdmi_cable"], shopping_cart, 4)


ws.buy_shopping_cart(shopping_cart, all_wares, wallet)


print(f"The amount in the wallet after the purchase: {wallet.get_amount()}")
