import pandas as pd
import numpy as np

df=pd.DataFrame(np.random.randn(10,4))
df.iloc[0,0]=np.nan
df.iloc[2,1]=np.nan

df.style.applymap(lambda x:'background:yellow' if pd.isna(x) else '')
