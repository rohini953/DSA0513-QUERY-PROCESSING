import pandas as pd

df=pd.DataFrame({'Item':['Pen','Pen','Book'],
                 'Sale':[100,150,200]})

print(pd.pivot_table(df,index='Item',
                     values='Sale',
                     aggfunc=['max','min']))
