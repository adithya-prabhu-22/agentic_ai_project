def old_regime_tax(income, deductions):

    taxable_income = income - deductions

    tax = 0

    if taxable_income <= 250000:
        tax = 0
    elif taxable_income <= 500000:
        tax = (taxable_income - 250000) * 0.05
    elif taxable_income <= 1000000:
        tax = 12500 + (taxable_income - 500000) * 0.2
    else:
        tax = 112500 + (taxable_income - 1000000) * 0.3

    return max(tax, 0)


def new_regime_tax(income):

    tax = 0

    if income <= 300000:
        tax = 0
    elif income <= 600000:
        tax = (income - 300000) * 0.05
    elif income <= 900000:
        tax = 15000 + (income - 600000) * 0.1
    elif income <= 1200000:
        tax = 45000 + (income - 900000) * 0.15
    elif income <= 1500000:
        tax = 90000 + (income - 1200000) * 0.2
    else:
        tax = 150000 + (income - 1500000) * 0.3

    return tax