# AI Tax Regime Advisor

AI Tax Regime Advisor is a simple AI-powered tax assistant that helps users understand and compare Indian tax regimes using tax rules, policy data, a basic tax calculator, and Retrieval-Augmented Generation (RAG).

The project combines structured tax calculation logic with document retrieval so users can ask tax-related questions and receive context-aware answers.

## Features

- Old vs new tax regime guidance
- Tax calculation logic
- RAG-based document retrieval
- Tax policy data support using JSON
- Groq LLM integration
- Vector store for document search
- Simple Python application structure

## Project Structure

```text
AI-Tax-Regime-Advisor/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── pdfs/
│   │   └── tax_regime_summary_2025.txt
│   │
│   └── policy/
│       └── tax_rules_2025_26.json
│
├── rag/
│   ├── ingest.py
│   ├── retriever.py
│   └── vector_store/
│
├── tax_engine/
│   ├── calculator.py
│   └── regime_logic.py
│
└── utils/
    └── helpers.py