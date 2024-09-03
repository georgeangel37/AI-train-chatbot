import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from math import sqrt
import pickle

data = pd.read_csv("data.csv")

data = data.dropna()

y_data = data.iloc[:, 5]
x_data = data.iloc[:, [3, 4]]

scaler = StandardScaler()
scaler.fit(x_data)
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.5, random_state=1)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
mlp = MLPRegressor(hidden_layer_sizes=20, solver='sgd', max_iter=10000, activation='logistic', random_state=0, learning_rate_init=0.001, verbose=True, momentum=0.9, tol=0.0001, early_stopping=False)
mlp.fit(x_train, y_train)
y_guess = mlp.predict(x_test)
print(f"R²: {r2_score(y_test, y_guess)}")
print(f"Root Mean Squared Error: {sqrt(mean_squared_error(y_test, y_guess))}")
print(f"Mean Absolute Error: {mean_absolute_error(y_test, y_guess)}")


with open("model.pickle", 'wb') as f:
    pickle.dump(mlp, f)