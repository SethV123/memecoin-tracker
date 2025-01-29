import pandas as pd
import talib

def analyze_data(data):
    # Convert data to a DataFrame
    df = pd.DataFrame(data['pairs'])

    # Calculate RSI
    df['rsi'] = talib.RSI(df['priceUsd'], timeperiod=14)

    # Determine buy/sell signals
    should_buy = df['rsi'].iloc[-1] < 30  # Oversold condition
    should_sell = df['rsi'].iloc[-1] > 70  # Overbought condition

    return {
        'should_buy': should_buy,
        'should_sell': should_sell
    }
