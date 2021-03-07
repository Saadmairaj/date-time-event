import unittest
import time
import datetime
from date_time_event import Untiltime
from date_time_event.utils import complete_datetime


class Test_complete_datetime(unittest.TestCase):

    def test_time(self):
        date_test = datetime.datetime.now()
        time = date_test.time()
        self.assertEqual(date_test, complete_datetime(time))

    def test_date_now(self):
        date_test = datetime.datetime.now()
        current_time = complete_datetime(date_test.date(), True)
        self.assertEqual(date_test.day, current_time.day)
        self.assertEqual(date_test.hour, current_time.hour)
        self.assertEqual(date_test.minute, current_time.minute)
        self.assertEqual(date_test.second, current_time.second)
        self.assertEqual(str(date_test.microsecond)[:-4],
                         str(current_time.microsecond)[:-4])

    def test_date(self):
        date_test = datetime.datetime.now().replace(
            hour=0, second=0, minute=0, microsecond=0)
        date = date_test.date()
        self.assertEqual(date_test, complete_datetime(date))


class TestUntiltime(unittest.TestCase):

    def dummy_return(self, value):
        return value*value

    def dummy_delay_run(self, delay=0.1):
        time.sleep(delay)
        self._delay_run = True

    def dummy_current_datetime(self):
        return datetime.datetime.now()

    def test_return(self):
        value = 10
        th = Untiltime(
            self.dummy_return, kwargs=dict(value=value))
        th.start()
        th.join()
        self.assertEqual(th.get(), value*value)

    def test_no_join(self):
        th = Untiltime(self.dummy_delay_run)
        th.start()
        time.sleep(0.2)
        self.assertTrue(getattr(self, '_delay_run', False))

    def test_Date(self):
        value = 10
        date_test = datetime.datetime.now() + datetime.timedelta(0, 2)
        th = Untiltime(
            self.dummy_return,
            dateOrtime=date_test, join=True,
            kwargs=dict(value=value))
        th.start()
        self.assertGreater(datetime.datetime.now(), date_test)
        self.assertEqual(th.get(), value*value)

    def test_change_date(self):
        date_test1 = datetime.datetime.now() + datetime.timedelta(
            days=2, hours=2, minutes=2, seconds=5)
        date_test2 = datetime.datetime.now() + datetime.timedelta(0, 2)

        th = Untiltime(
            self.dummy_current_datetime,
            dateOrtime=date_test1, join=True)
        th.date = date_test2
        th.start()

        current_time = th.get()
        self.assertEqual(date_test2.day, current_time.day)
        self.assertEqual(date_test2.hour, current_time.hour)
        self.assertEqual(date_test2.minute, current_time.minute)
        self.assertEqual(date_test2.second, current_time.second)
        self.assertNotEqual(date_test1.day, current_time.day)
        self.assertNotEqual(date_test1.hour, current_time.hour)
        self.assertNotEqual(date_test1.minute, current_time.minute)
        self.assertNotEqual(date_test1.second, current_time.second)

    def test_accuracy(self):
        date_test = datetime.datetime.now() + datetime.timedelta(0, 2)
        th = Untiltime(
            self.dummy_current_datetime,
            join=True, dateOrtime=date_test)
        th.start()
        current_time = th.get()
        self.assertEqual(date_test.day, current_time.day)
        self.assertEqual(date_test.hour, current_time.hour)
        self.assertEqual(date_test.minute, current_time.minute)
        self.assertEqual(date_test.second, current_time.second)
        self.assertNotEqual(date_test.microsecond, current_time.microsecond)

    def test_cancel(self):
        date_test = datetime.datetime.now() + datetime.timedelta(0, 2)
        th = Untiltime(
            setattr, dateOrtime=date_test,
            kwargs=dict(__obj=self, __name='_not_exist', __value=True))
        th.start()
        th.cancel()
        with self.assertRaises(AttributeError):
            getattr(self, '_not_exist')


class TestUntiltimeDecorator(unittest.TestCase):

    date_test = datetime.datetime.now() + datetime.timedelta(0, 2)

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
        self.assertTrue(getattr(self, '_no_join_class', False))

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
        self.assertTrue(getattr(self, '_no_join', False))

        # Parenthesis
        @Untiltime()
        def _no_join2():
            time.sleep(0.1)
            self._no_join = False
        _no_join2()
        time.sleep(0.2)
        self.assertFalse(getattr(self, '_no_join', True))

    def test_date(self):
        date_test = datetime.datetime.now() + datetime.timedelta(0, 2)

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
        date_test = datetime.datetime.now() + datetime.timedelta(0, 2)

        @Untiltime(dateOrtime=date_test, join=True)
        def _date_acc():
            return datetime.datetime.now()

        current_time = _date_acc()
        self.assertEqual(date_test.day, current_time.day)
        self.assertEqual(date_test.hour, current_time.hour)
        self.assertEqual(date_test.minute, current_time.minute)
        self.assertEqual(date_test.second, current_time.second)
        self.assertNotEqual(date_test.microsecond, current_time.microsecond)
