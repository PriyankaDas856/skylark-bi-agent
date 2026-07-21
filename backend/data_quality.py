import pandas as pd


class DataQuality:

    @staticmethod
    def generate_report(df: pd.DataFrame, dataset_name: str) -> dict:
        """
        Generate a data quality report.
        """

        # Create a copy so we don't modify the original dataframe
        duplicate_df = df.copy()

        # Convert lists into strings so pandas can hash them
        for col in duplicate_df.columns:
            duplicate_df[col] = duplicate_df[col].apply(
                lambda x: ", ".join(x) if isinstance(x, list) else x
            )

        report = {
            "dataset": dataset_name,
            "total_rows": len(df),
            "total_columns": len(df.columns),
            "duplicate_rows": int(duplicate_df.duplicated().sum()),
            "missing_values": {}
        }

        for col in df.columns:

            missing = df[col].isna().sum()

            if df[col].dtype == object:
                missing += (df[col] == "").sum()

            report["missing_values"][col] = int(missing)

        return report

    @staticmethod
    def print_report(report: dict):

        print("=" * 60)
        print(f"DATA QUALITY REPORT : {report['dataset']}")
        print("=" * 60)

        print(f"Rows        : {report['total_rows']}")
        print(f"Columns     : {report['total_columns']}")
        print(f"Duplicates  : {report['duplicate_rows']}")

        print("\nMissing Values")

        for column, value in report["missing_values"].items():
            print(f"{column:<35} {value}")

        print("=" * 60)