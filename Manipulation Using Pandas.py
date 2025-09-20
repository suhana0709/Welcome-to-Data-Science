#**********Manipulation using Pandas***************

#importing libraries
import pandas as pd
import numpy as np

data = {'Name':['Pankaj', 'Meghna', 'David', 'Lisa'],
             'Role':['CEO', np.nan, np.nan, np.nan],
             'Salary':[100, 200, np.nan, np.nan]}

labels = ['1.', '2.', '3.', '4']

main = pd.DataFrame(data, index=labels)

print("Data:-\n",main)

print("\nSummary of the basic information bout the data:-\n")
print(main.info())