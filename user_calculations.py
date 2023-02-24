import streamlit as st

st.set_page_config(
    page_title="Testing tax!",
    page_icon="😎"
)

st.title("Tax test")
st.write("Testing out some code to calulate tax...")
st.write("---")

income_total: float = st.number_input("Total income: ")
deduction_total: float = st.number_input("Total deductions: ")
finance_cost_total: float = st.number_input("Total finance costs: ")
division: int = st.number_input("How many people is this divided by: ", step = 1)


def calc_taxtest(income_total, deduction_total, finance_cost_total, division):
    income_totalpp = round(income_total/division, 2)
    deduction_totalpp = round(deduction_total/division, 2)
    finance_cost_totalpp = round(finance_cost_total/division, 2)

    rental_profit = round(income_totalpp - deduction_totalpp, 2)
    # tax calculated from profit
    income_tax_profit = round(rental_profit * 0.2, 2)
    # can deduct a further 20% of mortgage interest costs
    tax_credit = round(finance_cost_totalpp * 0.2, 2)
    tax_owedpp = round(income_tax_profit - tax_credit, 2)
    
    st.success(f"Tax owed per person {tax_owedpp}")

# tax_owedpp = calc_taxtest(income_total, deduction_total, finance_cost_total, division)
# print(tax_owedpp)

if st.button("Calculate tax"):
    calc_taxtest(income_total, deduction_total, finance_cost_total, division)