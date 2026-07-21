import pandas as pd


class Analytics:

    @staticmethod
    def work_order_summary(df: pd.DataFrame):
        summary = {
            "total_work_orders": len(df),
        }

        if "Execution Status" in df.columns:
            summary["execution_status"] = (
                df["Execution Status"]
                .value_counts(dropna=False)
                .to_dict()
            )

        if "Sector" in df.columns:
            summary["sector_distribution"] = (
                df["Sector"]
                .value_counts(dropna=False)
                .to_dict()
            )

        if "Billing Status" in df.columns:
            summary["billing_status"] = (
                df["Billing Status"]
                .value_counts(dropna=False)
                .to_dict()
            )

        return summary

    @staticmethod
    def deals_summary(df: pd.DataFrame):
        summary = {
            "total_deals": len(df),
        }

        if "Deal Status" in df.columns:
            summary["deal_status"] = (
                df["Deal Status"]
                .value_counts(dropna=False)
                .to_dict()
            )

        if "Sector/service" in df.columns:
            summary["sector_distribution"] = (
                df["Sector/service"]
                .value_counts(dropna=False)
                .to_dict()
            )

        if "Deal Stage" in df.columns:
            summary["deal_stage"] = (
                df["Deal Stage"]
                .value_counts(dropna=False)
                .to_dict()
            )

        return summary

    @staticmethod
    def overall_summary(work_orders, deals):
        return {
            "work_orders": Analytics.work_order_summary(work_orders),
            "deals": Analytics.deals_summary(deals),
        }