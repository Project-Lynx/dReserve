import unittest

from app.flask_app import app


class TestEventsRoutes(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.midpoint = '/futures'

    def test_get_hist(self) -> None:
        response = self.app.get(
            self.midpoint + '/get-hist/ZN',
        )
        self.assertEqual(response.status_code, 200)

    def test_get_quotes(self) -> None:
        response = self.app.get(
            self.midpoint + '/get-quote/ES',
        )
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
