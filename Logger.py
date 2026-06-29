"""
Race Dash Pro
logger.py

Менеджер логирования.
"""

from pathlib import Path
from datetime import datetime
import csv
import json

class DataLogger:

    def __init__(self,
                 log_folder="logs",
                 max_minutes=60):

        self.folder = Path(log_folder)
        self.folder.mkdir(exist_ok=True)

        self.max_minutes = max_minutes

        self.minute_logs = []

        self.current_log = []

        self.current_start = datetime.now()

    # -------------------------------------------------

    def add(self, data: dict):
        """
        Добавить запись.
        """

        entry = data.copy()

        entry["timestamp"] = datetime.now().strftime("%H:%M:%S")

        self.current_log.append(entry)

    # -------------------------------------------------

    def finish_minute(self):
        """
        Закрыть минутный лог.
        """

        if len(self.current_log) == 0:
            return

        self.minute_logs.append({
            "start": self.current_start,
            "entries": self.current_log
        })

        while len(self.minute_logs) > self.max_minutes:
            self.minute_logs.pop(0)

        self.current_start = datetime.now()

        self.current_log = []

    # -------------------------------------------------

    def get_logs(self):

        return self.minute_logs

    # -------------------------------------------------

    def save_txt(self, index):

        log = self.minute_logs[index]

        filename = self.folder / (
            log["start"].strftime("%Y-%m-%d_%H-%M") + ".txt"
        )

        with open(filename, "w", encoding="utf-8") as f:

            for row in log["entries"]:

                f.write(json.dumps(
                    row,
                    ensure_ascii=False
                ))

                f.write("\n")

        return filename

    # -------------------------------------------------

    def save_csv(self, index):

        log = self.minute_logs[index]

        filename = self.folder / (
            log["start"].strftime("%Y-%m-%d_%H-%M") + ".csv"
        )

        if len(log["entries"]) == 0:
            return filename

        with open(filename,
                  "w",
                  newline="",
                  encoding="utf-8") as f:

            writer = csv.DictWriter(
                f,
                fieldnames=log["entries"][0].keys()
            )

            writer.writeheader()

            writer.writerows(log["entries"])

        return filename

    # -------------------------------------------------

    def clear(self):

        self.minute_logs.clear()

        self.current_log.clear()

    # -------------------------------------------------

    @property
    def count(self):

        return len(self.minute_logs)


