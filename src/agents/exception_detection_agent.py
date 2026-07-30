import pandas as pd


class ExceptionDetectionAgent:
    """
    Detects portfolio exceptions after schema mapping and validation.
    """

    def detect(self, dataframe):
        """
        Detect portfolio exceptions.

        Args:
            dataframe (pd.DataFrame): Validated portfolio dataframe.

        Returns:
            pd.DataFrame: Portfolio positions containing exceptions.
        """

        exceptions = dataframe[
            (dataframe["NumberOfShares"] <= 0)
            | (dataframe["MarketValue"] <= 0)
            | (dataframe["ISIN"].isna())
            | (dataframe["Currency"].isna())
        ].copy()

        exception_types = []

        for _, row in exceptions.iterrows():

            reasons = []

            if pd.isna(row["ISIN"]):
                reasons.append("Missing ISIN")

            if row["NumberOfShares"] <= 0:
                reasons.append("Invalid number of shares")

            if row["MarketValue"] <= 0:
                reasons.append("Invalid market value")

            if pd.isna(row["Currency"]):
                reasons.append("Missing currency")

            exception_types.append(", ".join(reasons))

        exceptions["ExceptionType"] = exception_types

        print(f"✅ Detected {len(exceptions)} portfolio exception(s)")

        return exceptions