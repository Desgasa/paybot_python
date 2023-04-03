import time 
import datetime


def days_to_seconds(days):
        return days * 24 * 60 * 60


def time_sub_day(get_time):
        time_now = int(time.time())
        middle_time = int(get_time) - time_now
        if middle_time <= 0:
                return False
        else: 
                dt = str(datetime.timedelta(seconds=middle_time))
                dt = dt.replace("days","Дней")
                return dt