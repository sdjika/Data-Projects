import pandas as pd
import numpy as np

df = pd.read_csv("dirty_cafe_sales.csv")

# dropped duplicates
df.drop_duplicates(inplace=True)

unknown_placeholders = ["UNKNOWN", "unknown", "?", "N/A", "na", "ERROR"]
df = df.replace(unknown_placeholders, np.nan)

df_cleaned = df.dropna()

print(df_cleaned)