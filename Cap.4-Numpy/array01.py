import numpy as np;

array = np.array([10,20,30]);
print("1d array:",array);

array02 = np.array([[10,20,30],[40,50,60]]);

print("2d array: ",array02);
print("2d array type: ",type(array));

#Functions to structure numpy array
array = np.ones(10);
print(array);

array02 = np.zeros(10).reshape(5,2);
print(array02);

##Arrange
array = np.arange(10,31,10);
print(array);

#Nupy operations
array = np.arange(1, 10, 1);
array02 = np.arange(9, 0, -1);

print("array com arange crescente:   ", array);
print("array com arange decrescente: ", array02);

print(array02+array);

print("array concatenado: ", np.concatenate([array02,array]))

##Operations with Matrix
array02 = np.array([50,10,60,100,25,100,75,80,100]).reshape(3,3);

print(array02);

np.random.seed(10);
array = np.random.randint(1,101,10);
print(array);