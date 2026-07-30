from src.services.mapping_store import MappingStore
from src.services.llm_service import LLMService


class SchemaMappingAgent:

    STANDARD_COLUMNS = [
        "Invoice",
        "Fund",
        "ActualAmount",
        "ExpectedAmount"
    ]

    def __init__(self):
        self.mapping_store = MappingStore()
        self.llm = LLMService()

    def map_schema(self, df):

        for column in df.columns:

            if self.mapping_store.has_mapping(column):
                print(f"✅ Found mapping for '{column}'")
            else:
                print(f"❌ Unknown column: '{column}'")

        return df