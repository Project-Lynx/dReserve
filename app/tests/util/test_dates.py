import unittest

from app.util import dates


class TestDates(unittest.TestCase):
    def test_convert_shorthand_month(self):
        self.assertEqual(
            dates.convert_shorthand_month('Jan'), '01',
        )
        self.assertEqual(
            dates.convert_shorthand_month('Mar'), '03',
        )
        self.assertEqual(
            dates.convert_shorthand_month('May'), '05',
        )
        self.assertEqual(
            dates.convert_shorthand_month('Dec'), '12',
        )
        with self.assertRaises(ValueError):
            dates.convert_shorthand_month('January')
        with self.assertRaises(TypeError):
            dates.convert_shorthand_month(["Jan", "Feb"])


if __name__ in '__main__':
    unittest.main()
