# 小枫
# @Time : 2024/3/20 15:02
# @Author : 小贤 
# @Version :3.11.4
# @IDE : PyCharm 
# @Project : python

# import the numpy
import numpy as np
'''benifit of numpy'''
# define
arr = np.arange(1, 6)
# output
print(arr)
# set computation
lst = [1, 2, 3, 4, 5]
# first way
# for i in range(len(lst)):
#     lst[i] += 1
# print(lst)

# second way
lst = [i+1 for i in lst]
print(lst)

# when we use numpy
arr = np.arange(1, 6)
print(arr + 1)
print(arr)

# %timeit is a code for running code 7times and compute the average time of every times
# %timeit
a = list(range(10000))
b = np.array(a)

# the object we deal with
''' ndarray define'''
c = [1, 2, 3, 4, 5]
c2 = [[1, 2, 3],
      [4, 5, 6]
     ]
arr1 = np.array(c)
arr2 = np.array(c2)
print('arr1', arr1)
print(arr2)

c3 = [[[1, 2, 3], [4, 5, 6]],
      [[7, 8, 9], [10, 11, 12]]
      ]
arr3 = np.array(c3)
print('arr3')
print(arr3)

'''property of array'''
# 1 check the shape
print(arr1.shape)
print(arr2.shape)  # the mean is 2d array, 2row, every row 3 elements.
print(arr3.shape)

# 2 check the dimension
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

# 3 check the number of elements
print(arr2.size)
print(arr3.size)

# 4 size of every element
print(arr2.itemsize)
print(arr3.itemsize)

# 5 type of elements
print(arr2.dtype)

""" the type of element in array"""
# 1 define dtype with int8 and find its itemsize
d = np.array([1, 3, 5, 7, 9], dtype=np.int8)
print(d.itemsize, d.dtype)
e = np.array([1, 3, 5, 7, 9], dtype=np.int64)
print(e.itemsize, e.dtype)
f = np.array([1, 3, 5, 7, 9], dtype='f8')
print(f.itemsize, f.dtype)

lst = list('abcd')
g = np.array(lst)
print(g.itemsize, g.dtype)  # S represent the str, U is unicode

str1 = np.array(['Numpy', 'pandas', 'matplotlib', 'python'], dtype=np.string_)
print(str1.dtype)
print(str1.itemsize)

# 2 modify the type
h = f.astype('i8')  # int - float but they are identical
print(h.dtype, h.itemsize)
noi = e.astype(np.float16)
print(noi)
j = f.astype(np.float16)
print(j)
k = np.array([1.2, 3.14, 55, 8])
print(k)
print(k.dtype, k.itemsize)
m = k.astype('i4')
print(m)  # when we change the high float to low int
n = np.array(['1', '2', '3']).astype('f2')
print(n)

# tolist()  to make the array to the list
o = k.tolist()
print(o)
print(type(o))
print(type(k))
print(k.tostring())
p = k.tobytes()
print(p)

'''the data passing to down'''
# in the ndarray structure all element must be the same type
# aj = [1, 2, 3, 4]
aj = [1, False, 3.5, 4, 'str']
ajry = np.array(aj)
print(ajry.dtype)  # if there are not the same, the type will pass in low level
'''conclusion for above the '''
# the False or True > int > flot > str

# z66 = ajry.astype('f2')
# print(z66.dtype)
# print(z66) # i can undstand how I can't not astype the str

ajk = [1, False, 3.5, 4, 'str']
ajkry = np.array(ajk,dtype=np.object_)
print(ajkry.dtype)
print(ajkry*2)
