import pandas as pd
df = pd.read_json('dataETL.json')
print(df.to_string()) 