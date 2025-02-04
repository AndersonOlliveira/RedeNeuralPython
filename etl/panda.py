import pandas as pd
dfData = pd.read_csv(r"C:\PATH\etl.csv", nrows=500000)
print(dfData.head())
dfData.describe()
dfData.info()
dfData.memory_usage()
dfData.count()
dfData.isnull()
dfData.isna()