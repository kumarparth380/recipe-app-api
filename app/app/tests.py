from django.test import TestCase

from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two no are added together"""
        self.assertEqual(add(2, 9), 11)

    def test_subtract_number(self):
        """subtract x from y"""
        self.assertEqual(subtract(2, 9), 7)
