import numpy as np
import matplotlib.pylab as plt

# Data
X = np.array([1,2,3,4,5,6,7,8,9,10])
Y = np.array([30,35,50,55,65,70,-10,85,90,95])

Xmean = X.mean()
Ymean = Y.mean()

numerator = np.sum((X - Xmean) * (Y - Ymean))
denominator = np.sum((X - Xmean) ** 2)

m = numerator / denominator
print(Xmean, Ymean, m)
b = Ymean - m * Xmean
Y_pred = m*X + b


x_new = 12
y_pred = m * x_new + b

print("Slope (m):", m)
print("Intercept (b):", b)
print("Prediction for 12 hours:", y_pred)

plt.scatter(X,Y_pred)
plt.show()
