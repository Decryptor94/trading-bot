import pandas as pd
import numpy as np
from tensorflow.keras.models import load_model
from binance.client import Client
from sklearn.preprocessing import MinMaxScaler

# Load the trained model
model = load_model('models/price_prediction_model.h5')

# Binance API credentials
api_key = 'your_api_key'
api_secret = 'your_api_secret'
client = Client(api_key, api_secret)

def predict_price(data):
    # Preprocess data for prediction
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data)
    time_step = 60
    X_test = []
    for i in range(time_step, len(scaled_data)):
        X_test.append(scaled_data[i-time_step:i, 0])
    X_test = np.array(X_test)
    X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)
    
    # Make predictions
    predictions = model.predict(X_test)
    predictions = scaler.inverse_transform(predictions)
    return predictions

def execute_trade(predictions):
    # Trading logic
    # This is a placeholder. Implement your own buy/sell logic based on predictions
    for prediction in predictions:
        current_price = float(client.get_symbol_ticker(symbol="BTCUSDT")['price'])
        if prediction > current_price:
            print("Buy")
        else:
            print("Sell")

# Example usage
if __name__ == "__main__":
    df = pd.read_csv('data/btc_usdt.csv')
    data = df['close'].values.reshape(-1, 1)
    predictions = predict_price(data)
    execute_trade(predictions)
