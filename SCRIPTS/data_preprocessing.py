import os
import pandas as pd

# def load_and_prepare_all(start='2015-01-01', folder='DATA'):
#     data = {}
#     for file in os.listdir(folder):
#         if file.endswith('_monthly.csv'):
#             symbol = file.split('_')[0]  # Extract ticker from filename
#             path = os.path.join(folder, file)
#             df = pd.read_csv(path, index_col=0, parse_dates=True)
#             df.index = pd.to_datetime(df.index, errors='coerce')
#             df = df[df.index >= pd.to_datetime(start)]
#             df['month'] = range(len(df))
#             df = df.rename(columns={"4. close": "close"})
#             data[symbol] = df[['month', 'close']]
#     return data

def load_and_prepare_all(start='2015-01-01', folder='DATA'):
    data = {}
    for file in os.listdir(folder):
        if file.endswith('_monthly.csv'):
            symbol = file.split('_')[0]  # Extract ticker from filename
            path = os.path.join(folder, file)
            df = pd.read_csv(path, index_col=0, parse_dates=True)  # Ensure dates are parsed
            df.index = pd.to_datetime(df.index, errors='coerce')  # Convert index to datetime
            df = df[df.index >= pd.to_datetime(start)]  # Ensure start is a valid date
            df['month'] = range(len(df))
            df = df.rename(columns={"4. close": "close"})
            data[symbol] = df[['month', 'close']]
    return data

# Example usage
if __name__ == '__main__':
    all_data = load_and_prepare_all()
    for symbol, df in all_data.items():
        print(f"{symbol}:\n", df.head(), "\n")