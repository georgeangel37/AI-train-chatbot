from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
import pickle

with open("model.pickle", 'rb') as f:
    mlp: MLPRegressor = pickle.load(f)

def predict_arival_delay(departure_delay, travel_time):
    x = [[departure_delay, travel_time]]
    return mlp.predict(x)

# print(predict_arival_delay(6, 27))