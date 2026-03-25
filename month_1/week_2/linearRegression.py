import numpy as np
import matplotlib.pylab as plt
import pandas as pd
# # Data
# X = np.array([1,2,3,4,5,6,7,8,9,10])
# Y = np.array([30,35,50,55,65,70,-10,85,90,95])

# Xmean = X.mean()
# Ymean = Y.mean()

# numerator = np.sum((X - Xmean) * (Y - Ymean))
# denominator = np.sum((X - Xmean) ** 2)

# m = numerator / denominator
# print(Xmean, Ymean, m)
# b = Ymean - m * Xmean
# Y_pred = m*X + b


# x_new = 12
# y_pred = m * x_new + b

# print("Slope (m):", m)
# print("Intercept (b):", b)
# print("Prediction for 12 hours:", y_pred)

# plt.scatter(X,Y_pred)
# plt.show()


# data = pd.read_csv('./data/real_estate.csv', index_col=0, nrows=100)

# data['sqft'] = data['sqft'].fillna(data['sqft'].median())
# data['listPrice'] = data['listPrice'].fillna(data['listPrice'].median())
# x = data['sqft'].values
# y = data['listPrice'].values

# x_mean= np.mean(x)
# y_mean= np.mean(y)
# m = np.sum((x-x_mean)*(y-y_mean))/np.sum((x-x_mean)**2)
# b = y_mean - x_mean* m

# y_pred = m*x+ b

# x = (x - np.mean(x)) / np.std(x)

# m= 0
# b = 0

# learning_rate = 0.1
# epochs = 10000
# n = len(x)
# for i in range(epochs):
#     y_pred = m * x + b

#     dm = (-2/n) * np.sum(x* (y-y_pred))
#     db = (-2/n) * np.sum(y - y_pred)

#     m = m- learning_rate * dm
#     b = b- learning_rate * db

#     if i %100 ==0:
#         loss = np.mean((y - y_pred)**2)
#         print(f"Epoch {i}, Loss: {loss}")

# y_pred = m * x + b


# x = (x - np.mean(x))/np.std(x)

# m = 0 
# b = 0 

# learning_rate = 0.1
# n = len(x)
# epochs = 1000

# for i in range(epochs):
#     y_pred = m *x +b

#     dm = (-1/n)* np.sum(x * (y-y_pred))
#     db = (-1/n) * np.sum(y-y_pred)

#     m = m - learning_rate * dm
#     b = b - learning_rate * db


#     if i %100 ==0:
#         loss = np.mean((y-y_pred)**2)
#         print(f'Epoch {i}, Loss: {loss}')

# y_pred =m *x + b


# feature = ['sqft' , 'beds', 'baths' , 'garage', 'year_built']

# x = data[feature]
# x = x.fillna(x.median())

# y = data['listPrice'].fillna(data['listPrice'].mean()).values

# x = (x-np.mean(x))/np.std(x)
# x= x.values
# n_samples, n_features = x.shape

# print(type(n_features) , n_features)
# w = np.zeros(n_features)
# b = 0 
# learning_rate = 0.01
# epochs = 1000
# losses = []
# for i in range(epochs):
#     y_pred = np.dot(x, w) + b

#     error = y-y_pred
#     losses.append(error)

#     dw = (-2/n_samples) * np.dot(x.T , error)
#     db = (-2/n_samples) * np.sum(error)

#     w = w- learning_rate * dw
#     b = b - learning_rate * db

#     if i % 100 == 0:
#         loss = np.mean(error**2)
#         print(f"Epoch {i}, Loss: {loss}")

# y_pred = np.dot(x, w)+ b



# plt.scatter(x,y, color="red", label="Data Points")
# # plt.plot(x,y, color="green", label="Linear Regression")
# plt.plot(x,y_pred, color="blue", label="Linear Regression")
# plt.title('Linear Regression of sqft and price data')
# plt.legend()
# plt.show()

# plt.scatter(data['sqft'], y, label="Actual", alpha=0.6)
# plt.plot(data['sqft'], y_pred, color="red" ,label="Predicted", alpha=0.6)

# plt.plot(losses, label="lr=0.01")
# plt.legend()

# plt.xlabel("Iterations")
# plt.ylabel("Loss (MSE)")
# plt.title("Loss Curve (Gradient Descent)")

# plt.show()

data = pd.read_csv('./data/student.csv', nrows=100)
print(data)
# Select features
features = ['Hours_Studied', 'Attendance']
x = data[features].fillna(data[features].mean()).values

# Target variable
y = data['Exam_Score'].fillna(data['Exam_Score'].mean()).values

x_mean = x.mean(axis=0)
x_std = x.std(axis=0)
x_scaled = (x-x_mean)/x_std

n_sample , n_feature = x_scaled.shape

print(n_sample, n_feature)

w = np.zeros(n_feature)
b = 0 

learning_rate = 0.01
epochs = 1000
losses =[]

for i in range(epochs):
    y_pred = np.dot(x_scaled, w) + b
    loss = y-y_pred

    dw =(-2/n_sample) * np.dot(x_scaled.T, loss)
    db =(-2/n_sample) * np.sum(loss)

    w = w- learning_rate * dw
    b = b- learning_rate * db

    losses.append(loss)

    if i % 100 == 0:
        print(f"Epoch {i}, Loss: {losses[-1]}")

y_pred = np.dot(x, w) + b

mse = (1/2*n_sample) * np.sum((y- y_pred)**2)
rmse = np.sqrt(mse)


print("\nTest set evaluation:")
print(f"MSE: {mse:.2f}, RMSE: {rmse:.2f}")
      
plt.plot(losses)
plt.xlabel("Iterations")
plt.ylabel("Loss (MSE)")
plt.title("Loss Curve")
plt.show()

# --------------------------
# 8️⃣ Plot Actual vs Predicted
# --------------------------
plt.scatter(y, y_pred)
plt.xlabel("Actual Exam Score")
plt.ylabel("Predicted Exam Score")
plt.title("Actual vs Predicted Exam Scores")
plt.show()