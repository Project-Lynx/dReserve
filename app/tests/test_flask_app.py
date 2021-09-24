import unittest

from app.flask_app import app


class TestHealth(unittest.TestCase):
    def test_healthcheck(self):
        response = app.test_client().get("/")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
