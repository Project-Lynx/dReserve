import unittest

from app.util import symbols_n_ids


class TestSymbols_n_Ids(unittest.TestCase):
    def test_get_CME_pids(self):
        self.assertEqual(
            symbols_n_ids.get_CME_pids("GE"), "1",
        )
        self.assertEqual(
            symbols_n_ids.get_CME_pids(["6E", "ZN", "CL"]),
            ["58", "316", "425"],
        )


if __name__ == '__main__':
    unittest.main()
