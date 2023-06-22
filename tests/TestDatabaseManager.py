import unittest

from src.DatabaseManager import DatabaseManager


class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseManager(':memory:')

    def test_insert_and_check_headline(self):
        self.assertFalse(self.db.is_headline_exists('test_headline'))
        self.db.insert_headline('test_headline', 'test_summary')
        self.assertTrue(self.db.is_headline_exists('test_headline'))


if __name__ == '__main__':
    unittest.main()
