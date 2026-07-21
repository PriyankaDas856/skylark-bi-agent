import requests
import pandas as pd

from backend.config import (
    MONDAY_API_KEY,
    WORK_ORDERS_BOARD_ID,
    DEALS_BOARD_ID,
)

MONDAY_API_URL = "https://api.monday.com/v2"

HEADERS = {
    "Authorization": MONDAY_API_KEY,
    "Content-Type": "application/json",
}


def fetch_board(board_id: str) -> pd.DataFrame:
    """
    Fetch all items and column values from a Monday.com board.
    Returns a pandas DataFrame.
    """

    query = """
    query ($board_id: ID!) {
      boards(ids: [$board_id]) {
        name
        items_page(limit: 500) {
          items {
            id
            name
            column_values {
              column {
                title
              }
              text
            }
          }
        }
      }
    }
    """

    variables = {"board_id": int(board_id)}

    response = requests.post(
        MONDAY_API_URL,
        headers=HEADERS,
        json={
            "query": query,
            "variables": variables,
        },
        timeout=30,
    )

    response.raise_for_status()

    result = response.json()

    if "errors" in result:
        raise Exception(result["errors"])

    items = result["data"]["boards"][0]["items_page"]["items"]

    rows = []

    for item in items:
        row = {
            "Item Name": item["name"]
        }

        for col in item["column_values"]:
            row[col["column"]["title"]] = col["text"]

        rows.append(row)

    return pd.DataFrame(rows)


def get_work_orders():
    return fetch_board(WORK_ORDERS_BOARD_ID)


def get_deals():
    return fetch_board(DEALS_BOARD_ID)