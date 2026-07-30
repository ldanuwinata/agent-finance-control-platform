from src.services.llm_service import LLMService
from src.services.mapping_store import MappingStore
from src.services.prompt_service import PromptService


class SchemaMappingAgent:

    STANDARD_COLUMNS = [
        "Fund",
        "ISIN",
        "NumberOfShares",
        "MarketValue",
        "Currency"
    ]

    def __init__(self):
        self.llm = LLMService()
        self.mapping_store = MappingStore()
        self.prompt_service = PromptService()

    def map_schema(self, dataframe):
        """
        Maps client column names to the project's standard schema.

        Workflow:
        1. Check if a mapping already exists.
        2. Otherwise ask the LLM.
        3. Save the learned mapping.
        4. Rename the DataFrame.
        """

        rename_dict = {}

        for column in dataframe.columns:

            # 1. Existing mapping
            if self.mapping_store.has_mapping(column):

                standard_name = self.mapping_store.get_standard_name(column)

                print(f"✅ Found mapping for '{column}'")

            # 2. Ask LLM
            else:

                print(f"❌ Unknown column: '{column}'")

                prompt = self.prompt_service.load_prompt(
                    "schema_mapping.md",
                    Column=column,
                    StandardColumns="\n".join(self.STANDARD_COLUMNS)
                )

                standard_name = self.llm.ask(prompt).strip()

                print(f"🤖 Ollama suggests: {standard_name}")

                # Validate LLM response
                if standard_name not in self.STANDARD_COLUMNS:
                    raise ValueError(
                        f"LLM returned invalid standard column: '{standard_name}'"
                    )

                # Store learned mapping
                self.mapping_store.add_mapping(
                    column_name=column,
                    standard_name=standard_name,
                    source="llm"
                )

                print(f"💾 Learned mapping: '{column}' -> '{standard_name}'")

            rename_dict[column] = standard_name

        mapped_dataframe = dataframe.rename(columns=rename_dict)

        print("✅ Schema mapping completed")

        return mapped_dataframe