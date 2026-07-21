from fastapi import FastAPI
from pydantic import BaseModel

from backend.monday_client import get_work_orders, get_deals
from backend.data_normalizer import DataNormalizer
from backend.agent import BusinessIntelligenceAgent

app = FastAPI(
    title="Business Intelligence Agent",
    version="1.0.0"
)


class Query(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "Business Intelligence Agent is running!"
    }


@app.post("/ask")
def ask(query: Query):

    # ----------------------------------------
    # Fetch data from Monday.com
    # ----------------------------------------

    work_orders = get_work_orders()
    deals = get_deals()

    # ----------------------------------------
    # Clean datasets
    # ----------------------------------------

    work_orders = DataNormalizer.clean(work_orders)
    deals = DataNormalizer.clean(deals)

    # ----------------------------------------
    # Create Agent
    # ----------------------------------------

    agent = BusinessIntelligenceAgent(
        work_orders,
        deals
    )

    # ----------------------------------------
    # Get Response
    # ----------------------------------------

    response = agent.answer(query.question)

    return {
        "question": query.question,
        **response
    }