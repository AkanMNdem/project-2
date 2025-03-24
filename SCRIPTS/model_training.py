import os
from data_preprocessing import load_and_prepare_all
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

def train_and_predict(df, symbol='TICKER'):
    # Filter training and testing periods
    train_df = df[(df.index >= '2015-01-01') & (df.index <= '2020-01-31')]
    test_df  = df[df.index >= '2020-04-01']

    # Prepare feature (month index) and target (close price)
    train_X = train_df[['month']].values
    train_y = train_df['close'].values
    test_X = test_df[['month']].values
    test_y = test_df['close'].values

    # Fit and predict
    model = LinearRegression()
    model.fit(train_X, train_y)
    predictions = model.predict(test_X)

    # Evaluate and plot
    print(f"[{symbol}] R² on test set: {r2_score(test_y, predictions):.4f}")

    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['close'], label='Actual')
    plt.plot(test_df.index, predictions, label='Predicted (Test)', linestyle='--')
    plt.title(f'Stock Price Prediction: {symbol}')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.legend()
    plt.grid(True)
    plt.savefig(f'OUTPUT/{symbol}_price_prediction.png')
    plt.show()

# Main execution
if __name__ == '__main__':
    all_data = load_and_prepare_all()  # Load all data without passing symbol
    for symbol, df in all_data.items():
        train_and_predict(df, symbol)