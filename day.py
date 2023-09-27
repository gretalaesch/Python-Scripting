# Compute and print the current day of the week.

# import module to compute the seconds since midnight of 1/1/1970:
from time import time
time()
timeval = int(time())
def UTCDay(timeval):
    """Takes as input UTC time value (float), and returns the
    number of the day of the week (integer between 0 and 6 inclusive)"""
    day = (int((timeval / 86400) % 7))
    return day

UTCDay(timeval)

offset = -5
def localDay(timeval, offset):
    """Takes as input UTC time value  (float) and an offset (float),
    calls UTCDay to help compute the current day of the week
    for a timezone that is offset hours ahead of UTC."""
    day = (int(((timeval + (offset * 3600)) / 86400) % 7))
    return day

localDay(timeval, offset)
#Changes standard UTC time to the timezone of Williamstown (Offset -5)

wday = (localDay(timeval, offset) - 3)
#Defines wday as the time in Williamstown, and changes day 0 to Sunday

def dayOfWeek(wday):
    if wday == 1:
        return 'Monday'
    elif wday == 2:
        return 'Tuesday'
    elif wday == 3:
        return 'Wednesday'
    elif wday == 4:
        return 'Thursday'
    elif wday == 5:
        return 'Friday'
    elif wday == 6:
        return 'Saturday'
    else:
        return 'Sunday'

# at this point, we have definitions necessary to support the computation
# add code, here, to print the day of the week in Williamstown (offset -5)
# according to the format described in the lab handout.

if __name__ == "__main__":
    print('It is', dayOfWeek(wday)+'!')
