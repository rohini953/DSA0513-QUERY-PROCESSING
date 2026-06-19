import pandas as pd

df=pd.DataFrame({'Name':['Alex','JOHN']})
print(df['Name'].str.swapcase())
