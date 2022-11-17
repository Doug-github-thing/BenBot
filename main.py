import core
import schedule
import time

if(__name__ == "__main__"):

    # wait for the time to be a new hour before scheduling recurring bong    
    t = time.localtime()
    t = time.strftime("%H:%M:%S", t)
    initial_hr = int(t[:2])
    hr = initial_hr

    while hr == initial_hr:
        t = time.localtime()
        t = time.strftime("%H:%M:%S", t)
        hr = int(t[:2])
        time.sleep(10)        

    schedule.every().hour.do(core.run_bot)
    core.run_bot()

    while True:
        schedule.run_pending()