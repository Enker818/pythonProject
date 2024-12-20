def confirm_order(order_cost):
    print(f"Den totale kostnaden for bestillingen er: {order_cost:.2f} kr.")
    confirmation = input("Bekrefter du bestillingen? Skriv 'yes' eller 'no': ").strip().lower()
    if confirmation == "yes":
        print("Rudolf er grønn på nesen!")
        return True
    else:
        print("Rudolf er rød på nesen!")
        return False
total_cost = 749.50  # Eksempelverdi
confirmation_result = confirm_order(total_cost)
print(f"Bekreftelse mottatt: {confirmation_result}")
