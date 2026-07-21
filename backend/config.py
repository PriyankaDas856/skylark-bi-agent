from dotenv import load_dotenv
import os
from pathlib import Path

# Load .env from backend folder
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

MONDAY_API_KEY = os.getenv("MONDAY_API_KEY")
WORK_ORDERS_BOARD_ID = os.getenv("WORK_ORDERS_BOARD_ID")
DEALS_BOARD_ID = os.getenv("DEALS_BOARD_ID")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")