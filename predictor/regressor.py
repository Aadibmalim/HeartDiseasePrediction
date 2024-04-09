
# Importing libraries 
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings("ignore")


class LogitRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.W = None
        self.b = None

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, Y):
        self.m, self.n = X.shape
        self.W = np.zeros(self.n)
        self.b = 0
        self.X = X
        self.Y = Y

        for i in range(self.iterations):
            self.update_weights()

    def update_weights(self):
        if self.W is None or self.b is None:
            raise ValueError("Weights and bias should be initialized before updating.")

        Z = np.dot(self.X, self.W) + self.b
        A = self.sigmoid(Z)

        tmp = A - self.Y
        dW = np.dot(self.X.T, tmp) / self.m
        db = np.sum(tmp) / self.m

        self.W = self.W - self.learning_rate * dW
        self.b = self.b - self.learning_rate * db

    def predict(self, X):
        if self.W is None or self.b is None:
            raise ValueError("Weights and bias should be initialized before predicting.")

        Z = np.dot(X, self.W) + self.b
        A = self.sigmoid(Z)
        Y_pred = np.where(A > 0.5, 1, 0)

        return Y_pred, A
    


def find():
    df = pd.read_csv(r"C:\Users\aadib\OneDrive - Zeetech\Desktop\project - Copy\predictor\heart[1].csv")
    X = df.iloc[:, :-1].values
    Y = df.iloc[:, -1].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

   

    # Split the data into training and testing sets
    X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=0)

    # Create and train the Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    # Make predictions on the test set
    Y_pred = model.predict(X_test)

    return X_scaled, Y

    

    
  

