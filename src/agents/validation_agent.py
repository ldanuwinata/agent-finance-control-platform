import pandas as pd

class ValidationAgent:

    REQUIRED_COLUMNS = [
        "Fund",
        "ISIN",
        "NumberOfShares",
        "MarketValue",
        "Currency"
    ]

    NUMERIC_COLUMNS = [
        "NumberOfShares",
        "MarketValue"
    ]

    def validate(self, dataframe):
        errors = []

        # Check required columns
        for column in self.REQUIRED_COLUMNS:
            if column not in dataframe.columns:
                errors.append(f"Missing required column: {column}")

        if errors:
            return False, errors

        # Check numeric columns
        for column in self.NUMERIC_COLUMNS:
            if not pd.api.types.is_numeric_dtype(dataframe[column]):
                errors.append(f"{column} must be numeric.")

        return len(errors) == 0, errors