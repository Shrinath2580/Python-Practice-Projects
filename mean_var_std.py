# %%
import pandas as pd
import numpy as np
import sys
import math

def calculate(elements: list):
    rows = 3
    columns = 3

    try:
#   Printing the matrix given by the user
        matrixx = np.array(elements).reshape(rows,columns)
                       
        
        mean = matrixx.mean(0).tolist(), matrixx.mean(1).tolist(), matrixx.mean().tolist()
        
        variance = matrixx.var(0).tolist(), matrixx.var(1).tolist(), matrixx.var().tolist()
        
        standard_deviation = matrixx.std(0).tolist(), matrixx.std(1).tolist(), matrixx.std().tolist()
        
        max = matrixx.max(0).tolist(), matrixx.max(1).tolist(), matrixx.max().tolist() 
        
        min = matrixx.min(0).tolist(), matrixx.min(1).tolist(), matrixx.min().tolist()
                        
        sum = matrixx.sum(0).tolist(), matrixx.sum(1).tolist(), matrixx.sum().tolist()
        
        Res = {"mean" : mean,"variance" : variance, "Standard Deviation" : standard_deviation,"max" : max,"min" : min, "sum" : sum}
        
        for key, value in Res.items():
            print(key, ':', value)
        
        
        
    except ValueError:
        print("List must contain nine numbers.")
        
calculate([0,1,2,3,4,5,6,7,8])

# %%



