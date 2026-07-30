from services.llm_service import LLMService

class AnalysisAgent:

    def __init__(self):
        self.llm_service = LLMService()

    def analyse(self, exceptions):
        # Perform analysis on the exceptions
        analyses = []
        
        for _, row in exceptions.iterrows():

            difference = row['Difference']

            prompt = f"""
            You are an expert financial analyst.
            Analyze this invoice discrepancy.
            Invoice: {row['Invoice']}
            Expected Amount: {row['Expected Amount']}
            Actual Amount: {row['Actual Amount']}
            Difference: {difference}

            Write ashort explanation in one sentence.
            """

            reason = self.llm_service.ask(prompt)
            

            analyses.append(reason)
                
        return analyses