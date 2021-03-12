import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [2,5,4,7,3,4,1,5,4]

plt.plot(x,y, color='y', linestyle="-.", linewidth=3, marker='^', markersize=13,
         markerfacecolor="green")

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Styling')
plt.show()