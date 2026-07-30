import pandas as pd

from src.agents.schema_mapping_agent import SchemaMappingAgent
from src.agents.validation_agent import ValidationAgent
from src.agents.analysis_agent import AnalysisAgent

# Create sample client data
df = pd.DataFrame({
    "Invoice Number": ["INV001"],
    "Gross Amount": [1000],
    "Budget": [900]
})

# Step 1: Map schema
mapper = SchemaMappingAgent()
mapped_df = mapper.map_schema(df)

# Step 2: Validate
validator = ValidationAgent()

is_valid, errors = validator.validate(mapped_df)

if not is_valid:
    print("❌ Validation failed")
    for error in errors:
        print(error)
    exit()

print("✅ Validation passed")

# Step 3: Perform analysis
mapped_df["Difference"] = (
    mapped_df["ActualAmount"] - mapped_df["ExpectedAmount"]
)

mapped_df["Status"] = mapped_df["Difference"].apply(
    lambda x: "OK" if x == 0 else "Mismatch"
)

exceptions = mapped_df[mapped_df["Status"] == "Mismatch"]

# Step 4: LLM analysis
analysis_agent = AnalysisAgent()

analyses = analysis_agent.analyse(exceptions)

# Print results
print("\nAnalysis Results:")

for invoice, analysis in zip(exceptions["Invoice"], analyses):
    print(f"{invoice}: {analysis}")