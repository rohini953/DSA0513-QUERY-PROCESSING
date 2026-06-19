import pandas as pd

df=pd.DataFrame({'school':['S1','S2','S1'],
                 'age':[10,12,11]})

g=df.groupby('school')
print(type(g))
