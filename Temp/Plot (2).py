import matplotlib.pyplot as plt
import numpy as np
x=np.arange(2,12,1)
y=x**2
ax=plt.subplots()
ax.stem(x,y)
plt.show()
