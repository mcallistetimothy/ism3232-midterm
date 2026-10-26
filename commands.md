# Terminal Record: Ridgeline Tool Rental

## 1. Building the project

cd documents
cd ism3232
mkdir ism3232-midterm
cd ism3232-midterm
python3 -m venv .venv
source .venv/bin/activate
pip list
pip install pytest ruff
pip list
pip freeze > requirements.txt
cat requirements.txt
echo '.venv/' > .gitignore
echo '__pycache__/' >> .gitignore
cat .gitignore
printf ".venv/\n__pycache__/\n" > .gitignore
cat .gitignore
touch business_rules.py main.py commands.md README.md
mkdir -p tests
touch tests/__init__.py tests/text_business_rules.py
ls -la
ls -la tests


## 2. The virtual environment

which python3

output: 
/Users/maliyahtimothy/Documents/ism3232/ism3232-midterm/.venv/bin/python3


The output shows that the virtual environment is active because the Python path points to the `.venv` folder inside the `ism3232-midterm` project.

## 3. Project Structure

tree -L 2
```
.
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py
```

4 directories, 8 files

## 4. Every function and test

rg 'def '

tests/test_business_rules.py
13:def test_calculate_rental_cost():
17:def test_discount_two_days():
20:def test_discount_three_days():
23:def test_discount_seven_days():
26:def test_discount_contractor():
31:def test_discounted_cost_below_150():
34:def test_discounted_cost_150():
37:def test_discounted_cost_above_150():
40:def test_quote_with_contractor_discount():
44:def test_deposit_below_1000():
47:def test_deposit_at_1000():
51:def test_inspection_four_days_quote_900():
54:def test_inspection_five_days_quote_900():
57:def test_inspection_six_days_quote_800():
60:def test_inspection_six_days_quote_801():
64:def test_total_quoted_short():
76:def test_total_quoted_long():
89:def test_largest_rental():
106:def test_largest_rental_with_first_customer():
123:def test_largest_rental_empty_list():
127:def test_format_rental_line():

business_rules.py
19:def calculate_rental_cost(daily_rate: float, days: int)-> float:
23:def get_rental_discount(days: int, contractor: bool = False) -> float:
34:def calculate_quote(daily_rate: float, days: int, contractor: bool = False) -> float:
43:def requires_deposit(quote: float) -> bool:
50:def needs_inspection(days: int, quote: float) -> bool:
57:def total_quoted(rentals: list) -> float:
65:def largest_rental(rentals: list) -> str:
76:def format_rental_line(customer: str, quote: float, deposit: bool, inspection: bool) -> str:

## 5. Which files print

rg -l 'print'

output: 
```
main.py
```

## 6. Commit history

git log --oneline

6fa73ad (HEAD -> main, origin/main) ALL TESTS PASSED AFTER 5 RUNS
be48344 Finished troubleshooting, program runs perfectly
9cb7760 Debugging, no output being produced
61daafe Create and run main
fadb34a Create business rules python functions
96b1b8e Set up miderm repo
(.venv) maliyahtimothy@Maliyahs-MacBook-Air-5 ism3232-midterm % 