import matplotlib.pyplot as plt
import numpy as np

# fig , ax = plt.subplots(figsize=(8, 4))
# x = np.linspace(0,10,100)
# y = np.sin(x)

# print(x)
# print(y)
# ax.plot(x,y, label='Sin Wave' , color="blue")
# ax.set_title("My First Professional Plot")
# ax.set_xlabel("Time")
# ax.set_ylabel("Amplitude")

# ax.legend()
# plt.show()


# fig , (ax, ax1) = plt.subplots(2,1, figsize=(10, 7))

# x = np.linspace(1,20,200)
# y = np.sin(x)
# ax.plot(x, y, color='red')
# ax.set_title("Plot 1")
# ax.grid()
# ax.axis('tight')

# ax1.plot(['A', 'B', 'C'], [5, 20, 8], color='purple',linestyle='--',linewidth=1.5,alpha=1,label='Projected Goal')
# ax1.set_title("Plot 2")

# ax2.pie(['A', 'B', 'C'], [5, 20, 8], color='red',)
# ax2.set_title("Pie Chart")

# # plt.tight_layout()
# fig.savefig('plot.png')
# plt.show()


# labels = ['Python', 'Java', 'C++', 'JavaScript']
# sizes = [45, 25, 15, 15] 
# colors = ['#377eb8', '#ff7f00', '#4daf4a', '#f781bf'] 
# explode = (0.1, 0, 0, 0) 

# # 2. Setup Figure
# fig, ax = plt.subplots(figsize=(8, 6))

# # 3. Create the Pie Chart
# ax.pie(sizes, 
#        explode=explode,    
#        labels=labels,       # Text labels for slices
#        colors=colors,       # Custom color palette
#        autopct='%1.1f%%',
#        shadow=True,         # Adds a subtle 3D shadow
#        startangle=140
#        )      # Rotates the start of the chart

# # 4. Final Touches
# ax.set_title("Programming Language Popularity", fontsize=14)

# plt.show()


# header = "Day,Sales,Expenses,Customers"
# data = np.array([
#     [1, 200, 150, 50], [2, 220, 160, 55], [3, 210, 155, 52],
#     [4, 250, 180, 70], [5, 280, 190, 85], [6, 310, 200, 95],
#     [7, 300, 195, 90]
# ])

# np.savetxt('business_data.csv', data, delimiter=',', header=header, comments='')


# Load data (ensure busines_data.csv exists in your directory)
# dtype=None allows NumPy to guess types (like strings for 'Days')


# data = np.genfromtxt('business_data.csv', delimiter=',', names=True, dtype=None, encoding='utf-8')

# days = data['Day']
# sales = data['Sales']
# expenses = data['Expenses']
# customers = data['Customers']
# profit = sales - expenses

# # 1. FIXED: Changed plt.figure to plt.subplots
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
# fig.suptitle("Weekly Business Performance Dashboard", fontsize=20, fontweight='bold', y=0.98)

# # Ax1: Revenue vs Costs
# ax1.plot(days, sales, 'o-', color='green', label='Sales')
# ax1.plot(days, expenses, 's--', color='red', label='Expenses')
# ax1.set_title("Revenue vs Costs")
# ax1.grid(alpha=0.3)
# ax1.legend()

# ax2.fill_between(days, profit, color='skyblue', alpha=0.4)
# ax2.plot(days, profit, color='blue', marker='d', label='Profit')
# ax2.set_title("Daily Profit Margin")
# ax2.legend()

# ax3.bar(days , customers , color='orange', alpha=0.7)
# ax3.set_title("Daily Customer Count")

# ax4.scatter(sales, expenses, color="purple", s=100)
# ax4.set_title("Sales vs. Expenses Correlation")
# ax4.set_xlabel("Sales")
# ax4.set_ylabel("Expenses")

# plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to make room for suptitle
# plt.show()



# from matplotlib.animation import FuncAnimation

# fig, ax = plt.subplots()
# x_data, y_data = [], []
# ln, = ax.plot([], [], 'r-')

# def init():
#     ax.set_xlim(0, 2*np.pi)
#     ax.set_ylim(-1, 1)
#     return ln,

# def update(frame):
#     x_data.append(frame)
#     y_data.append(np.sin(frame))
#     ln.set_data(x_data, y_data)
#     return ln,

# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128),
#                     init_func=init, blit=True)
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Apply a professional theme
plt.style.use('seaborn-v0_8-whitegrid')

# 1. Generate Data
x = np.linspace(0, 10, 50)
y = np.exp(x/3) + np.random.normal(0, 1, 50)

# 2. Create Layout
fig, ax = plt.subplots(figsize=(10, 6))

# 3. Plot with specific styles
ax.plot(x, y, color='#4C72B0', lw=3, label='Server Load')
ax.fill_between(x, y, color='#4C72B0', alpha=0.2) # Area chart style

# 4. Custom Formatting
ax.set_title("System Performance Analysis", loc='left', fontsize=18, pad=20)
ax.set_ylabel("Memory Usage (GB)")
ax.set_xlabel("Uptime (Hours)")

# 5. Annotation: Highlight a Spike
# peak_idx = np.argmax(y)
# ax.annotate('Critical Peak', 
#             xy=(x[peak_idx], y[peak_idx]), 
#             xytext=(x[peak_idx]-2, y[peak_idx]+5),
#             arrowprops=dict(arrowstyle='->', lw=2),
#             fontweight='bold')

# 6. Save Export
plt.tight_layout()
plt.show()