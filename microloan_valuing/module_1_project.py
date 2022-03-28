# coding: utf-8
import csv
from pathlib import Path

loan_costs = [500, 600, 200, 1000, 450]


population = len(loan_costs)
sum_of_loan_costs = sum(loan_costs)
average = sum_of_loan_costs / population
print(f"Number of loans: {population}")
print(f"Sum of all loans: {sum_of_loan_costs}")
print(f"The average loan cost: {average}")





loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#creating variables needed to solve present value equation
loan_price = loan.get("loan_price")
time = loan.get("remaining_months")
future_value = loan.get("future_value")

present_value = future_value / (1+.20)**time 

#if else statement to decide if loan is worth buying
if present_value >= loan_price:
    print("The loan is worth at least what it costs ti=o purchase!")
else:
        print("The loan is too expensive!")



new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#function that solves present value if parmaters are input in order
def present_value_calc(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate)**remaining_months
    return present_value



print(f"The present value of the loan is: {present_value}")


loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

#list created to add loans <= 500 
inexpensive_loans = []

#going through each loan in list: loans to check if loan_price is <= 500
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan["loan_price"])
print(inexpensive_loans)




# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")


#$writing to inexpensive_loans.csv adding data from list loans
with open(output_path, 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(header)

    for row in loans:
        csvwriter.writerow(row.values())
