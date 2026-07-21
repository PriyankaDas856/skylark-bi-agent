import pandas as pd


class CrossReference:

    @staticmethod
    def compare_by_sector(work_orders: pd.DataFrame, deals: pd.DataFrame):
        """
        Compare Work Orders and Deals aggregated by Sector.
        """

        # Work Order sector column
        if "Sector" in work_orders.columns:
            wo_sector = (
                work_orders["Sector"]
                .fillna("Unknown")
                .astype(str)
                .str.strip()
                .value_counts()
            )
        else:
            wo_sector = pd.Series(dtype=int)

        # Deal sector column
        if "Sector/service" in deals.columns:
            deal_sector = (
                deals["Sector/service"]
                .fillna("Unknown")
                .astype(str)
                .str.strip()
                .value_counts()
            )
        else:
            deal_sector = pd.Series(dtype=int)

        sectors = sorted(
            set(wo_sector.index).union(set(deal_sector.index))
        )

        comparison = []

        for sector in sectors:
            comparison.append(
                {
                    "Sector": sector,
                    "Work Orders": int(wo_sector.get(sector, 0)),
                    "Deals": int(deal_sector.get(sector, 0)),
                }
            )

        return comparison

    @staticmethod
    def compare_by_owner(work_orders: pd.DataFrame, deals: pd.DataFrame):
        """
        Compare datasets by owner/person codes.
        """

        # Work Orders
        wo_col = None
        for col in [
            "BD/KAM Personnel code",
            "Owner code",
            "Person",
        ]:
            if col in work_orders.columns:
                wo_col = col
                break

        # Deals
        deal_col = None
        for col in [
            "Owner code",
            "Person",
        ]:
            if col in deals.columns:
                deal_col = col
                break

        if wo_col is None or deal_col is None:
            return []

        wo_owner = (
            work_orders[wo_col]
            .fillna("Unknown")
            .astype(str)
            .str.strip()
            .value_counts()
        )

        deal_owner = (
            deals[deal_col]
            .fillna("Unknown")
            .astype(str)
            .str.strip()
            .value_counts()
        )

        owners = sorted(
            set(wo_owner.index).union(set(deal_owner.index))
        )

        comparison = []

        for owner in owners:
            comparison.append(
                {
                    "Owner": owner,
                    "Work Orders": int(wo_owner.get(owner, 0)),
                    "Deals": int(deal_owner.get(owner, 0)),
                }
            )

        return comparison