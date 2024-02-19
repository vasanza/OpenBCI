#%%
import pandas as pd 
import matplotlib.pyplot as plt


df = pd.read_csv('C:/Users/danie/Documents/BCI Data Collection/Datacollected_method_1/S02R1M7_2.csv')
print(df)
 #Leer documento
#canal='9'
#print(df[canal])
for i in range(0,8):
    plt.plot(df[str(i)])
    plt.show()
# %%
