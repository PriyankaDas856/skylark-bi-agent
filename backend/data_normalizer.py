import pandas as pd


class DataNormalizer:
    @staticmethod
    def remove_duplicate_headers(df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove rows where the first column value is the same as the column header.
        This handles duplicate header rows imported into Monday.com.
        """
        if df.empty:
            return df

        first_col = df.columns[0]

        df = df[
            df[first_col]
            .astype(str)
            .str.strip()
            .str.lower()
            != first_col.strip().lower()
        ]

        return df.reset_index(drop=True)

    @staticmethod
    def normalize_text(df: pd.DataFrame) -> pd.DataFrame:
        """
        Clean text columns by trimming whitespace and fixing common typos.
        """

        replacements = {
            "BIlled": "Billed",
            "billed": "Billed",
            "nan": "",
            "None": "",
        }

        for col in df.select_dtypes(include="object"):
            df[col] = (
                df[col]
                .fillna("")
                .astype(str)
                .str.strip()
                .replace(replacements)
            )

        return df

    @staticmethod
    def normalize_dates(df: pd.DataFrame) -> pd.DataFrame:
        """
        Convert Monday.com date strings into datetime objects.
        """

        date_columns = [
            "Created Date",
            "Close Date",
            "Start Date",
            "End Date",
            "Invoice Date",
            "Collection Date",
        ]

        for col in date_columns:
            if col in df.columns:
                cleaned = (
                    df[col]
                    .astype(str)
                    .str.replace(r" GMT.*", "", regex=True)
                )

                df[col] = pd.to_datetime(
                    cleaned,
                    format="%a %b %d %Y %H:%M:%S",
                    errors="coerce"
                )

        return df

    @staticmethod
    def normalize_sector(df: pd.DataFrame) -> pd.DataFrame:
        """
        Standardize sector names.
        """

        sector_columns = [
            "Sector",
            "Sector/service",
            "Sector/Service",
        ]

        for col in sector_columns:
            if col in df.columns:
                df[col] = (
                    df[col]
                    .fillna("Unknown")
                    .astype(str)
                    .str.strip()
                    .str.title()
                    .replace(
                        {
                            "": "Unknown",
                            "Nan": "Unknown",
                        }
                    )
                )

        return df

    @staticmethod
    def normalize_work_types(df: pd.DataFrame) -> pd.DataFrame:
        """
        Convert comma-separated work types into Python lists.
        """

        if "Type of Work" in df.columns:

            def split_types(value):
                if not value:
                    return []

                return [
                    item.strip()
                    for item in str(value).split(",")
                    if item.strip()
                ]

            df["Type of Work"] = df["Type of Work"].apply(split_types)

        return df

    @staticmethod
    def remove_blank_items(df: pd.DataFrame) -> pd.DataFrame:
        """
        Remove completely blank items.
        """

        if "Item Name" in df.columns:
            df = df[df["Item Name"].astype(str).str.strip() != ""]

        return df.reset_index(drop=True)

    @staticmethod
    def clean(df: pd.DataFrame) -> pd.DataFrame:
        """
        Execute the complete normalization pipeline.
        """

        df = DataNormalizer.remove_duplicate_headers(df)
        df = DataNormalizer.normalize_text(df)
        df = DataNormalizer.normalize_dates(df)
        df = DataNormalizer.normalize_sector(df)
        df = DataNormalizer.normalize_work_types(df)
        df = DataNormalizer.remove_blank_items(df)

        return df