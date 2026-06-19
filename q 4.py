import pandas as pd
import matplotlib.pyplot as plt

df=pd.DataFrame({'Date':['D1','D2','D3'],
                 'Close':[140,145,143]})

plt.plot(df['Date'],df['Close'])
plt.show()
