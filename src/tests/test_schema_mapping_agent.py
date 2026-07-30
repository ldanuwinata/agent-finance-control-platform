import pandas as pd

from src.agents.schema_mapping_agent import SchemaMappingAgent
from src.services.mapping_store import MappingStore


def main():

    # Add one known mapping
    store = MappingStore()
    store.add_mapping("Invoice Number", "Invoice")

    # Create a sample DataFrame
    df = pd.DataFrame({
        "Invoice Number": ["INV001"],
        "Gross Amount": [1000],
        "Budget": [900]
    })

    agent = SchemaMappingAgent()

    mapped_df = agent.map_schema(df)

    print("\nColumns:")
    print(mapped_df.columns.tolist())

    print("\nDataFrame:")
    print(mapped_df)

if __name__ == "__main__":
    main()