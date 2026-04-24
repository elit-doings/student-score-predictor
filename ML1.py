import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

x = np.array([[1], [2], [3], [4], [5]])
y = np.array([40, 50, 60, 70, 80])


doings = LinearRegression()

doings.fit(x, y)

with open("doings.pkl", "wb") as f:
    pickle.dump(doings, f)

print('Model trained and saved!')
