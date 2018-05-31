
import matplotlib.pyplot as plt
import numpy as np


path = "/Users/martin/Desktop/Cours/Advanced Computing techniques 2018/Project/"
filename = "results.csv"
dtype = (object,9)
date = np.genfromtxt(path+ filename, delimiter=",", skip_header=1, dtype =dtype, encoding=None,usecols=range(9))

n = len(X[:,0])

for i in range(n):

    print (X[i,-1])

    if X[i,-1] == b'TRUE':
        X[i,-1] = 1
    elif X[i,-1] == b'FALSE':
        X[i, -1] = 0

    else:
        print ("Error")

print(X[1,:])