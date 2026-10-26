from typing import final


SHORT_RENTAL_DAYS = 3
LONG_RENTAL_DAYS = 7

NO_DISCOUNT = 0.0
REG_RENTAL_DISCOUNT = 0.10
LONG_RENTAL_DISCOUNT = 0.20

DAMAGE_WAIVER = 25.00
DAMAGE_WAIVER_THRESHOLD = 150.00

DEPOSIT_THRESHOLD = 1000.00

INSPECTION_DAYS = 5
INSPECTION_QUOTE_THRESHOLD = 800.00

def calculate_rental_cost(daily_rate: float, days: int)-> float:
    """Calculate the total cost of a rental based on daily rate and number of days"""
    return daily_rate * days

def get_rental_discount(days: int, contractor: bool = False) -> float:
    """Get the discount for a rental based on days and contractor status"""
    if days >= LONG_RENTAL_DAYS:
        return LONG_RENTAL_DISCOUNT
    elif days >= SHORT_RENTAL_DAYS:
        return REG_RENTAL_DISCOUNT
    elif contractor:
        return REG_RENTAL_DISCOUNT
    else:
        return NO_DISCOUNT
    
def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
    """Calculate the final quote for a rental based on daily rate, days, and contractor status"""
    rental_cost = calculate_rental_cost(daily_rate, days)
    discount = get_rental_discount(days, contractor)
    quote = rental_cost * (1 - discount)
    if quote < DAMAGE_WAIVER_THRESHOLD:
        quote += DAMAGE_WAIVER
    return quote #calculate final quote based on rental cost, discount, and damage waiver

def requires_deposit(quote: float) -> bool:
    """Determine if a deposit is required based on the quote"""
    if quote >= DEPOSIT_THRESHOLD:
        return True
    else:
        return False #determine if a deposit is required based on the quote
    
def needs_inspection(days: int, quote: float) -> bool:
    """Determine if an inspection is needed based on rental days and quote"""
    if days >= INSPECTION_DAYS and quote > INSPECTION_QUOTE_THRESHOLD:
        return True
    else:
        return False #determine if an inspection is needed based on rental days and quote

def total_quoted(rentals: list) -> float:
    """Calculate the total quoted amount for all rentals"""
    total = 0.0
    for rental in rentals:
        quote = calculate_quote(rental["daily_rate"], rental["days"], rental["contractor"])
        total += quote
    return total #calculate the total quoted amount for all rentals

def largest_rental(rentals: list) -> str:
    """Returns the customer with the largest rental quote"""
    largest_quote = 0.0
    largest_customer = ""
    for rental in rentals:
        quote = calculate_quote(rental["daily_rate"], rental["days"], rental["contractor"])
        if quote > largest_quote:
            largest_quote = quote
            largest_customer = rental["customer"]
    return largest_customer #find the customer with the largest rental quote  

def format_rental_line(customer: str, quote: float, deposit: bool, inspection: bool) -> str:
    """Format the rental line for display"""
    if deposit is True:
        deposit_str = "Yes"
    else:
        deposit_str = "No"
    if inspection is True:
        inspection_str = "Yes"
    else:
        inspection_str = "No"
    return f"{customer}: ${quote:.2f} | deposit: {deposit_str} | inspection: {inspection_str}"