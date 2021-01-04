from datetime import datetime, timedelta
from math import pow


def add(moment: datetime) -> datetime:
    """
    Returns a gigasecond from given time

    :param
    moment: datetime.datetime

    :return:
    moment_plus_gigasecond: datetime.datetime
    """
    return moment + timedelta(0, pow(10, 9))
