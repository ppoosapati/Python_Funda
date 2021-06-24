import pandas as pd
import numpy as np

# np.array/np.ndarray
# pd.series
# pd.dataframe

# array
#my_numpy_array = np.random.rand(3)
my_np_array = [1,2,3]
#print (my_numpy_array)
print (my_np_array)

# series 
#series = pd.Series(my_numpy_array, index = ["first", "second", "third"])
#print (series)

# dataframe 
#my_panda_df = pd.DataFrame([np.random.rand(3,2)])
man_df = pd.DataFrame([1,'x'], [2,'y'], [3,'z'])
#print (my_panda_df)
print (man_df)

#my_panda_df.columns = ("first","second")
man_df.columns = ("first","second")
#print(my_panda_df)
print(man_df)