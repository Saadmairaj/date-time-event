import threading
from event.utils import convert_datetime_secs, complete_datetime


class Untiltime(threading.Thread):

    def __init__(self, function=None, dateOrtime=None, name=None,
                 join=False, group=None, daemon=False, *args, **kwargs):

        super().__init__(daemon=daemon, name=name, group=group)
        print(args, kwargs, function)
        self._date = dateOrtime  # if dateOrtime is not None else 0
        self._join = join
        self.function = function
        self.args = kwargs.get('args', [])
        self.kwargs = kwargs.get('kwargs', {})
        self.finished = threading.Event()
        self._return_value = None

    def __call__(self, *args, **kwargs):
        args = list(args)
        print('call', args, kwargs, self.function)
        def _start(*ags, **kw):
            """Internal function."""
            self.args = ags or self.args
            self.kwargs = kw or self.kwargs
            self.start()
            return self._return_value

        fn = args.pop(0) if args and args[0] else None
        if (fn is not None and not callable(self.function) and callable(fn)):
            self.function = fn
            print('Here')
            return _start
        return _start(*args, **kwargs)

    @property
    def date(self):
        """Return date/time."""
        if self._date is not None:
            return complete_datetime(self._date)

    @date.setter
    def date(self, val):
        """Set date/time."""
        self._date = complete_datetime(val)

    def start(self):
        """Start the thread's activity.

        It must be called at most once per thread object. It arranges for the
        object's run() method to be invoked in a separate thread of control.

        This method will raise a RuntimeError if called more than once on the
        same thread object.

        """
        val = super().start()
        if self._join:
            self.join()
        return val

    def cancel(self):
        """Stop the timer if it hasn't finished yet."""
        self.finished.set()

    def run(self):
        """Method representing the thread's activity.

        You may override this method in a subclass. The standard run() method
        invokes the callable object passed to the object's constructor as the
        target argument, if any, with sequential and keyword arguments taken
        from the args and kwargs arguments, respectively.
        
        """
        if self.date:
            self.finished.wait(convert_datetime_secs(self.date))
        if not self.finished.is_set():
            self._return_value = self.function(
                *self.args, **self.kwargs)
        self.finished.set()

    def get(self):
        """Returns the value returned by the tareget function.

        This function will only return value after the target function is 
        called and also if the function itself returns a non-None value.

        """
        if self.finished.is_set() and self._return_value is not None:
            return self._return_value


if "__main__" == __name__:
    import datetime

    date = datetime.time(13, 9, 30)

    @Untiltime(dateOrtime=date)
    def test_function(x):
        print('Test function ran fine! Arg: ', x)
        return x*3

    # th = Untiltime(test_function, date, kwargs=dict(x='Hello'), join=True)
    # th.start()
    print(test_function('Hello'))
    print('Done')
