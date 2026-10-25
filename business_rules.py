SHORT_RENTAL_DAYS = 3
LONG_RENTAL_DAYS = 7

NO_DISCOUNT = 0.0
REG_RENTAL_DISCOUNT = 0.10
LONG_RENTAL_DISCOUNT = 0.20

DAMAGE_WAIVER = 25.00
DAMAGE_WAIVER_THRESHOLD = 150.00

DEPOSIT_THRESHOLD = 1000.00

INSPECTIION_DAYS = 5
INSPECTION_QUOTE_THRESHOLD = 800.00

def calculate_rental_cost(daily_rate: float, days: int)-> float:
    return daily_rate * days #total cost of rental

def get_rental_discount(days: int, contractor: bool = False) -> float:
    if days <= SHORT_RENTAL_DAYS:
        return NO_DISCOUNT
    elif days <= LONG_RENTAL_DAYS:
        return REG_RENTAL_DISCOUNT
    else:
        return LONG_RENTAL_DISCOUNT #calculate discount based on rental days
    
def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
    rental_cost = calculate_rental_cost(daily_rate, days)
    discount = get_rental_discount(days, contractor)
    quote = rental_cost * (1 - discount)
    if quote < DAMAGE_WAIVER_THRESHOLD:
        quote += DAMAGE_WAIVER
    return quote #calculate final quote based on rental cost, discount, and damage waiver

def requires_deposit(quote: float) -> bool:
    if quote >= DEPOSIT_THRESHOLD:
        return True
    else:
        return False #determine if a deposit is required based on the quote
    
def needs_inspection(days: int, quote: float) -> bool:
    if days >= INSPECTIION_DAYS and quote >= INSPECTION_QUOTE_THRESHOLD:
        return True
    else:
        return False #determine if an inspection is needed based on rental days and quote
def total_quoted(rentals: list) -> float:
    total = 0.0
    for rental in rentals:
        quote = calculate_quote(rental["daily_rate"], rental["days"], rental["contractor"])
        total += quote
    return total #calculate the total quoted amount for all rentals

def largest_rental(rentals: list) -> str:
    largest_quote = 0.0
    for rental in rentals:
        quote = calculate_quote(rental["daily_rate"], rental["days"], rental["contractor"])
        if quote > largest_quote:
            largest_quote = quote
            largest_customer = rental["customer"]
    return largest_customer #find the customer with the largest rental quote  
def format_rental_line(customer: str, quote: float, deposit: bool, inspection: bool) -> str:
    if requires_deposit(quote) is True:
        deposit_str = "yes"
    else:
        deposit_str = "no"
    if needs_inspection(quote) is True:
        inspection_str = "yes"
    else:
        inspection_str = "no"
    return f"{customer}: Quote: ${quote:.2f}, Deposit Required: {deposit_str}, Inspection Needed: {inspection_str}"