import pandas as pd
df=pd.DataFrame({'employee_id':[101,101,102,103,103,103]})
print(df['employee_id'].value_counts()[lambda x:x>=2].index.tolist())
