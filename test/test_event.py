import unittest
import time
import datetime
from event import Untiltime


class TestUntiltimeDecorator(unittest.TestCase):

    date = datetime.datetime.now()
    sec = date.second + 5
    if sec > 60: 
        sec = 5
    date_test = datetime.time(date.hour, date.minute, sec)

    # Class functions
    @Untiltime(join=True)
    def dummy_decorator_join(self):
        return self

    @Untiltime(join=True)
    def dummy_decorator_return(self, value):
        return value

    @Untiltime()
    def dummy_decorator_no_join(self):
        time.sleep(0.1)
        self._no_join_class = True

    @Untiltime(dateOrtime=date_test)
    def dummy_decorator_date(self, value):
        return value

    @Untiltime(dateOrtime=date_test, join=True)
    def dummy_decorator_date_join(self, value):
        return value

    def test_class_return(self):
        value = 10
        self.assertEqual(self.dummy_decorator_return(value), value)

    def test_class_join(self):
        self.assertEqual(self.dummy_decorator_join(), self)

    def test_class_no_join(self):
        self.dummy_decorator_no_join()
        time.sleep(0.2)
        self.assertEqual(
            getattr(self, '_no_join_class', False), True)

    def test_class_date(self):
        val = 10
        self.assertEqual(self.dummy_decorator_date_join(val), val)
        self.assertEqual(self.dummy_decorator_date(val), val)

    def test_return(self):
        @Untiltime(join=True)
        def _return(val):
            return val
        self.assertEqual(_return(10), 10)

    def test_join(self):
        @Untiltime(join=True)
        def _join():
            return self
        self.assertEqual(_join(), self)

    def test_no_join(self):
        # No parenthesis
        @Untiltime
        def _no_join1():
            time.sleep(0.1)
            self._no_join = True
        _no_join1()
        time.sleep(0.2)
        self.assertEqual(getattr(self, '_no_join', False), True)

        # Parenthesis
        @Untiltime()
        def _no_join2():
            time.sleep(0.1)
            self._no_join = False
        _no_join2()
        time.sleep(0.2)
        self.assertEqual(getattr(self, '_no_join', True), False)

    def test_date(self):
        date = datetime.datetime.now()
        sec = date.second + 5
        if sec > 60:
            sec = 5
        date_test = datetime.time(
            date.hour, date.minute, sec)

        # Date with join set to True.
        @Untiltime(dateOrtime=date_test, join=True)
        def _date_join(val):
            return val*val

        # Date with join set to False.
        @Untiltime(dateOrtime=date_test)
        def _date_no_join(val):
            return val*val

        val = 10
        self.assertEqual(_date_join(val), val*val)
        self.assertEqual(_date_no_join(val), val*val)

    def test_date_accuracy(self):
        date = datetime.datetime.now()
        sec = date.second + 5
        if sec > 60:
            sec = 5
        date_test = datetime.time(
            date.hour, date.minute, sec)

        @Untiltime(dateOrtime=date_test, join=True)
        def _date_acc():
            return datetime.datetime.now(
                ).time().replace(microsecond=0)

        self.assertEqual(date_test, _date_acc())


if "__main__" == __name__:
    unittest.main()
