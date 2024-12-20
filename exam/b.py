import json
def save_order_to_file(file_name, order):
    try:
        with open(file_name, 'w') as file:
            json.dump(order, file, indent=4)
        print(f"Bestillingen er lagret i filen '{file_name}'.")
    except Exception as e:
        print(f"Kunne ikke lagre bestillingen: {e}")
def load_order_from_file(file_name):
    try:
        with open(file_name, 'r') as file:
            order = json.load(file)
        return order
    except FileNotFoundError:
        print("Fant ikke filen.")
        return None
    except json.JSONDecodeError:
        print("Klarte ikke å lese fra filen, den inneholder ikke gyldig JSON.")
        return None
order = {
    "Ribbe": 2,
    "Pinnekjøtt": 1,
    "Reinsdyrstek": 0
}
file_name = "order1.json"
save_order_to_file(file_name, order)
loaded_order = load_order_from_file(file_name)
print("Lest fra fil:", loaded_order)
