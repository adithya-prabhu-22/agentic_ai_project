def compare_regimes(income, deductions):

    from tax_engine.calculator import old_regime_tax, new_regime_tax

    old_tax = old_regime_tax(income, deductions)
    new_tax = new_regime_tax(income)

    if deductions > 0:
        warning = "Deductions are not allowed under new regime (except standard deduction)."
    else:
        warning = None

    better = "Old Regime" if old_tax < new_tax else "New Regime"

    return {
        "old_tax": old_tax,
        "new_tax": new_tax,
        "better_option": better,
        "warning": warning
    }