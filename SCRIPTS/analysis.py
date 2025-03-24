from data_preprocessing import load_and_prepare
from model_training import train_and_predict

etfs = ['SPY', 'QQQ', 'XLK', 'XLF', 'GLD', 'SLV']

for symbol in etfs:
    print(f"\n=== {symbol} ===")
    df = load_and_prepare(symbol)
    train_and_predict(df)