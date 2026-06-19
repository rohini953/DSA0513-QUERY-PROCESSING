import pandas as pd

df=pd.DataFrame({'Item':['Pen','Book','Pen'],
                 'Units':[5,3,2]})

print(pd.pivot_table(df,index='Item',
                     values='Units',
                     aggfunc='sum'))
