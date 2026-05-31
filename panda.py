#Getting used to this
import pandas as pd
"""creating a simple dataset"""
data = {
  'fruits': ['apple','banana', 'orange', 'date'],
  'quantity': [10, 20, 15,25],
  'price': [1.20, 0.60, 2.30,2.40],
  'in_stock': [True,False,True,True]
}

"""loading data into a dataframe"""
df = pd.DataFrame(data)
"""displaying the dataframe"""
print(df)

"""performing a simple math operation"""
print("\n--- summary statistics for price ---")
print(f"average fruit price: ${df['price'].mean():.2f}")