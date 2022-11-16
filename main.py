import core
import schedule

if(__name__ == "__main__"):
    schedule.every().hour.do(core.run_bot)

    while True:
        schedule.run_pending()