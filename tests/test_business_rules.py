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

#caculate rental cost
def test_calculate_rental_cost():
    assert round(calculate_rental_cost(100.00, 5), 2) == 500.00

#test discount for 2 days, 3 days, and 7 days
def test_discount_two_days():
    assert get_rental_discount(2) == 0.0

def test_discount_three_days():
    assert get_rental_discount(3) == 0.10

def test_discount_seven_days():
    assert get_rental_discount(7) == 0.20

def test_discount_contractor():
    assert get_rental_discount(2, contractor=True) == 0.10
    assert get_rental_discount(2, contractor=False) == 0.00

#test discounted cost below 150
def test_discounted_cost_below_150():
    assert round(calculate_quote(74.50, 2), 2) == 174.00

def test_discounted_cost_150():
    assert round(calculate_quote(75.00, 2), 2) == 150.00

def test_discounted_cost_above_150():
    assert round(calculate_quote(75.50, 2), 2) == 151.00

def test_quote_with_contractor_discount():
    assert round(calculate_quote(50.00, 2, True), 2) == 115.00

#requires deposit tests
def test_deposit_below_1000():
    assert requires_deposit(999.99) == False

def test_deposit_at_1000():
    assert requires_deposit(1000.00) == True

#needs inspection tests over 5 days and quote over 800
def test_inspection_four_days_quote_900():
    assert needs_inspection(4, 900.00) == False

def test_inspection_five_days_quote_900():
    assert needs_inspection(5, 900.00) == True

def test_inspection_six_days_quote_800():
    assert needs_inspection(6, 800.00) == False

def test_inspection_six_days_quote_801():
    assert needs_inspection(6, 801.00) == True

#total quoted tests
def test_total_quoted_short():
    rentals = [
        {
            "customer": "Alvarez", "daily_rate": 60.00, "days": 2, "contractor": False},
        {
            "customer": "Brennan", "daily_rate": 60.00, "days": 2, "contractor": True,
        },
    ]
    expected_total = (calculate_quote(60.00, 2, False) + calculate_quote(60.00, 2, True))

    assert round(total_quoted(rentals), 2) == round(expected_total, 2)
    
def test_total_quoted_long():
    rentals = [
        {
            "customer": "Chowdhury", "daily_rate": 85.00, "days": 4, "contractor": False},
        {
            "customer": "Dvorak", "daily_rate": 120.00, "days": 10, "contractor": False,
        },
    ]
    expected_total = (calculate_quote(85.00, 4, False) + calculate_quote(120.00, 10, False))

    assert round(total_quoted(rentals), 2) == round(expected_total, 2)

#largest rental tests
def test_largest_rental():
    rentals = [
        {
            "customer": "Small",
            "daily_rate": 50.00, 
            "days": 2, 
            "contractor": False,
        },
        {
            "customer": "Large",
            "daily_rate": 100.00,
            "days": 5,
            "contractor": False,
        },
    ]
    assert largest_rental(rentals) == "Large"

def test_largest_rental_with_first_customer():
    rentals = [
        {
            "customer": "First",
            "daily_rate": 100.00,
            "days": 5,
            "contractor": False,
        },
        {
            "customer": "Second",
            "daily_rate": 100.00,
            "days": 5,
            "contractor": False,
        },
    ]
    assert largest_rental(rentals) == "First"

def test_largest_rental_empty_list():
    assert largest_rental([]) == ""

#format rental line tests
def test_format_rental_line():
    result = format_rental_line("A", 100.00, True, False)
    assert result == "A: $100.00 | deposit: Yes | inspection: No"