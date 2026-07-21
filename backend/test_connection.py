from pprint import pprint

from backend.monday_client import get_work_orders, get_deals
from backend.data_normalizer import DataNormalizer
from backend.data_quality import DataQuality
from backend.analytics import Analytics
from backend.cross_reference import CrossReference
from backend.agent import BusinessIntelligenceAgent


def main():
    print("=" * 60)
    print("Fetching data from Monday.com...")
    print("=" * 60)

    # Fetch data
    work_orders = get_work_orders()
    deals = get_deals()

    print(f"Fetched {len(work_orders)} Work Orders")
    print(f"Fetched {len(deals)} Deals")

    # Normalize
    work_orders = DataNormalizer.clean(work_orders)
    deals = DataNormalizer.clean(deals)

    print("\nData normalization completed.")

    # -----------------------------
    # Data Quality
    # -----------------------------
    print("\n" + "=" * 60)
    print("DATA QUALITY")
    print("=" * 60)

    wo_report = DataQuality.generate_report(
        work_orders,
        "Work Orders"
    )

    deal_report = DataQuality.generate_report(
        deals,
        "Deals"
    )

    DataQuality.print_report(wo_report)
    print()
    DataQuality.print_report(deal_report)

    # -----------------------------
    # Analytics
    # -----------------------------
    print("\n" + "=" * 60)
    print("BUSINESS ANALYTICS")
    print("=" * 60)

    analytics = Analytics.overall_summary(
        work_orders,
        deals
    )

    pprint(analytics)

    # -----------------------------
    # Cross Reference
    # -----------------------------
    print("\n" + "=" * 60)
    print("SECTOR COMPARISON")
    print("=" * 60)

    sector = CrossReference.compare_by_sector(
        work_orders,
        deals
    )

    pprint(sector)

    print("\n" + "=" * 60)
    print("OWNER COMPARISON")
    print("=" * 60)

    owner = CrossReference.compare_by_owner(
        work_orders,
        deals
    )

    pprint(owner)

    # -----------------------------
    # Agent Demo
    # -----------------------------
    print("\n" + "=" * 60)
    print("BUSINESS INTELLIGENCE AGENT")
    print("=" * 60)

    agent = BusinessIntelligenceAgent(
        work_orders,
        deals
    )

    while True:

        print()

        question = input("Ask a question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        response = agent.answer(question)

        print("\nResponse:\n")
        pprint(response)


if __name__ == "__main__":
    main()