import numpy as np
import pandas as pd 

def header(msg):
    print('-'*50)
    print('[' + msg + ']')

file_name = 'titanic.csv'
df = pd.read_csv('titanic.csv')
print(df)

