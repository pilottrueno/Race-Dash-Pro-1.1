"""
Race Dash Pro
ECU Driver - MegaSquirt

Поддержка:
MS2
MS3
MS3Pro
"""

import serial
import threading
import time

class MegaSquirt:

    def __init__(
            self,
            port="/dev/ttyUSB0",
            baudrate=115200):

        self.port = port
        self.baudrate = baudrate

        self.serial = None

        self.connected = False

        self.running = False

        self.thread = None

        self.data = {
            "rpm": 0,
            "boost": 0.0,
            "coolant": 0,
            "oil": 0,
            "voltage": 0.0,
            "egt": 0,
            "lambda": 1.00,
            "afr": 14.7,
            "fuelPress": 0,
            "intake": 0,
            "fuelTemp": 0,
            "ambient": 0,
            "tps": 0,
            "oilPress": 0,
            "gps": 0,
            "gpsFix": False,
            "mode": "NO SIGNAL"
        }

    # --------------------------------------------------

    def connect(self):

        try:

            self.serial = serial.Serial(
                self.port,
                self.baudrate,
                timeout=0.05
            )

            self.connected = True

            self.running = True

            self.thread = threading.Thread(
                target=self._reader,
                daemon=True
            )

            self.thread.start()

            return True

        except Exception as e:

            print("MegaSquirt:", e)

            return False

    # --------------------------------------------------

    def disconnect(self):

        self.running = False

        if self.serial:

            self.serial.close()

        self.connected = False

    # --------------------------------------------------

    def _reader(self):

        while self.running:

            try:

                self.read()

            except Exception:

                pass

            time.sleep(0.01)

    # --------------------------------------------------

    def read(self):
        """
        Здесь позже будет настоящий
        протокол MegaSquirt.
        """

        pass

    # --------------------------------------------------

    def get(self):

        return self.data.copy()



