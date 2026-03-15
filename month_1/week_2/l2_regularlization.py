import random
import numpy as np
import matplotlib.pyplot as plt
from model_utils import *


train_X = np.loadtxt('train_x.csv' , delimiter=',')
train_Y = np.loadtxt('train_y.csv' , delimiter=',').reshape(1, train_X.shape[1])
print("File loaded!")
test_X = np.loadtxt('test_x.csv' , delimiter=',')
test_Y = np.loadtxt('test_y.csv' , delimiter=',').reshape(1, test_X.shape[1])

print('shape of train x',np.shape(train_X))
print('shape of train y',np.shape(train_Y))
print('shape of Test x',np.shape(test_X))
print('shape of Test y',np.shape(test_Y))


plt.scatter(train_X[0], train_X[1], c=train_Y[0])
plt.show()


def model(X,Y, layer_dims, learning_rate=0.3, num_iterations = 20000):
    grad= {}
    cost_list=[]
    m=X.shape[1]

    parameters=initialize_parameters(layer_dims)

    for i in range(0, num_iterations):
        a3 ,cache =  forward_propagation(X, parameters)
        cost = cost_function(a3, Y)

        grads = backward_propagation(X, Y, cache)
        
        parameters = update_parameters(parameters, grads, learning_rate)
        
        if (i%1000 == 0):
            print("Cost after iteration ", i, " is : ", cost)
            cost_list.append(cost)
    
    # plot the cost
    plt.plot(cost_list)
    plt.ylabel('cost')
    plt.xlabel('iterations')
    plt.show()
    
    return parameters

learning_rate = 0.3
num_iterations = 20000 + 1
layers_dims = [train_X.shape[0], 100, 10, 1]
parameters = model(train_X, train_Y, layers_dims, learning_rate, num_iterations)


learning_rate = 0.3
num_iterations = 20000 + 1
layers_dims = [train_X.shape[0], 100, 10, 1]
parameters = model(train_X, train_Y, layers_dims, learning_rate, num_iterations)

accuracy(train_X, train_Y, parameters, "Train")
accuracy(test_X, test_Y, parameters, "Test")

plt.title("For Training Dataset")
plot_decision_boundary(lambda x: predict_dec(parameters, x.T), train_X, train_Y)

plt.title("For Test Dataset")
plot_decision_boundary(lambda x: predict_dec(parameters, x.T), test_X, test_Y)