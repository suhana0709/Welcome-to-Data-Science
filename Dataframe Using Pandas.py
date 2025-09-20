#**********DataFrame using Pandas***************

#importing libraries
import pandas as pd
import numpy as np

exam_data = {'Name':['Harry', 'Hermione', 'Ron', 'Fred', 'George', 'Draco', 'Voldemort', 'Albus', 'Aeberforth', 'Snape'],
             'Score':[8.5, 10, 5.5, 4, np.nan, 9, 10, np.nan, 5, 10],
             'Attempts':[2, 1, 3, 1, 1, 2, 1, 2, 3, 1],
             'Qualify':['yes', 'yes', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes']}

labels = ['a.', 'b.', 'c.', 'd.', 'e.', 'f.', 'g.', 'h.', 'i.', 'j.']

main = pd.DataFrame(exam_data, index=labels)

print("Exam Datas:-\n",main)

print("\nSummary of the basic information bout the data:-\n")
print(main.info())