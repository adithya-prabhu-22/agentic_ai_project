def compliance_warnings(income, deductions, regime):

    warnings = []

    if regime == "new" and deductions > 0:
        warnings.append("Most Chapter VI-A deductions are not allowed under New Regime.")

    if regime == "old" and income <= 500000:
        warnings.append("Check eligibility for Section 87A rebate.")

    if regime == "new" and income <= 1200000:
        warnings.append("Check eligibility for enhanced Section 87A rebate.")

    return warnings