import pandas as pd

income_total = float(input("Total income: "))
deduction_total = float(input("Total deductions: "))
finance_cost_total = float(input("Total finance costs: "))
division = int(input("How many people is this divided by: "))



income_totalpp = round(income_total/division, 2)
deduction_totalpp = round(deduction_total/division, 2)
finance_cost_totalpp = round(finance_cost_total/division, 2)

rental_profit = round(income_totalpp - deduction_totalpp, 2)
    # tax calculated from profit
income_tax_profit = round(rental_profit * 0.2, 2)
    # can deduct a further 20% of mortgage interest costs
tax_credit = round(finance_cost_totalpp * 0.2, 2)
tax_owedpp = round(income_tax_profit - tax_credit, 2)

print(tax_owedpp)
