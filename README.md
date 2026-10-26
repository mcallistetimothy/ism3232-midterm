ISM3232 Midterm: Ridgeline Tool Rental

Name: Maliyah Calliste Timothy
Version: Alpha
Date: October 25, 2026

What This Program Does

This program creates rental quotes for Ridgeline Tool Rental based on the daily rental rate, number of rental days, and contractor status. It applies discounts and damage waiver fees when needed and determines whether a deposit or inspection is required. The program also calculates the total amount quoted and identifies the customer with the largest rental quote.

Business Rules

The basic rental cost is calculated by multiplying the daily rental rate by the number of rental days.

Rentals from 3 to 6 days receive a 10% discount, while rentals of 7 days or more receive a 20% discount. Rentals under 3 days normally receive no discount, but contractors receive at least a 10% discount.

A $25 damage waiver is added when the rental cost after the discount is less than $150.

A deposit is required when the final rental quote is $1,000 or more.

An inspection is required when the rental lasts at least 5 days and the final quote is greater than $800.

The program calculates the total amount quoted for all rentals and identifies the customer with the largest rental quote. If two customers have the same largest quote, the first customer is returned.

How to Run

python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py

How to Test

I wrote 21 tests to check the business rules and boundary conditions.

ruff check .
pytest -v

Files in This Repository

.gitignore — Lists the files and folders that Git should ignore.

business_rules.py — Contains the constants and functions used to apply the rental business rules.

main.py — Contains the rental data, calls the business rule functions, and prints the rental report.

commands.md — Contains the terminal commands and outputs used while building and testing the project.

README.md — Explains the project, business rules, setup instructions, testing instructions, and repository files.

requirements.txt — Lists the Python packages and versions needed for the project.

tests/init.py — Marks the tests folder as a Python package.

tests/test_business_rules.py — Contains the 21 pytest tests for the business rule functions.

AI Use Statement

I did not use AI while completing the original exam.
