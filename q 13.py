import pandas as pd
import numpy as np

df=pd.DataFrame([[1,np.nan],[3,4]])
print(df.isnull())
