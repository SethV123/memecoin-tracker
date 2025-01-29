from tracker.data_fetcher import fetch_data
from tracker.analyzer import analyze_data
from tracker.alerts import send_telegram_alert
from tracker.scheduler import start_scheduler

def main():
    # Fetch data from DexScreener
    data = fetch_data()

    # Analyze data using technical indicators
    analysis = analyze_data(data)

    # Check for buy/sell signals
    if analysis['should_buy']:
        send_telegram_alert("Buy signal detected!")
    if analysis['should_sell']:
        send_telegram_alert("Sell signal detected!")

    # Start the scheduler to run periodically
    start_scheduler()

if __name__ == "__main__":
    main()
