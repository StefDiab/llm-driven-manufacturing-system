from planner import extract_orders


orders = extract_orders(
    "Produce 2 type1 parts and 3 type2 parts"
)

print("\nPARSED ORDERS:")
print(orders)