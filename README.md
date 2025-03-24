# Stock Price Prediction Tool

## Repository Overview
Welcome to the DS4002 Project 2 Repo for Hudson Noyes, Akan Ndem, and Ali Nilforoush. Our project focused using past stock prices to make predictions of future prices. This repo contains: this README and a LICENSE file and DATA, SCRIPT, and OUTPUT folders.

---

## Section 1: Software and Platform  
This project was developed using the following software and tools:

- **Software Used:**  
  - [Python]
  - [Apla Vantage API]   
  
- **Add-On Packages:**  
  - [PANDAS] – [Used for data manipulation and analysis]
  - [REQUESTS] - [Used for JSON accessing]
  - [MAPLOTLIB.PYPLOT] - [Used for data visualization]
  - [TIME] - [Used for time related functions]
  - [SCIPY] - [Used for analysis of AI detection results]
  - [SKLEARN] - [Used for model training and testing R^2 values]
  - [OS] - [Used for directory access to make code more modular]
 
- **Platform Compatibility:**  
  - ✅ Windows  
  - ✅ macOS (used during project)  
  - ✅ Linux  

Ensure you have the required software installed before proceeding.

---

## Section 2: Project Structure  
Below is a map of the repository, illustrating the hierarchy of files and folders:

📂 Project_Folder/ │-- 📂 DATA/ # Stock price data in csv form from 1999-12-31 - 2025-03-21 │-- 📂 SCRIPTS/ # Code for data processing, training, testing, and analysis │ │-- preliminar_plots.py # Pull data using Alpha Vantage API and store in CSV files for each ticker │ │-- data_preprocessing.py # Data cleaning and normalizing │  │-- model_training.py # training, testing, and analyzing data │-- 📂 RESULTS/ # Output files (graphs) │-- 📂 RESULTS/ # results of analysis performed on data, showing regression model test against data after 2020-04-01 │ │-- README.md # This orientation file

## Section 3: Results Reproduction Instructions
1. Run preliminary_plots.py: Uses the Alpha Vantage API to pull stock data based on the input ticker (in our case: AAPL, MSFT, NVDA, JPM, V, MA, LLY, JNJ, UNH, GLD, DLV). After the user inputs a ticker, the program validates the return object, converts it do a data fram from json, and stores it as a csv file for later use.
   ```python
   import requests
    import json
    import pandas as pd
    
    api_key = 'BGC08TPHNNTLV25Z'
    
    def get_monthly_ticker_data(symbol):
    # symbol = input("Please enter the stock symbol: ").strip().upper()
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={symbol}&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    if "Monthly Time Series" not in data:
        print("Error: Unexpected response format.")
        return None

    df = pd.DataFrame.from_dict(data["Monthly Time Series"], orient="index").astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df.to_csv(f"DATA/{symbol}_monthly.csv")
    return df


    if __name__ == '__main__':
        symbol = input("Please enter ticker symbol: ").strip().upper()
        df = get_monthly_ticker_data(symbol)
        print(df.head())
   ```

2. Run data_preprocessing.py: this script cleans the data to to only include the date and monthly close price for each ticker and normalizes the "close" column.
   ```python
   import os
   import pandas as pd
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
   ```

3. Run model_training.py: this script breaks up the data into two parts:
   
     - one part being from 2015-01-01 - 2020-01-31
     - the other part being from 2020-04-01 - 2025-03-21

   This allows the older data to be for training the model, which is better since there are many more data points, and the newer data to be tested against the prediction model. After splitting the data in two, it is plotted and the R-squared value is gathered.
   ```python
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
   ```
