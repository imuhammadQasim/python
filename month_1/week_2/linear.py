import numpy as np
import matplotlib.pylab as plt
import pandas as pd


data = pd.read_csv('./data/house_prices_practice.csv')

class LinearRegressionModel:
    def __init__(self, learning_rate, iterations):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.theta = None
        self.cost_history = []