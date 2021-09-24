import unittest

from app.repositories.futures import hist, quote


class TestFuturesRepo(unittest.TestCase):
    def test_get_hist(self) -> None:
        scenarios = ["ZN", "ES"]
        for scenario in scenarios:
            output = hist.get_hist(scenario)
            self.assertIsInstance(output, dict)
            self.assertEqual(
                len([key for key in output]), 1,
            )

    def test_get_hists(self) -> None:
        scenarios = ["SR3,GE", "CL,NG,BTC"]
        for scenario in scenarios:
            output = hist.get_hists(scenario)
            self.assertIsInstance(output, dict)
            self.assertEqual(
                len([key for key in output]),
                len(list(scenario.split(","))),
            )

    def test_hist_handler(self) -> None:
        scenarios = ["ES", "NG,CL"]
        for scenario in scenarios:
            output = hist.handler(scenario)
            self.assertIsInstance(output, dict)

    def test_get_quote(self) -> None:
        scenarios = ["GE", "SR3"]
        for scenario in scenarios:
            output = quote.get_quote(scenario)
            self.assertIsInstance(output, dict)
            self.assertEqual(
                len([key for key in output]), 1,
            )

    def test_get_quotes(self) -> None:
        scenarios = ["GE,SR3", "CL,BTC"]
        for scenario in scenarios:
            output = quote.get_quotes(scenario)
            self.assertIsInstance(output, dict)
            self.assertEqual(
                len([key for key in output]),
                len(list(scenario.split(","))),
            )

    def test_handle_quotes(self) -> None:
        scenarios = ["NG", "CL,ES,BTC"]
        for scenario in scenarios:
            output = quote.handler(scenario)
            self.assertIsInstance(output, dict)


if __name__ in '__main__':
    unittest.main()
