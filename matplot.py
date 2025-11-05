import matplotlib.pyplot as plt
import  numpy as np

x=np.array([1,2,6,8])
y=np.array([3,2,1,8])

z=np.array([1,2,5,2])
plt.plot(x,color='r')
plt.plot(y,color='y')

plt.grid()
plt.show()