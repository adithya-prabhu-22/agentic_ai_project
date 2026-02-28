import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
from rag.retriever import query_tax_regime

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def calculate_tax(income, deductions):
    # TODO: Replace with real old vs new regime logic
    return "New"


def generate_explanation(user_income, regime_recommended):

    query = f"""
    Explain tax regime rules applicable for income {user_income}.
    Focus on {regime_recommended} regime.
    """

    context = query_tax_regime(query)

    prompt = f"""
    You are a professional Indian tax assistant.

    STRICT RULES:
    1. Answer ONLY using the provided context.
    2. Do NOT use outside knowledge.
    3. If information is missing, say:
       "Information not available in official policy documents."
    4. Keep explanation clear and structured.

    Context:
    {context}

    Question:
    {query}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content


# ---------------- STREAMLIT UI ---------------- #

st.set_page_config(page_title="AI Tax Regime Advisor", layout="centered")

st.title("AI Tax Regime Advisor")

st.markdown("Enter your details to get a regime recommendation with explanation.")

income = st.number_input("Enter your annual income (₹)", min_value=0, step=10000)
deductions = st.number_input("Enter your total deductions (₹)", min_value=0, step=10000)

if st.button("Calculate"):

    if income <= 0:
        st.warning("Please enter a valid income amount.")
    else:
        with st.spinner("Analyzing tax regime..."):

            recommended = calculate_tax(income, deductions)
            explanation = generate_explanation(income, recommended)

        st.divider()

        st.subheader("Recommended Regime")
        st.success(recommended)

        st.subheader("Explanation")
        st.markdown(explanation)