import unittest
from unittest.mock import Mock

from src.HeadlineSummarizer import HeadlineSummarizer


class TestHeadlineSummarizer(unittest.TestCase):

    def setUp(self):
        self.db = Mock()
        self.openai = Mock()
        self.summarizer = HeadlineSummarizer(self.openai, self.db)


if __name__ == '__main__':
    unittest.main()
