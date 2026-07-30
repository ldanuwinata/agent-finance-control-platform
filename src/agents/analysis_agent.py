from src.services.llm_service import LLMService
from src.services.prompt_service import PromptService


class AnalysisAgent:

    def __init__(self):
        self.llm = LLMService()
        self.prompts = PromptService()

    def analyse(self, dataframe):

        analyses = []

        for _, row in dataframe.iterrows():

            prompt = self.prompts.load_prompt(
                "analysis.md",
                Fund=row["Fund"],
                ISIN=row["ISIN"],
                NumberOfShares=row["NumberOfShares"],
                MarketValue=row["MarketValue"],
                Currency=row["Currency"],
                ExceptionType=row["ExceptionType"],
            )

            response = self.llm.ask(prompt)

            analyses.append({
                "Fund": row["Fund"],
                "ExceptionType": row["ExceptionType"],
                "Analysis": response
            })

        return analyses