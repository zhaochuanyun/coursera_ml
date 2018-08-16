import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('ex1data1.txt')

x = np.array([
    [1,2,3],
    [4,5,6]
])

y = [
    [1,2],
    [3,4],
    [5,6]
]

print(np.dot(x, y))

def computeCostFunction(X, y, theta):
    np.dot(X, theta)
