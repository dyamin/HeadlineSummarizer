import sqlite3


class DatabaseManager:

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS headlines
                         (full_headline PRIMARY KEY, summarised_headline)''')

    def insert_headline(self, full_headline, summarised_headline):
        self.c.execute("INSERT INTO headlines VALUES (?,?)", (full_headline, summarised_headline))
        self.conn.commit()

    def is_headline_exists(self, full_headline):
        self.c.execute('SELECT * FROM headlines WHERE full_headline=?', (full_headline,))
        return self.c.fetchone() is not None
