# 🚀 Skylark Business Intelligence Agent

An AI-powered Business Intelligence dashboard built as part of the Skylark AI Engineering Assignment. The application analyzes Deals and Work Orders data from Monday.com and generates executive-level business insights using a FastAPI backend and an interactive Streamlit dashboard.

---

## 📌 Project Overview

The Business Intelligence Agent connects to Monday.com, processes business data, performs analytics, and generates natural-language insights for executives. It provides an intuitive dashboard with KPIs, charts, and AI-generated summaries to help stakeholders make informed business decisions.

---

## ✨ Features

- 📊 Interactive executive dashboard
- 🤖 AI-generated business insights
- 📈 KPI cards for business metrics
- 📉 Deal status distribution
- 🛠️ Work order status analysis
- 🏢 Sector-wise business analysis
- 🔍 Data quality reporting
- 🔄 Cross-reference analysis between Deals and Work Orders
- ⚡ FastAPI REST API backend
- 🎨 Modern Streamlit frontend with Plotly visualizations

---

## 🏗️ System Architecture

```
Monday.com API
       │
       ▼
FastAPI Backend
       │
       ├── Data Collection
       ├── Data Cleaning
       ├── Analytics Engine
       ├── Business Intelligence Agent
       └── REST API
       │
       ▼
Streamlit Dashboard
       │
       ├── KPI Cards
       ├── Charts
       ├── Executive Summary
       └── Business Insights
```

---

## 📂 Project Structure

```
skylark-bi-agent/
│
├── backend/
│   ├── agent.py
│   ├── analytics.py
│   ├── data_loader.py
│   ├── main.py
│   └── models.py
│
├── frontend/
│   ├── app.py
│   └── styles.css
│
├── README.md
├── requirements.txt
├── decision_log.md
└── .gitignore
```

---

## 🛠️ Tech Stack

### Backend
- FastAPI
- Python
- Monday.com GraphQL API
- Pandas
- Requests

### Frontend
- Streamlit
- Plotly
- HTML/CSS

### Tools
- Git
- GitHub
- VS Code

---

## 📊 Dashboard Features

- Executive Summary
- Business KPIs
- Deal Status Distribution
- Work Order Status
- Sector-wise Deal Analysis
- Sector-wise Work Order Analysis
- Data Quality Report
- AI Business Insights

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/PriyankaDas856/skylark-bi-agent.git
cd skylark-bi-agent
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file inside the project root.

```env
MONDAY_API_TOKEN=your_token
DEALS_BOARD_ID=your_board_id
WORK_ORDERS_BOARD_ID=your_board_id
```

---

## ▶️ Run Backend

```bash
uvicorn backend.main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

## ▶️ Run Frontend

```bash
streamlit run frontend/app.py
```

Frontend runs on:

```
http://localhost:8501
```

---

## 📈 Business Insights Generated

The Business Intelligence Agent provides:

- Executive Summary
- Total Deals
- Total Work Orders
- Active Opportunities
- Revenue Distribution
- Sector Performance
- Work Order Completion Status
- Data Quality Assessment
- Business Recommendations

---

## 🔒 Security

- API tokens stored securely using environment variables
- `.env` excluded from version control
- No sensitive credentials stored in the repository

---

## 🚀 Future Improvements

- Predictive analytics
- Revenue forecasting
- Automated anomaly detection
- LLM-powered conversational BI assistant
- User authentication
- Deployment on cloud infrastructure
- Export reports as PDF/Excel

---

## 👩‍💻 Author

**Priyanka Das**

GitHub: https://github.com/PriyankaDas856

---

## 📄 License

This project was developed as part of the **Skylark AI Engineering Assignment** and is intended for evaluation purposes.
