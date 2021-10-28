import unittest
from unittest import TestCase, mock

from app.flask_app import app


class TestYieldsRoutes(TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.midpoint = '/yields'

    def test_get_curve(self) -> None:
        with mock.patch('app.repositories.yields.yields_repo.Yields_Repo.get_data') as patched:
            patched.return_value = None
            response = self.app.get(self.midpoint + '/get-curve/UST/2008-09-15')
            patched.assert_called_with(["UST", "2008-09-15", None])
            self.assertEqual(response.status_code, 200)

    def test_get_rate(self) -> None:
        with mock.patch('app.repositories.yields.yields_repo.Yields_Repo.get_data') as patched:
            patched.return_value = None
            response = self.app.get(self.midpoint + '/get-rate/JGB/M1/current,2017-01-19')
            patched.assert_called_with(["JGB", "current,2017-01-19", "M1"])
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
