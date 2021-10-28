"""
import unittest

from app.repositories.events import events


class TestEventsRepo(unittest.TestCase):
    def test_get_events(self) -> None:
        scenario = "US,IN,CA,JP,GB"
        output = events.get_events(scenario)
        self.assertIsInstance(output, dict)
        self.assertEqual(len(output[1]), 5)

    def test_handle_events(self) -> None:
        scenarios = ["CA", "JP,GB"]
        for scenario in scenarios:
            output = events.handle_events(scenario)
            self.assertIsInstance(output, dict)


if __name__ in '__main__':
    unittest.main()
"""
