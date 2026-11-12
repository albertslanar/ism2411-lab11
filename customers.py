# Reflection 1: I use .get() when a key might be missing, like an optional email, so the program doesn't crash. 
# I use brackets when the key must exist, because a KeyError shows me the data is wrong. Rule: .get() for optional, brackets for required.
# Reflection 2: It reminds me of a pivot table or SUMIF in Excel. 
# Python is better for large datasets because the same code handles a million rows and can be rerun on multiple data.

# --- Exercise 1 ---
customer={"name": "Max", "email": "max.example@gmail.com", "tier": "gold", "ytd_spend": 14730.00}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# --- Exercise 2 ---
customer["phone"] = "555-0123"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# --- Exercise 3 ---
email = customer.get("email", "no email on file")
print(email)
try:
    print(customer["email"])
except KeyError:
    print("KeyError: the key 'email' does not exist")

# --- Exercise 4 ---
for key, value in customer.items():
    print(f"{key}: {value}")
for key in customer:
    print(key)

# Difference: looping over the dictionary directly gives only the keys.
# Using .items() gives each key and its value together, so I can print "name: Max" without looking the value up again.

# --- Exercise 5 ---
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
discount = tier_discounts.get(customer["tier"], 0)
purchase = 200
final_price = purchase * (1 - discount)
print(f"Tier: {customer['tier']}")
print(f"Discount: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")

# --- Exercise 6 ---
customers = [
    {"name": "Alice", "tier": "gold"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Carla", "tier": "platinum"},
    {"name": "Dan", "tier": "bronze"},
]
purchase = 300
for c in customers:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = purchase * rate
    print(f"{c['name']} | {c['tier']} | discount: ${discount_amount:.2f}")

# --- Exercise 7 ---
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} has only {info['stock']} left")

# --- Exercise 8 ---
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
region_totals = {}
for t in transactions:
    region = t["region"]
    region_totals[region] = region_totals.get(region, 0) + t["amount"]
for region in sorted(region_totals):
    print(f"{region}: {region_totals[region]}")