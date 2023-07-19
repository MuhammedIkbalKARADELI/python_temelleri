import numpy as np



# python list 
py_list = [1,2,3,4,6,7,8,9] # bu bir python listesidir.

# numpy array(dizisi)
np_array = np.array([1,2,3,4,5,6,7,8,9])  # array dizisi oluşturur normalde python da list var ama dizi yok burda bu lib ile dizi oluşturuyoruz.

print(type(py_list)) # <class 'list'>
print(type(np_array)) # <class 'numpy.ndarray'>


py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3) # 3*3 bir matris oluşturyoruz.

print(py_multi)
print(np_multi)


print(np_array.ndim)  # dizinin boyutunu bize verir.
print(np_multi.ndim)

print(np_array.shape)  # burda bize diznin shapini verir. (9,0) gibi
print(np_multi.shape)  # (3,3) matris olduğunu söyler bize




    
