#np.reshape
import numpy as np 
arr=np.array([1,2,3,4,5,6,7,8,9])
new_arr=arr.reshape(3,3)
print(new_arr)
#arr.flatten
import numpy as np 
arr=np.array([[1,2,3],
              [4,5,6]])
flattened_arr=arr.flatten()
print(flattened_arr)
#arr.revel
import numpy as np 
arr = np.array([[1,2,3],
              [4,5,6]])
new_arr=arr.reshape(-1)
print(new_arr)
#arr.resize
import numpy as np 
arr = np.array([1,2,3,4,])
new_arr=np.resize(arr,(3,3))
print(new_arr)