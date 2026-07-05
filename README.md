# AI Personal Finance Coach

An intelligent **Multi-Agent AI Financial Assistant** that helps users analyze their monthly finances, generate personalized budgets, answer finance-related questions, and create goal-based financial plans through both **text** and **voice** interaction.

---

## Features

*  Voice-enabled financial assistant
*  Chat-based financial guidance
*  Monthly expense analysis
*  Budget recommendations using the 50-30-20 rule
*  Goal-based financial planning
*  Finance question answering (SIP, Mutual Funds, Insurance, Loans, Taxes, etc.)
*  Multi-Agent architecture using LangGraph
*  AI voice response using Edge-TTS

---

#  System Architecture

```
                User
                  │
      ┌───────────┴────────────┐
      │                        │
      ▼                        ▼
 Voice Input               Text Input
      │                        │
      └───────────┬────────────┘
                  ▼
         Speech-to-Text (Groq Whisper)
                  │
                  ▼
            Parser Agent
                  │
                  ▼
           Manager Agent
                  │
      ┌───────────┼─────────────┐
      ▼           ▼             ▼
 Expense      Finance QA    Planning
  Agent         Agent         Agent
      │
      ▼
 Budget Agent
      │
      ▼
 Response Agent
      │
      ▼
 Text + Voice Response
```

---

#  Agents

### 1. Parser Agent

* Extracts structured financial information from natural language.
* Detects:

  * Monthly income
  * Expenses
  * Financial goals

---

### 2. Manager Agent

* Determines which specialized agents should execute.
* Routes tasks dynamically.

---

### 3. Expense Analysis Agent

* Calculates total monthly expenses.
* Computes remaining balance.
* Calculates savings rate.
* Identifies the highest expense category.

---

### 4. Budget Planning Agent

* Applies the 50-30-20 budgeting strategy.
* Compares spending with recommended allocations.
* Suggests improvements.

---

### 5. Financial Planning Agent

* Creates personalized saving strategies.
* Calculates required monthly savings.
* Evaluates whether financial goals are achievable.
* Recommends suitable investment options.

---

### 6. Finance QA Agent

Answers questions related to:

* SIP
* Mutual Funds
* Inflation
* Insurance
* Taxes
* Credit Score
* Loans
* Emergency Fund
* Retirement Planning

---

### 7. Response Agent

* Combines outputs from all agents.
* Produces a single, user-friendly response.
* Generates both text and voice output.

---

#  Technology Stack

### Frontend

* Streamlit

### Backend

* Python 3.10+

### LLM

* Groq API

### Framework

* LangGraph

### AI Framework

* LangChain

### Speech-to-Text

* Groq Whisper

### Text-to-Speech

* Edge-TTS

### Data Validation

* Pydantic

### Environment Management

* python-dotenv

---

#  Project Structure

```
personal-finance-coach/

├── agents/
│   ├── parser_agent.py
│   ├── manager.py
│   ├── expense_agent.py
│   ├── budget_agent.py
│   ├── planning_agent.py
│   ├── finance_qa_agent.py
│   └── response_agent.py
│
├── config/
│   └── settings.py
│
├── graph/
│   ├── state.py
│   └── finance_graph.py
│
├── models/
│   └── llm.py
│
├── tools/
│   ├── calculator.py
│   └── budget.py
│
├── voice.py
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── .env
```

---

#  Installation

Clone the repository

```bash
git clone https://github.com/sandhya29-m/Personal-finance-assistant.git

cd AI-Personal-Finance-Coach
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file.

```
GROQ_API_KEY=your_groq_api_key
```

---

# Run the Application

```bash
streamlit run app.py
```

---

# Example Queries

### Expense Analysis

> My monthly income is ₹80,000. I spend ₹20,000 on rent, ₹10,000 on food, ₹5,000 on shopping, and ₹4,000 on bills. Analyze my expenses.

---

### Financial Goal

> I want to buy a car worth ₹10,00,000 in five years. Can you create a financial plan?

---

### Finance Q&A

> What is SIP and how does it work?

---

### Voice Assistant

Click **Start Recording** and speak naturally, for example:

> My monthly income is eighty thousand rupees. I spend twenty thousand on rent and ten thousand on food. Help me create a budget.

---

# Future Enhancements

* Authentication and user profiles
* Expense history and analytics dashboard
* Investment portfolio tracking
* Bank statement import
* OCR-based bill scanning
* Real-time market insights
* Cloud database integration
* Financial report generation in PDF
* Mobile application support

---

# Demo

Add screenshots or a short demo video here after deployment.

---

# Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository, open issues, or submit pull requests.

---

# License

This project is intended for educational and learning purposes.
