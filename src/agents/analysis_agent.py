class AnalysisAgent:

    def analyse(self, exceptions):
        # Perform analysis on the exceptions
        analyses = []
        
        for _, row in exceptions.iterrows():

            difference = row['Difference']

            if difference > 0:
                reason = (
                    f"Invoice {row['Invoice']} exceeds the expected amount by"
                    f"by EUR{difference}."
                )

            else:
                reason = (
                    f"Invoice {row['Invoice']} is below the expected amount"
                    f"by EUR{abs(difference)}."
                )

            analyses.append(reason)
                
        return analyses