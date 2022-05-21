from django.test import TestCase
from ..data_prep import data_prep


class TestData(TestCase):
    def test_if_passed_plain_text_returns_unmodified(self):
        self.assertEqual(data_prep("test"), "test")

    def test_if_passed_a_different_plain_text_rtrns_unmodified(self):
        self.assertEqual(data_prep("test two"), "test two")

    def test_should_replace_commas_with_character_code(self):
        self.assertEqual(data_prep("test, two"), "test&#44; two")

    def test_should_replace_commas_with_character_code(self):
        self.assertEqual(data_prep("'(test)'"), "&#39;&#40;test&#41;&#39;")
        self.assertEqual(data_prep('"<test>"'), "&#34;&#60;test&#62;&#34;")
