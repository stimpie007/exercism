from calendar import Calendar, day_name
from datetime import date

WEEKDAY_NAMES = dict(zip(day_name, range(0, 7)))


class MeetupDayException(Exception):
    pass


def raise_():
    raise MeetupDayException("Month specified doesn't have 5th day of week.")


def meetup(year, month, week, day_of_week):
    WEEK_GETTER = {
        "1st": lambda x: x[0],
        "2nd": lambda x: x[1],
        "3rd": lambda x: x[2],
        "4th": lambda x: x[3],
        "5th": lambda x: x[4] if len(x) == 5 else raise_(),
        "last": lambda x: x[-1],
        "teenth": lambda x: list(filter(lambda y: 13 <= y[2] < 20, x))[0],
    }
    cal = Calendar()
    month_cal = list(
        filter(
            lambda x: x[0] == year
                      and x[1] == month
                      and x[3] == WEEKDAY_NAMES[day_of_week],
            cal.itermonthdays4(year, month),
        )
    )
    return date(*WEEK_GETTER[week](month_cal)[:-1])
