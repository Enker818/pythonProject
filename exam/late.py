order_history = []
def record_order(history_list, order):
    history_list.append(order)
    print("Bestillingen er lagret i historikken.")
menu = {
    "Ribbe": 145.90,
    "Pinnekjøtt": 155.90,
    "Lutefisk": 135.90,
    "Nøttestek": 135.90,
    "Reinsdyrstek": 155.90
}

current_order = {
    "Ribbe": 3,
    "Pinnekjøtt": 1,
    "Reinsdyrstek": 2
}
record_order(order_history, current_order)
print("Ordrehistorikk:")
for idx, order in enumerate(order_history, start=1):
    print(f"Bestilling {idx}: {order}")
