import schedule
import time
from booking_checker import BookingChecker


if __name__ == '__main__':
    booking_checker = BookingChecker("***REMOVED***")

    schedule.every(15).minutes.do(booking_checker.booking_checker_job)

    while True:
        schedule.run_pending()
        time.sleep(1)
