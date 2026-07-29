import pandas as pd

class ValidationAgent:

    def validate(self, dataframe):

        """
        Compare Amound and ExpectedAmount and calculate the variance.
        """

        dataframe['Difference'] = dataframe['Amount'] - dataframe['ExpectedAmount']

        dataframe['Status'] = dataframe['Difference'].apply(lambda x: 'OK' if x == 0 else 'Mismatch')

        return dataframe

    def get_exceptions(self, dataframe):

        """
        Get the rows where the Amount and ExpectedAmount do not match.
        """

        exceptions = dataframe[dataframe['Status'] == 'Mismatch']

        return exceptions