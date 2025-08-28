import numpy as np

database = np.loadtxt('space.csv', delimiter = ';', dtype = str, encoding = 'utf-8');
##print(database);
cost = database[:,6];
costf = cost.astype(float);
print(np.sum((cost.astype(float))));
