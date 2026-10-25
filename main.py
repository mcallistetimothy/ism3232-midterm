from business_rules import (
    calculate_rental_cost,
    get_rental_discount,
    calculate_quote,
    requires_deposit,
    needs_inspection,
    total_quoted,
    largest_rental,
    format_rental_line,
)

rentals = [
    {"customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
    {"customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True},
    {"customer": "Chowdhury", "daily_rate": 85.00, "days": 4, "contractor": False},
    {"customer": "Dvorak", "daily_rate": 120.00, "days": 10, "contractor": False},
    {"customer": "Eastman", "daily_rate": 210.00, "days": 8, "contractor": True},
    {"customer": "Fujita", "daily_rate": 250.00, "days": 4, "contractor": False},
    {"customer": "Garza", "daily_rate": 95.00, "days": 5, "contractor": True},
    {"customer": "Hughes", "daily_rate": 200.00, "days": 7, "contractor": False},
]

print ("Ridgeline Tool Rental - Rental Report")
for rental in rentals:
    quote = calculate_quote(rental["daily_rate"], rental["days"], rental["contractor"])
    deposit = requires_deposit(quote)
    inspection = needs_inspection(rental["days"], quote)
    rental_line = format_rental_line(rental["customer"], quote, deposit, inspection)
    
    print(rental_line)

inspection_total= 0
for rental in rentals:
    inspection = needs_inspection(rental["days"], calculate_quote(rental["daily_rate"], rental["days"], rental["contractor"]))
    if inspection == True:
        inspection_total += 1

deposit_total = 0
for rental in rentals:
    deposit = requires_deposit(calculate_quote(rental["daily_rate"], rental["days"], rental["contractor"]))
    if deposit == True:
        deposit_total += 1

total = total_quoted(rentals)
largest_customer = largest_rental(rentals)
average_quote = total / len(rentals)

print(f"Rentals: {len(rentals)}")
print(f"\nTotal quoted: ${total:.2f}")
print(f"Average quote: ${average_quote:.2f}")
print(f"Largest quote: {largest_customer}")
print(f"Deposits required: {deposit_total}")
print(f"Inspections required: {inspection_total}")