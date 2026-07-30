import pandas as pd

from src.agents.schema_mapping_agent import SchemaMappingAgent
from src.agents.validation_agent import ValidationAgent


# Sample client CSV
df = pd.DataFrame({
    "Invoice Number": ["INV001"],
    "Gross Amount": [1000],
    "Budget": [900]
})

# Standardize schema
mapper = SchemaMappingAgent()
mapped_df = mapper.map_schema(df)

# Validate
validator = ValidationAgent()

is_valid, errors = validator.validate(mapped_df)

if is_valid:
    print("✅ Validation passed")
else:
    print("❌ Validation failed")
    for error in errors:
        print(error)