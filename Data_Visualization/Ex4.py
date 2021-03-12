import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0.0,10.0)
y1 = np.sin(x1)

x2 = np.linspace(0.0,10.0)
y2 = np.cos(2*np.pi*x2)*np.exp(-x2)

plt.subplot(2,1,1)
plt.plot(x1,y1)
plt.subplot(2,1,2)
plt.plot(x2,y2)

plt.show()