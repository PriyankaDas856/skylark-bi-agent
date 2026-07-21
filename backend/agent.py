from backend.analytics import Analytics
from backend.cross_reference import CrossReference
from backend.data_quality import DataQuality


class BusinessIntelligenceAgent:

    def __init__(self, work_orders, deals):
        self.work_orders = work_orders
        self.deals = deals

    def answer(self, question: str):

        question = question.lower().strip()

        analytics = Analytics.overall_summary(
            self.work_orders,
            self.deals
        )

        work_quality = DataQuality.generate_report(
            self.work_orders,
            "Work Orders"
        )

        deal_quality = DataQuality.generate_report(
            self.deals,
            "Deals"
        )

        work = analytics["work_orders"]
        deals = analytics["deals"]

        top_work_sector = max(
            work["sector_distribution"],
            key=work["sector_distribution"].get
        )

        top_deal_sector = max(
            deals["sector_distribution"],
            key=deals["sector_distribution"].get
        )

        top_stage = max(
            deals["deal_stage"],
            key=deals["deal_stage"].get
        )

        top_status = max(
            work["execution_status"],
            key=work["execution_status"].get
        )

        # ===========================================================
        # EXECUTIVE SUMMARY
        # ===========================================================

        if any(word in question for word in [
            "summary",
            "overview",
            "dashboard",
            "executive",
            "report"
        ]):

            return {
                "answer":
                (
                    f"📊 Executive Business Summary\n\n"

                    f"• Total Work Orders : {work['total_work_orders']}\n"
                    f"• Total Deals : {deals['total_deals']}\n\n"

                    f"• Top Work Order Sector : {top_work_sector}\n"
                    f"• Top Deal Sector : {top_deal_sector}\n\n"

                    f"• Most Common Work Status : {top_status}\n"
                    f"• Largest Deal Stage : {top_stage}"
                ),
                "details": analytics
            }

        # ===========================================================
        # DEAL QUESTIONS
        # ===========================================================

        if any(word in question for word in [
            "deal",
            "sales",
            "pipeline",
            "opportunity"
        ]):

            return {
                "answer":
                (
                    f"📈 Deal Summary\n\n"

                    f"• Total Deals : {deals['total_deals']}\n"
                    f"• Won : {deals['deal_status'].get('Won',0)}\n"
                    f"• Open : {deals['deal_status'].get('Open',0)}\n"
                    f"• Dead : {deals['deal_status'].get('Dead',0)}\n\n"

                    f"• Top Sector : {top_deal_sector}\n"
                    f"• Largest Stage : {top_stage}"
                ),
                "details": deals
            }

        # ===========================================================
        # WORK ORDER QUESTIONS
        # ===========================================================

        if any(word in question for word in [
            "work",
            "execution",
            "project"
        ]):

            return {
                "answer":
                (
                    f"📋 Work Order Summary\n\n"

                    f"• Total Work Orders : {work['total_work_orders']}\n"
                    f"• Most Common Status : {top_status}\n"
                    f"• Top Sector : {top_work_sector}"
                ),
                "details": work
            }

        # ===========================================================
        # SECTOR COMPARISON
        # ===========================================================

        if any(word in question for word in [
            "sector",
            "industry",
            "compare sector"
        ]):

            comparison = CrossReference.compare_by_sector(
                self.work_orders,
                self.deals
            )

            return {
                "answer":
                (
                    "Sector comparison completed.\n\n"
                    "Work Orders and Deals have been compared "
                    "using Sector as the common business dimension."
                ),
                "details": comparison
            }

        # ===========================================================
        # OWNER COMPARISON
        # ===========================================================

        if any(word in question for word in [
            "owner",
            "person",
            "employee",
            "manager"
        ]):

            comparison = CrossReference.compare_by_owner(
                self.work_orders,
                self.deals
            )

            return {
                "answer":
                (
                    "Owner comparison completed successfully."
                ),
                "details": comparison
            }

        # ===========================================================
        # DATA QUALITY
        # ===========================================================

        if any(word in question for word in [
            "quality",
            "duplicate",
            "missing",
            "null",
            "clean"
        ]):

            return {
                "answer":
                (
                    "Data Quality Analysis\n\n"

                    f"Work Orders\n"
                    f"• Rows : {work_quality['total_rows']}\n"
                    f"• Duplicate Rows : {work_quality['duplicate_rows']}\n\n"

                    f"Deals\n"
                    f"• Rows : {deal_quality['total_rows']}\n"
                    f"• Duplicate Rows : {deal_quality['duplicate_rows']}"
                ),
                "details":
                {
                    "work_orders": work_quality,
                    "deals": deal_quality
                }
            }

        # ===========================================================
        # UNSUPPORTED ROW MATCHING
        # ===========================================================

        if any(word in question for word in [
            "match",
            "linked",
            "which deal",
            "which work order"
        ]):

            return {
                "answer":
                (
                    "I cannot accurately match individual Deals to "
                    "Work Orders because the two datasets do not "
                    "share a reliable common identifier.\n\n"
                    "You can compare them using Sector or Owner Code."
                )
            }

        # ===========================================================
        # DEFAULT
        # ===========================================================

        return {
            "answer":
            (
                "I can help analyze Monday.com business data.\n\n"
                "Try asking one of these questions."
            ),
            "examples":
            [
                "Executive summary",
                "Show deal summary",
                "Show work order summary",
                "Compare sectors",
                "Compare owners",
                "Show data quality",
                "Which sector performs best?",
                "How many won deals do we have?",
                "Show project summary"
            ]
        }