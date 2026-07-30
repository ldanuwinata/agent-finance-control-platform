# 🤖 Agentic Finance Control Platform

An AI-powered portfolio onboarding and financial control workflow built with Python, Pandas, Ollama, and Qwen.

This project demonstrates how **agentic AI** can automate financial data onboarding by standardizing heterogeneous client datasets, validating portfolio data, detecting business exceptions, generating AI-assisted explanations, and producing an audit-ready PDF report.

---

# 🎯 Business Problem

Financial institutions receive portfolio data from multiple clients in different formats.

Before onboarding a portfolio, operations teams must:

- Standardize client-specific column names
- Validate required fields
- Detect data quality issues
- Review business exceptions
- Produce documentation for auditors

These activities are often manual, repetitive, and time-consuming.

This project demonstrates how an **agentic AI workflow** can automate these tasks while keeping each processing step modular and explainable.

---

# 🏗 Architecture

```
Portfolio CSV
      │
      ▼
SchemaMappingAgent
      │
      ▼
ValidationAgent
      │
      ▼
ExceptionDetectionAgent
      │
      ▼
AnalysisAgent
 (Ollama + Qwen3)
      │
      ▼
ReportAgent
      │
      ▼
PDF Exception Report
```

Each agent has a single responsibility, making the system modular, maintainable, and easy to extend.

---

# 🚀 Features

✅ Client schema standardization

- Maps client-specific column names
- Learns mappings using a local knowledge base

---

✅ Portfolio validation

- Required field validation
- Numeric validation
- Missing data detection

---

✅ Exception detection

Business rules currently implemented:

- Missing ISIN
- Missing Currency
- Invalid Number of Shares
- Invalid Market Value

---

✅ AI-powered analysis

Uses a local Large Language Model (Qwen3 via Ollama) to generate concise explanations for detected portfolio exceptions.

Example:

> A negative number of shares was detected for this portfolio position. The position should be reviewed before onboarding.

---

✅ Audit-ready PDF report

Automatically generates a professional portfolio exception report.

---

# 📂 Project Structure

```
agentic-finance-control-platform/

├── data/
│   └── portfolio.csv
│
├── output/
│
├── src/
│   ├── agents/
│   │
│   ├── services/
│   │
│   ├── prompts/
│   │
│   ├── knowledge/
│   │
│   └── main.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🤖 Agents

## SchemaMappingAgent

Maps client-specific column names to the platform's standard schema.

Example:

```
Portfolio
        ↓
Fund

Security ID
        ↓
ISIN
```

---

## ValidationAgent

Validates:

- required columns
- missing values
- numeric fields

---

## ExceptionDetectionAgent

Detects portfolio exceptions using business rules.

Example:

- Missing ISIN
- Invalid Market Value

---

## AnalysisAgent

Uses Ollama + Qwen to generate short AI explanations for each detected exception.

---

## ReportAgent

Creates an audit-style PDF summarizing detected portfolio exceptions.

---

# 🧠 AI Workflow

```
Client Portfolio

↓

Schema Standardization

↓

Validation

↓

Exception Detection

↓

AI Analysis

↓

PDF Report
```

---

# ⚙ Technology Stack

| Layer | Technology |
|---------|------------|
| Language | Python |
| Data Processing | Pandas |
| AI | Ollama |
| LLM | Qwen3 |
| Reporting | ReportLab |
| Architecture | Agent-Based Design |

---

# 📄 Example Console Output

```
==================================================
Agentic Finance Control Platform
==================================================

Client portfolio onboarding...

✅ Schema mapping completed
✅ Validation passed
✅ Detected 3 portfolio exception(s)

===== PORTFOLIO REVIEW =====

Fund              : Global Equity Fund
Exception         : Invalid number of shares

AI Assessment

A negative number of shares was detected for this portfolio position.
```

---

# 📑 Example PDF Output

The generated report contains:

- Processing summary
- Portfolio exceptions
- AI-generated assessments
- Audit-ready formatting

*(A sample report can be found in the `docs/` folder.)*

---

# ▶ Running the Project

## Clone repository

```bash
git clone https://github.com/<your-username>/agentic-finance-control-platform.git

cd agentic-finance-control-platform
```

---

## Create virtual environment

```bash
python -m venv .venv
```

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download:

https://ollama.com

---

## Download the model

```bash
ollama pull qwen3:4b
```

---

## Run the project

```bash
python -m src.main
```

---

# 🔮 Future Improvements

Possible future enhancements include:

- Multi-agent orchestration
- Risk scoring agent
- Financial controls knowledge base
- Vector database for historical exception retrieval
- Interactive web dashboard
- Multi-client schema learning
- Human-in-the-loop approval workflow
- Integration with enterprise document management systems

---

# 🎓 Learning Objectives

This project was developed to explore:

- Agentic AI system design
- Financial data onboarding
- AI-assisted financial controls
- Large Language Model integration
- Modular software architecture
- Prompt engineering
- AI-generated reporting

---

# 👨‍💻 About

This project demonstrates how AI agents can support financial operations by automating repetitive control activities while maintaining transparency and modularity.

The architecture reflects workflows commonly found in:

- Asset Management
- Fund Administration
- Financial Operations
- Audit
- Digital Transformation
- AI-assisted Financial Controls

---

# 📜 License

MIT License