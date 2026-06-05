# speed 
import time
l = list(range(1000000))
start = time.time()
res = [x * 2 for x in l]
list_time = time.time()-start
print(list_time)

import numpy as np
a = np.arange(1000000)
start = time.time()
res = a * 2
np_time = time.time()- start
print(np_time)

import numpy as np
arr = np.array([1,2,3,4,5])
print(arr)



zeros = np.zeros((2,3),dtype=int)
print(zeros)
ones = np.ones((2,3),dtype=int)
print(ones)
range_arr = np.arange(10)
print(range_arr)

arr = np.linspace(0,1,5)
print(arr)
den = np.eye(4)
print(den)
rand = np.random.randint(1,100,size=(3,3))
print(rand)
# array attributes and indexing
arr = np.array([[10,20,30,],[40,50,60,],[70,80,90,]])
print(arr.shape)
print(arr.size)
print(arr.ndim)

# slicing and indexing
print(arr[2:,0:])
print(arr[0:,1:])
print(arr[1:,2:])

print(arr[2,0])
print(arr[0,1])
# mathematical operations
a = np.array([1,2,3])
b= np.array([4,5,6])
add = a+b
print(add)
sub = a-b
print(sub)
mul = a*b 
print(mul)
print(np.sqrt(a))
print(np.sum(a))

# min max mean median_arr std axis=0
arr1 = np. array([[10,20,30,40],
                  [50,50,60,70,]])

print(np.min(arr1))
print(np.max(arr1,))
print(np.mean(arr1))
print(np.median(arr1))
print(arr1.flatten())


print(np.unique(arr1))
print(np.sum(arr1,axis=0))
print(np.std(arr1,axis=1))
# broadcasting & reshaping
scalar_arr1 = arr1 + 10
print(scalar_arr1)

arr1 = np.arange(12)
reshape = arr1.reshape(3,4)
print(reshape)

import numpy as np
c = np.array([3,4,5,6])
d = np.array([7,8,9,0])
con_1 = np.concatenate((c,d))
print(con_1)
print(np.vstack((c,d)))
print(np.hstack((c,d)))


k = np.array([1,2,3,7,5,6])
print(np.split(k,3))
print(np.sort(k))


arr = np.arange(10)
filter = arr[arr>5]
print(filter)


h = np.array([[1,2],[3,4]])
p = np.array([[5,6],[9,9]])
result = np.dot(h,p)
print(result)
























