"""
Race Dash Pro
graph_manager.py

Менеджер истории показаний и графиков.
"""

from collections import deque

class GraphManager:

    def __init__(self, max_points=300):

        self.max_points = max_points

        self.history = {
            "time": deque(maxlen=max_points),

            "rpm": deque(maxlen=max_points),
            "boost": deque(maxlen=max_points),
            "coolant": deque(maxlen=max_points),
            "oil": deque(maxlen=max_points),
            "voltage": deque(maxlen=max_points),
            "egt": deque(maxlen=max_points),
            "lambda": deque(maxlen=max_points),
            "afr": deque(maxlen=max_points),
            "fuelPress": deque(maxlen=max_points),
            "intake": deque(maxlen=max_points),
            "fuelTemp": deque(maxlen=max_points),
            "ambient": deque(maxlen=max_points),
            "tps": deque(maxlen=max_points),
            "oilPress": deque(maxlen=max_points)
        }

        self.current_time = 0.0

    # -----------------------------------------------------

    def add(self, data: dict):

        self.current_time += 0.1

        self.history["time"].append(self.current_time)

        for key in self.history:

            if key == "time":
                continue

            self.history[key].append(data.get(key, 0))

    # -----------------------------------------------------

    def get(self, key):

        return list(self.history.get(key, []))

    # -----------------------------------------------------

    def get_pair(self, key):

        return (
            list(self.history["time"]),
            list(self.history[key])
        )

    # -----------------------------------------------------

    def clear(self):

        for key in self.history:

            self.history[key].clear()

        self.current_time = 0.0

    # -----------------------------------------------------

    @property
    def size(self):

        return len(self.history["time"])

    # -----------------------------------------------------

    def export(self):

        return {
            k: list(v)
            for k, v in self.history.items()
        }




