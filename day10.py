#check memory sharing
import numpy as np
ist=[1,2,3]
arr=np.asarray(ist)
arr[0]=100
print(ist)
#original data
import numpy as np
ist=[10,20,30]
arr=np.asarray(ist)
arr[1]=99
print(ist)
print(arr)
#3d array zeros
import numpy as np
arr=np.zeros((2,3,4))
print(arr)
#fill values later
import numpy as np
arr=np.zeros(5)
arr[:] = [1,2,3,4,5]
print(arr)