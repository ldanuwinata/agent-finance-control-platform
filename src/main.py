import pandas as pd

print ("Welcome to the Agentic Finance Control Platform!")

data = {
    "Invoice": [1001, 1002, 1003],
    "Fund": ["Fund A", "Fund B", "Fund C"],
    "Amount": [25000, 18000, 42000],
    
}

df = pd.DataFrame(data)

print(df)
