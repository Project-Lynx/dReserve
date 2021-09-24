import unittest

from app.flask_app import app


class TestEventsRoutes(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.midpoint = '/events'

    def test_get_econ_events(self) -> None:
        response = self.app.get(
            self.midpoint + '/get-econ-events/US',
        )
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
