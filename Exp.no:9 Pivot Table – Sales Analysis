import pandas as pd

df=pd.DataFrame({'Region':['East','East'],
                 'Manager':['A','A'],
                 'Salesman':['X','Y'],
                 'Sale':[100,200]})

print(pd.pivot_table(df,
                     index=['Region','Manager','Salesman'],
                     values='Sale',
                     aggfunc='sum'))
