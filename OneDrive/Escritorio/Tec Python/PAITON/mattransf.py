import numpy as np
import matplotlib.pyplot as plt


A1=np.array([[0.5,0],[0,2]])
M=np.array([[0,0.5,1,0],[0,1,0,0]])

plt.plot(M[0],M[1],'-o')
plt.axis('equal')
plt.show()

A2=np.array([[1,0],[0,-1]])
W=np.matmul(A2,np.matmul(A1,M))
plt.plot(W[0],W[1],'-o')
plt.axis('equal')
plt.show()