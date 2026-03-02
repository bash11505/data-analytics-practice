#dtype
import numpy as np  
arr = np.array([1,2,3,4,5,6,7,8,9])
print(arr.dtype)
#2nd programme
import numpy as np 
arr = np.array(['apple','bannana','orange'])
print(arr.dtype)
#itemsize programme
import numpy as np 
arr = np.array([1,2,3,4,5],dtype='S')
print(arr)
#4thprogramme
import numpy as np
arr = np.array([1.0, 2.0], dtype=np.float64)
print(arr.itemsize)
#nbytes programme
import numpy as np
arr = np.array([1, 2, 3, 4], dtype=np.int32)
print(arr.nbytes)
#6th programme
import numpy as np
arr = np.array([[1.0, 2.0], [3.0, 4.0]])
print(arr.nbytes)