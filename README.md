# date-time-event
[![PyPI](https://img.shields.io/pypi/v/date-time-event?color=dark)](https://pypi.org/project/date-time-event/)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/ee305868a6a044c281f9423102f8480e)](https://www.codacy.com/gh/Saadmairaj/date-time-event/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Saadmairaj/date-time-event&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/ee305868a6a044c281f9423102f8480e)](https://www.codacy.com/gh/Saadmairaj/date-time-event/dashboard?utm_source=github.com&utm_medium=referral&utm_content=Saadmairaj/date-time-event&utm_campaign=Badge_Coverage)
[![Downloads](https://static.pepy.tech/personalized-badge/date-time-event?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=downloads)](https://pepy.tech/project/date-time-event)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FSaadmairaj%2Fdate-time-event&count_bg=%238EE74A&title_bg=%23555555&icon=python.svg&icon_color=%239A9A9A&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSaadmairaj%2Fdate-time-event.svg?type=small)](https://app.fossa.com/projects/git%2Bgithub.com%2FSaadmairaj%2Fdate-time-event?ref=badge_small)

A very simple package to trigger events at a specific DateTime.

## Installation

Use the package manager pip to install with the following command:

```bash
pip install date-time-event
```

If you would like to get the latest master or branch from github, you could also:

```bash
pip install git+https://github.com/Saadmairaj/date-time-event
```

Or even select a specific revision _(branch/tag/commit)_:

```bash
pip install git+https://github.com/Saadmairaj/date-time-event@master
```

## Usage

It is very simple and easy to use. First import the class which can be used either as a decorator or a thread function.

```python
from date_time_event import Untiltime
```

The `Untiltime` class is threaded based timer which will wait till the given date or timer is met. As it runs on a separate thread, it doesn't effect the main thread or lock it.

```python
from datetime import datetime, timedelta
from date_time_event import Untiltime

# Current datetime with 5 seconds in future.
date = datetime.now() + timedelta(0, 5)


@Untiltime(dateOrtime=date)
def function():
    print('Hello! Its time!', datetime.now())


function()
print('Function will be call at: %s \n' % date)
```

- `Untiltime` decorator options. Syntax: `@Untiltime( **options )`

  | Options      | Description                                                                                                                                                                                     |
  | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | _function_   | Pass Target function.                                                                                                                                                                           |
  | _dateOrtime_ | Give date or time for the function to trigger if None give function will be a threaded function which can only run once. The date, time or datetime should be an instance of `datetime` module. |
  | _name_       | A string used for identification purposes only. Just like in thread                                                                                                                             |
  | _join_       | Wait until the thread terminates. This blocks the calling thread until the thread whose `join()` method is called terminates.                                                                   |
  | _group_      | Reserved for future extension when a ThreadGroup class is implemented.                                                                                                                          |
  | _daemon_     | A boolean value indicating whether this thread is a daemon thread (True) or not (False).                                                                                                        |
  | _args_       | The _args_ is the argument tuple for the target invocation. Defaults to ().                                                                                                                     |
  | _kwargs_     | The _kwargs_ is a dictionary of keyword arguments for the target invocation. Defaults to {}.                                                                                                    |

The `Untiltime` class can also be used as thread class. Like so

```python
from datetime import datetime, timedelta
from date_time_event import Untiltime

def function():
    print('Hello! Its time!', datetime.now())


# Current datetime with 5 seconds in future.
date = datetime.now() + timedelta(0, 5)

th = Untiltime(function, dateOrtime=date)
th.start()

print('Function will be call at: %s \n' % date)
```

Once the thread is called it can be stopped or cancel if called `.cancel()` method before the datetime event occurs.

- Set date can be changed with property `date`, if the thread has not started.

```python
from datetime import datetime, timedelta
from date_time_event import Untiltime

def function():
    print('Hello! Its time!', datetime.now())


# Current datetime with 5 seconds in future.
date = datetime.now() + timedelta(0, 1)

th = Untiltime(function, dateOrtime=date)
# Initializing new date
th.date = datetime.now() + timedelta(0, 5)
th.start()

print('Function will be call at: %s \n' % th.date)
```

## [License](https://github.com/Saadmairaj/date-time-event/blob/master/LICENSE)

[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2FSaadmairaj%2Fdate-time-event.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2FSaadmairaj%2Fdate-time-event?ref=badge_large)
