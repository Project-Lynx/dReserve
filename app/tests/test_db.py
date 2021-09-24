import unittest

import pymysql

from app.config import RDS_HOST, RDS_PORT, RDS_PWORD, RDS_USER


class TestDB(unittest.TestCase):
    def test_connection(self) -> None:
        count = 0
        connect = pymysql.connect(
            host=RDS_HOST,
            port=RDS_PORT,
            user=RDS_USER,
            password=RDS_PWORD,
        )
        connect.close()
        count += 1

        self.assertEqual(count, 1)


if __name__ in '__main__':
    unittest.main()
