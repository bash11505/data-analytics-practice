#np.transpose
import numpy as np 
arr = np.array([[1,2,3]])
result = np.transpose(arr)
print(result)
#arr.T
import numpy as np 
arr = np.array(([1,2],
                  [3,4]))
print(arr.T)
#np.swapaxes
import numpy as np 
arr = np.array([[[1,2],[3,4]]])
result = np.swapaxes(arr,0,1)
print(result)
#np.moveaxis
import numpy as np
arr = np.ones((2,3,4))
result = np.moveaxis(arr, 0, 2)
print(result.shape)
#np.squeeze
import numpy as np
arr = np.array([[[1,2,3]]])
result = np.squeeze(arr)
print(result)
print(result.shape)
#np.expand_dims()
import numpy as np
arr = np.array([1,2,3])
result = np.expand_dims(arr, axis=0)
print(result)
print(result.shape)