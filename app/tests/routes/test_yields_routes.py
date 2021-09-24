import unittest

from app.flask_app import app


class TestEventsRoutes(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.midpoint = '/yields'

    def test_get_curve(self) -> None:
        response = self.app.get(
            self.midpoint + '/get-curve/UST/2008-09-15',
        )
        self.assertEqual(response.status_code, 200)

    def test_get_rate(self) -> None:
        response = self.app.get(
            self.midpoint + '/get-rate/JGB/M1/MOST_RECENT,2017-01-19',
        )
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
