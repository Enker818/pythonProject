def print_ware_information(ware):
    '''Funksjonsbeskrivelse: Printer ut informasjon om en spesifisert vare.'''
    print(f"Name: {ware['name']}")
    print(f"Price: {ware['price']},-")
    print(f"Number in stock: {ware['number_in_stock']}")
    print(f"Description: {ware['description']}")

def calculate_average_ware_rating(ware):
    '''Returnerer den gjennomsnittlige ratingen for en spesifisert vare.'''
    ratings = ware.get("ratings", [])
    if not ratings:
        return TBA
    average_rating = sum(ratings) / len(ratings)
    return round(average_rating, 1)

def get_all_wares_in_stock(all_wares):
    '''Returnerer en dictionary med alle varer som er på lager.'''
    return {key: ware for key, ware in all_wares.items() if ware["number_in_stock"] > 0}

def is_number_of_ware_in_stock(ware, number_of_ware):
    '''Returnerer en Boolean-verdi som representerer om et spesifisert antall av
    en gitt vare finnes på lager.'''
    return ware["number_in_stock"] >= number_of_ware

def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware=1):
    '''Legger til et spesifisert antall av en gitt vare i en spesifisert
    handlevogn.'''
    if ware["number_in_stock"] == 0:
        print(f"Sorry, {ware['name']} is out of stock.")
        return

    available_stock = ware["number_in_stock"]
    quantity_to_add = min(number_of_ware, available_stock)

    if ware_key in shopping_cart:
        shopping_cart[ware_key] += quantity_to_add
    else:
        shopping_cart[ware_key] = quantity_to_add

    ware["number_in_stock"] -= quantity_to_add

    if quantity_to_add < number_of_ware:
        print(f"Only {quantity_to_add} of {ware['name']} was added to the cart due to limited stock.")
    else:
        print(f"{quantity_to_add} of {ware['name']} was added to the cart.")

def calculate_shopping_cart_price(shopping_cart, all_wares, tax):
    total_price = 0.0

    for ware_key, quantity in shopping_cart.items():
        ware = all_wares.get(ware_key)
        if ware:
            total_price += ware["price"] * quantity

    # Apply tax
    total_price_with_tax = total_price * (1 + tax / 100)
    return round(total_price_with_tax, 2)


def buy_shopping_cart(shopping_cart, all_wares, wallet):
    total_price = calculate_shopping_cart_price(shopping_cart, all_wares, 25)
    if wallet.get_amount() >= total_price:
        wallet.subtract_amount(total_price)
        print(f"Purchase successful! Total price: {total_price} NOK")
        clear_shopping_cart(shopping_cart)
    else:
        print("Insufficient funds for this purchase.")

def is_ware_in_stock(ware):
    '''Returnerer en Boolean-verdi som representerer om en vare er på lager.'''
    if ware["number_in_stock"] >= 1:
        return True
    else:
        return False

def clear_shopping_cart(shopping_cart):
    '''Tømmer en handlevogn.'''
    shopping_cart.clear()
