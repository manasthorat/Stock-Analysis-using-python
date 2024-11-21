import pandas as pd
import yfinance as yf

# Load the CSV file
file_path = 'stock_list.csv'
stock_list_df = pd.read_csv(file_path)


# Extract the "Symbol" and "Market cap" columns
symbols = stock_list_df[['Symbol', 'Market cap']].to_dict('records')

def fetch_stock_data(symbol):
    """
    Fetches the daily historical data for the past year for a given stock symbol.
    """
    try:
        #stock_data = yf.download(symbol+".NS", start="2024-08-12",end="2024-09-13 ", interval='1d')
        stock_data = yf.download(symbol+".NS",period="1mo", interval='1d')
        return stock_data
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def calculate_rsi(data, window=14): 
    """
    Calculates the Relative Strength Index (RSI) for a given stock data.
    """
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def backtest_strategy(stock_data, entry_index):
    """
    Simulates a backtest strategy to determine the success of a trade.
    """
    entry_price = stock_data['Close'].iloc[entry_index]
    max_profit = 0
    max_loss = 0
    time_to_max_profit = 0
    time_to_max_loss = 0
    exit_price = entry_price
    
    for i in range(entry_index + 1, min(entry_index + 14, len(stock_data))):  # Exit after 20 days max
        current_price = stock_data['Close'].iloc[i]
        profit_or_loss = (current_price - entry_price) / entry_price * 100  # Percentage profit or loss
        
        # Update max profit/loss
        if profit_or_loss > max_profit:
            max_profit = profit_or_loss
            time_to_max_profit = i - entry_index
          
        if profit_or_loss < max_loss:
            max_loss = profit_or_loss
            time_to_max_loss = i - entry_index

        # Check exit conditions (e.g., ±10% threshold)
        if profit_or_loss >= 6 or profit_or_loss <= 5:
            exit_price = current_price
            break
        else: 
            exit_price = current_price

    
#    trade_result = 'Profit' if exit_price > entry_price or max_profit > 0 else 'Loss'

    if exit_price > entry_price:

        trade_result = "Profit"
        max_loss = 0
    
    else:
        if max_profit > 0:
            trade_result = "Profit"
            max_profit = max_profit - 1
        else:
            trade_result = "Loss"
            max_profit = 0
    
    return {
        'Max Profit (%)': max_profit,
        'Max Loss (%)': max_loss,
        'Time to Max Profit (days)': time_to_max_profit,
        'Time to Max Loss (days)': time_to_max_loss,
        'Trade Result': trade_result
    }

def check_conditions(stock_data, symbol, market_cap):
    """
    Checks if the conditions are met for a given stock's data.
    """
    master_data = []
    
    # Calculate 9-day average volume
    stock_data['9D_Avg_Volume'] = stock_data['Volume'].rolling(window=9).mean()
    
    # Calculate RSI
    stock_data['RSI'] = calculate_rsi(stock_data)

    # Iterate over the data to check conditions
    for i in range(10, len(stock_data)):
        # Calculate the volume multiple
        volume_multiple = stock_data['Volume'].iloc[i] / stock_data['9D_Avg_Volume'].iloc[i-1]
        
        if (volume_multiple > 4) and (stock_data['Close'].iloc[i] > stock_data['Close'].iloc[i-1]):
            # Perform backtest for the trade
            backtest_results = backtest_strategy(stock_data, i)
            
            # Store the required data
            master_data.append({
                'Stock Name': symbol,
                'Date': stock_data.index[i].strftime('%Y-%m-%d'),
                'RSI': stock_data['RSI'].iloc[i],
                'Volume Multiple': volume_multiple,
                'Market cap': market_cap,
                **backtest_results  # Include backtest results
            })

    return master_data

def store_results(symbols):
    """
    Iterates through all symbols, fetches data, checks conditions, and stores the results.
    """
    all_results = []
    
    for stock in symbols:
        symbol = stock['Symbol']
        market_cap = stock['Market cap']
        stock_data = fetch_stock_data(symbol)
        if stock_data is not None:
            result = check_conditions(stock_data, symbol, market_cap)
            all_results.extend(result)
    
    # Convert the list to a DataFrame
    master_data_df = pd.DataFrame(all_results, columns=[
        'Stock Name', 'Date', 'RSI', 'Volume Multiple', 'Market cap', 
        'Max Profit (%)', 'Max Loss (%)', 'Time to Max Profit (days)', 
        'Time to Max Loss (days)', 'Trade Result'
    ])
    return master_data_df

# Fetch data, check conditions, and store results
master_data_df = store_results(symbols)

# Display the resulting data
print(master_data_df)

# Optionally, save the data to a CSV file
master_data_df.to_csv('test_data.csv', index=False)
