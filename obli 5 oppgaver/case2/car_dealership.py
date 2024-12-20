from datetime import date

car_register = {
    "toyotaBZ4X": {
        "brand": "Toyota",
        "model": "Corolla",
        "price": 96_000,
        "year": 2012,
        "month": 8,
        "new": False,
        "km": 163_000
    },
    "pugeot408": {
        "brand": "Pugeot",
        "model": "408",
        "price": 330_000,
        "year": 2019,
        "month": 1,
        "new": False,
        "km": 40_000
    },
    "audiRS3": {
        "brand": "Audi",
        "model": "RS3",
        "price": 473_000,
        "year": 2022,
        "month": 2,
        "new": True,
        "km": 0
    },
}

NEW_CAR_REGISTRATION_FEE = 8745
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR__FEE = 1000


def print_car_information(car):
    print(f"Brand: {car['brand']}")
    print(f"Model: {car['model']}")
    print(f"Price: {car['price']} Kr")
    print(f"Manufactured year: {car['year']}")
    print(f"Condition: {'New' if car['new'] else 'Used'}")




def create_car(car_register, brand, model, price, year, month, new, km):
    key = brand.lower() + model.lower()
    car_register[key] = {
        "brand": brand,
        "model": model,
        "price": price,
        "year": year,
        "month": month,
        "new": new,
        "km": km,
    }


def get_car_age(car):
    today = date.today()
    år = today.year - car["year"]
    månde = today.month - car["month"]
    return år, månde




def next_eu_control(car):
    today = date.today()
    år = car['year']
    månde = car['month']
    førsteeu = år + 2
    while date(førsteeu,månde,1)<= today:
        førsteeu += 2
    return date(førsteeu, månde, 1)




def rent_car_monthly_price(car):
    rent = car["price"] * RENT_CAR_PERCENTAGE / 12
    if car["new"]:
        rent += RENT_NEW_CAR__FEE
    return rent


def calculate_total_price(car):

    År_avgiff = [
        (3, 6681),
        (11, 4034),
        (29, 1729),
    ]

    today = date.today()
    år = today.year - car['year']
    månde = today.month - car['month']
    if månde < 0:
        år -= 1

    for max_år, fee in År_avgiff:
        if år <= max_år:
            age_fee = fee
            break


    car_price = car['price']
    if car['new']:
        total_price = car_price + 10783
    else:
        total_price = car_price + age_fee

    return total_price






def is_new(car):
    return car['new']


if __name__ == '__main__':
    create_car(car_register, "Volvo", "V90", 850_000, 2021, 12, True, 0)
    toyota = car_register['toyotaBZ4X']
    print_car_information(toyota)
    print(f"\nThe total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)}kr.")
    print(f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}")
    print(f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota):.2f}.\n")

    audi = car_register['audiRS3']
    print_car_information(audi)
    print(f"\nThe total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)}kr.")
    print(f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}")
    print(f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi):.2f}kr.")
