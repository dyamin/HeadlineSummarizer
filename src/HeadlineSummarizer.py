import feedparser

from src import config


class HeadlineSummarizer:

    def __init__(self, openai, db_manager):
        print("Initializing Headline Summarizer")

        # Setting up the OpenAI API credentials
        self.openai = openai
        self.openai.api_key = config.OPENAI_API_KEY

        # Setting up the database
        self.db_manager = db_manager

    def process_headlines(self):
        full_headline = self.get_main_headline()
        if not self.db_manager.is_headline_exists(full_headline):
            summarised_headline = self.summarize_headline(full_headline)
            self.db_manager.insert_headline(full_headline, summarised_headline)
        else:
            print(f"Headline already exists in the database, skipping...")

    @staticmethod
    def get_main_headline():
        # This function uses the feedparser library to parse the RSS feed and get the main headline
        # Assuming the main headline is the first item in the feed

        feed = feedparser.parse(config.RSS_TO_PARSE)
        headline_text = feed.entries[0].title  # The title of the first news item
        print(f"Headline: {headline_text}")
        return headline_text

    def summarize_headline(self, full_headline):
        response = self.openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Please summarize the following headline to {config.NUMBER_OF_WORDS} words:\n{full_headline}\n\nSummary:",
            temperature=0.3,
            max_tokens=config.MAX_TOKENS,
        )
        summarised_headline = response.choices[0].text

        summarised_headline = ' '.join(summarised_headline.strip().split()[:config.MAX_TOKENS])

        print(f"Summary: {summarised_headline}")
        return summarised_headline
