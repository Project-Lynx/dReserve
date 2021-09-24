import unittest

from app.util import links


class TestLinks(unittest.TestCase):
    def test_links(self):
        self.assertEqual(
            links.CME_API_BASE,
            "https://www.cmegroup.com/CmeWS/mvc/Quotes/ContractsByNumber?productIds=",
        )


if __name__ in '__main__':
    unittest.main()
