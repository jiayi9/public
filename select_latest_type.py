
import pandas as pd
import numpy as np

D = pd.DataFrame({
        "type":["B","B","A", "A","B", "B"],
        "value":[1,2,3,4,5,6]
        })

D

LATEST_TYPE = "B"

i = 1

while D['type'].tolist()[-i] == "B":
    i = i + 1
    
print(i)

new_D = D[-i+1:]

print(new_D)


def retrieve_latest_type(DF, type_column_name, TYPE_NUMBER):
    i = 1
    while DF[type_column_name].tolist()[-i] == TYPE_NUMBER:
        i = i + 1
    if i == 1:
        new_DF = DF
    else:        
        new_DF = DF[-i+1:]
    return(new_DF)
    
retrieve_latest_type(D, 'type', 'B')
