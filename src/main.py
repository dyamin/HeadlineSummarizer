import time

import openai
import schedule

import config
from DatabaseManager import DatabaseManager
from HeadlineSummarizer import HeadlineSummarizer

"""
This project responsible for summarizing headlines from the nytimes RSS feed and storing them in a database.
It uses the OpenAI API to summarize the headlines.

There are two main approaches to text summarization: Extractive summarization and abstractive summarization. 
Extractive summarization involves selecting the most important sentences or phrases from the original text 
and concatenating them to form a summary, 
while abstractive summarization involves generating new sentences that capture the essence of the original text.
The OpenAI API uses abstractive summarization, which is more difficult to implement but can produce better results.
"""

if __name__ == "__main__":

    print("Starting Headline Summarizer")

    db_manager = DatabaseManager(config.DB_PATH)
    summarizer = HeadlineSummarizer(openai, db_manager)

    # Call the function immediately once at the start
    summarizer.process_headlines()

    # Then schedule it to run every 5 minutes
    schedule.every(config.STEP_IN_MINUTE).minutes.do(summarizer.process_headlines)

    while True:
        schedule.run_pending()
        time.sleep(config.RESOLUTION_IN_SECONDS)
