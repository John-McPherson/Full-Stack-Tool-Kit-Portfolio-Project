from ..dob_check import dob_check
from django.test import TestCase
import datetime

# Create your tests here.
class TestDob(TestCase):
    def test_string_returns_true_if_user_is_18_plus(self):
        self.assertTrue(dob_check("1989-12-15"))

    def test_string_returns_false_if_user_under_18(self):
        self.assertFalse(dob_check("2020-12-15"))

    def test_datetime_returns_false_if_user_under_18(self):
        self.assertFalse(dob_check(datetime.datetime.now()))

    def test_datetime_returns_true_if_user_over_18(self):
        self.assertTrue(dob_check(datetime.datetime(2000, 5, 17)))
