import sqlite3
import shutil 
import os 
from datetime import datetime

class ChromeExtractor:
    def  __init__(self, history_path):
        self.history_path = history_path
        self.temp_path = "data/History_temp"
    
    def  copy_database(self):
        shutil.copy2(self.history_path, self.temp_path)
        return self.temp_path


    def convert_timestamp(self, chrome_time):
        seconds = chrome_time / 1_000_000
        unix_time = seconds - 11_644_473_600
        return datetime.fromtimestamp(unix_time)

    def extract(self):
        db_path = self.copy_database()
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        cursor.execute("""
            SELECT urls.url, urls.title, visits.visit_time,
                       visits.visit_duration, urls.visit_count
            FROM visits
            JOIN urls ON visits.url = urls.id
            WHERE visits.visit_duration > 0
            ORDER BY visits.visit_time DESC
        """)

        rows = cursor.fetchall()
        history = []

        for row in rows:
            entry = {
                "url" : row[0],
                "title" : row[1],
                "timestamp" : self.convert_timestamp(row[2]),
                "duration" : row[3],
                "visit_count" : row[4],
                "browser" : "chrome"
            }
            history.append(entry)
        conn.close()
        return history
