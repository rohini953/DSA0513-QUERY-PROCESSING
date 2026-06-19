import pandas as pd
import numpy as np

df=pd.DataFrame([[1,np.nan,np.nan],
                 [1,2,3],
                 [np.nan,np.nan,5]])

print(df[df.isnull().sum(axis=1)>=2])
