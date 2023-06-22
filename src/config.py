from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent


OPENAI_API_KEY = 'OPENAI_API_KEY'
RSS_TO_PARSE = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
DB_PATH = '../resources/headlines.db'

NUMBER_OF_WORDS = 5
MAX_TOKENS = NUMBER_OF_WORDS * 2

STEP_IN_MINUTE = 5
RESOLUTION_IN_SECONDS = 1
