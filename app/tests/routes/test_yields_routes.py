import unittest
from unittest import TestCase, mock

from app.flask_app import app


class TestYieldsRoutes(TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.midpoint = '/yields'

    def test_get_curve(self) -> None:
        with mock.patch('app.repositories.yields.yields_repo.Yields_Repo.__init__') as patched:
            patched.return_value = None
            self.app.get(self.midpoint + '/get-curve/united states/previous')
            patched.assert_called_with({"product": "united states", "dates": "previous", "duration": None})

    def test_get_rate(self) -> None:
        with mock.patch('app.repositories.yields.yields_repo.Yields_Repo.__init__') as patched:
            patched.return_value = None
            self.app.get(self.midpoint + '/get-rate/japan/M1/')
            patched.assert_called_with({"product": "japan", "dates": None, "duration": "M1"})


if __name__ == '__main__':
    unittest.main()
