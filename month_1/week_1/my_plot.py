# # import matplotlib
# # import matplotlib.pyplot as plt
# # import numpy as np

# # data = np.random.randn(1000)
# # x = [0,1,2,3,4]
# # y = [5, 10,20,25,30]

# # plt.scatter(x,y,
# #             color='blue',
# #             s=100)

# # labels= ['A', 'B', 'C', 'D']
# # values= [10,20,30,40]

# # plt.bar(values, labels)
# # plt.hist(data,bins=10)
# # sizes = [30,40,20,10]

# # plt.pie(sizes,
# #         labels=['A','B','C','D'],
# #         autopct='%1.1f%%'
# #         )


# # fig, ax = plt.subplots(2,2)
# # fig, ax = plt.subplots(2,2)

# # ax[0,0].plot([1,2,3],[4,5,6])
# # ax[0,1].bar([1,2,3],[3,2,1])
# # ax[1,0].scatter([1,2,3],[7,8,9])
# # ax[1,1].hist([1,2,2,3,3,3])
# # labels= ['A', 'B', 'C', 'D']
# # values= [10,20,30,40]
# # values= [0,2,3,4]

# # plt.scatter(values, labels)
# # plt.grid(True)
# # plt.style.use('dark_background')
# # plt.legend()
# # plt.style.use('ggplot')
# # plt.savefig("chart.png")
# # plt.show()

# # import cv2
# # import matplotlib.pyplot as plt

# # img = cv2.imread("Resized.jpg")

# # plt.imshow(img)
# # plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# # x = np.linspace(0, 10, 100)  # Sample data.

# # Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
# # fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
# # ax.plot(x, x, label='linear')  # Plot some data on the Axes.
# # ax.plot(x, x**2, label='quadratic')  # Plot more data on the Axes...
# # ax.plot(x, x**3, label='cubic')  # ... and some more.
# # ax.set_xlabel('x label')  # Add an x-label to the Axes.
# # ax.set_ylabel('y label')  # Add a y-label to the Axes.
# # ax.set_title("Simple Plot")  # Add a title to the Axes.
# # ax.legend() 
# # plt.show()


# def my_plotter(ax, data1, data2, param_dict):
#     """
#     A helper function to make a graph.
#     """
#     out = ax.plot(data1, data2, **param_dict)
#     return out

# data1, data2, data3, data4 = np.random.randn(4, 100)  # make 4 random data sets
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(5, 2.7))
# # my_plotter(ax1, data1, data2, {'marker': 'x'})
# # my_plotter(ax2, data3, data4, {'marker': 'o'})

# # plt.show()


# import matplotlib.pyplot as plt

# # fig, ax = plt.subplots(1, 2, figsize=(5, 2.7))

# # x = [1,2,3]
# # y = [2,4,6]

# # ax[0].plot(x, y)
# # ax[0].set_title("Line Plot")

# # ax[1].bar(x, y)
# # ax[1].set_title("Bar Chart")

# # plt.show()


# fig, ax = plt.subplots(figsize=(5, 2.7))
# x = np.arange(len(data1))
# ax.plot(x, np.cumsum(data1), color='blue', linewidth=3, linestyle='--')
# l, = ax.plot(x, np.cumsum(data2), color='orange', linewidth=2)
# l.set_linestyle(':')
# ax.scatter(data1, data2, s=50, facecolor='C0', edgecolor='k')
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

data1=[1,2,0,4,5]
data2=[0,1,8,3,5]
data3=[1,2,3,4,7]
data4=[1,2,9,4,5]
# fig, ax = plt.subplots(1,2, figsize=(5, 2.7))
# ax[0].plot(data1, 'o', label='data1')
# ax[0].plot(data2, 'd', label='data2')
# ax[1].plot(data3, 'v', label='data3')
# ax[1].plot(data4, 's', label='data4')
# ax[1].plot(data3, data4)
# ax[0].legend()

# plt.show()


# mu, sigma = 115, 15
# x = mu + sigma * np.random.randn(10000)

# print(x.size)
# fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')

# n, bins, patches = ax.hist(x, 50, density=True, facecolor='C1', alpha=1)


# plt.show()


# fig, ax = plt.subplots(figsize=(5, 2.7))

# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2 * np.pi * t)
# line, = ax.plot(t, s, lw=2)

# ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#             arrowprops=dict(facecolor='black', shrink=0.05))

# ax.set_ylim(-2, 2)

# plt.show()


# fig, ax = plt.subplots(figsize=(5, 2.7))
# ax.plot(np.arange(len(data1)), data1, label='data1')
# ax.plot(np.arange(len(data2)), data2, label='data2')
# ax.plot(np.arange(len(data3)), data3, 'd', label='data3')
# ax.legend()


# fig, axs = plt.subplots(1, 2, figsize=(5, 2.7), layout='constrained')
# xdata = np.arange(len(data1))  # make an ordinal for this
# data = 10*data1
# axs[0].plot(xdata, data)

# axs[1].set_yscale('log')
# axs[1].plot(xdata, data)



import numpy as np
import matplotlib.pyplot as plt

# Generate full dataset using NumPy
xdata = np.arange(0, 100, 1)           # values from 0 → 99
data1 = np.sin(xdata * 0.1)            # generate a wave pattern

# Create two vertical subplots
fig, axs = plt.subplots(2, 1, figsize=(8,6), layout='constrained')

# -------- First Plot (Automatic Ticks) --------
axs[0].plot(xdata, data1)
axs[0].set_title('Automatic ticks')
axs[0].set_xlabel("X Values")
axs[0].set_ylabel("Sin Wave")

# -------- Second Plot (Manual Ticks) --------
axs[1].plot(xdata, data1)

# Set custom X ticks
axs[1].set_xticks(
    np.arange(0, 100, 30),
    ['zero', '30', 'sixty', '90']
)

# Set custom Y ticks
axs[1].set_yticks([-1.5, 0, 1.5])

axs[1].set_title('Manual ticks')
axs[1].set_xlabel("Custom X Labels")
axs[1].set_ylabel("Sin Wave")

# Show the figure
plt.show()


