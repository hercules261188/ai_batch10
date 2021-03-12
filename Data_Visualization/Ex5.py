import matplotlib.pyplot as plt

x1 = [1,2,3,4,5]
y1 = [10,18,24,35,40]

label = ["Jan","Feb","Mar","Apr","May"]

plt.bar(x1,y1, tick_label=label, color=['r','g','y'])
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Bar Graph")

plt.show()
