import numpy as np
print("importing done")
multi_arr=[
 [1,2,3],
 [4,5,6]
]
multi_np =np.arry(multi_arr)
rows,cols = multi_np.shape
print(row,col)
reshaped_np_arr=multi_np.reshape((3,2))
print(reshaped_np_arr)
