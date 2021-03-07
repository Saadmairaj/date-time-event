import threading
import datetime


def complete_datetime(dateOrTime, time_now=False):
    """Returns complete datetime.

    Args:
        dateOrTime: Give date or time to get complete time and date.
        time_now (bool, optional): Get complete date with current 
            time. Defaults to False.

    Returns:
        datetime.datetime: datetime with both time and date present.
    """
    if isinstance(dateOrTime, datetime.datetime):
        return dateOrTime
    if isinstance(dateOrTime, datetime.time):
        return datetime.datetime.combine(
            date=datetime.datetime.now().date(), time=dateOrTime)
    time = datetime.time(0, 0, 0)
    if time_now:
        time = datetime.datetime.now().time()
    return datetime.datetime.combine(date=dateOrTime, time=time)


def convert_datetime_secs(date1, date2=None):
    """Returns total seconds difference of two dates."""
    if date2 is None:
        date2 = datetime.datetime.now()
    return (date1 - date2).total_seconds()


if "__main__" == __name__:

    time = datetime.time(16, 3)
    date = datetime.date(2021, 3, 7)
    print(complete_datetime(date))
    print(convert_datetime_secs(
        complete_datetime(datetime.datetime(2021, 4, 10, 0, 0, 0, 0)),
        complete_datetime(datetime.datetime.now()), 
        )
    )
