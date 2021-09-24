import unittest

from app.util import tables


class TestTables(unittest.TestCase):
    def test_get_table(self):
        self.assertEqual(
            tables.get_table("JGB"),
            "JGB_table",
        )

        with self.assertRaises(ValueError):
            tables.get_table("* SHOULD NOT WORK *")


if __name__ == '__main__':
    unittest.main()
