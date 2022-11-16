from core import run_bot
import schedule

if(__name__ == "__main__"):
    schedule.every().hour.do(run_bot())

    while True:
        schedule.run_pending()