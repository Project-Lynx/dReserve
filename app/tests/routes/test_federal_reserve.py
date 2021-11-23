import unittest
from unittest import TestCase, mock

from app.flask_app import app


class TestFedRoutes(TestCase):
    def setUp(self) -> None:
        self.app = app.test_client()
        self.patch_target = 'app.repositories.federal_reserve.fomc_statements.FOMC_Statement_Repo.get_data'

    def test_get_fomc_statement(self) -> None:
        with mock.patch(self.patch_target) as patched:
            patched.return_value = None
            response = self.app.get("/fed/get-fomc-statement/")
            patched.assert_called()
            self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
