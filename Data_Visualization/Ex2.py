import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [4,2,1,1,5]

plt.plot(x1,y1, label="Line-1")

x2 = [1,2,3,4,5]
y2 = [3,4,1,2,5]

plt.plot(x2,y2, label="Line-2")
plt.legend()
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Multiple Line Graph")
plt.show()