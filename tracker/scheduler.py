import schedule
import time
from main import main

def start_scheduler():
    # Run the main function every hour
    schedule.every().hour.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
