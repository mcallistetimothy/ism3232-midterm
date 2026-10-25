def calculate_rental_cost(daily_rate: float, days: int)-> float:
    pass
def get_rental_discount(days: int, contractor: bool = False) -> float:
    pass
def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
    pass
def requires_deposit(quote: float) -> bool:
    pass
def needs_inspection(days: int, quote: float) -> bool:
    pass
def total_quoted(rentals: list) -> float:
    pass
def largest_rental(rentals: list) -> str:
    pass    
def format_rental_line(customer: str, quote: float, deposit: bool, inspection: bool) -> str:
    pass
