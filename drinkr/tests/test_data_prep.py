from django.test import TestCase
from ..data_prep import data_prep

class TestData(TestCase):
    def test_if_passed_plain_text_returns_unmodified(self):
        self.assertEqual(data_prep("test"), "test")
