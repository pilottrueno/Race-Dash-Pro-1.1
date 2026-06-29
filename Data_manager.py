"""
Race Dash Pro
data_manager.py

Менеджер получения данных.
Поддерживает:
- Demo
- Speeduino
- MaxxECU
- ECUMaster
- OBD-II
"""

from dataclasses import dataclass
import math
import time

@dataclass
class DashboardData:
    rpm: int = 0
    boost: float = 0.0
    coolant: int = 0
    oil: int = 0
    voltage: float = 0.0
    egt: int = 0
    lambda_value: float = 1.00
    afr: float = 14.7
    fuel_press: float = 0.0
    intake: int = 0
    fuel_temp: int = 0
    ambient: int = 20
    tps: int = 0
    oil_press: float = 0.0
    gps_speed: int = 0
    gps_fix: bool = False
    mode: str = "NO SIGNAL"

class DataManager:
    """
    Главный менеджер данных.
    """

    def __init__(self):

        self.source = "demo"

        self.time = 0

        self.data = DashboardData()

    def set_source(self, source: str):

        self.source = source.lower()

    def update(self):

        if self.source == "demo":
            self._update_demo()

        elif self.source == "speeduino":
            self._update_speeduino()

        elif self.source == "maxxecu":
            self._update_maxxecu()

        elif self.source == "ecumaster":
            self._update_ecumaster()

        elif self.source == "obd":
            self._update_obd()

        return self.data

    # -------------------------------------------------
    # DEMO
    # -------------------------------------------------

    def _update_demo(self):

        self.time += 0.02

        rpm = 4400 + 3600 * math.sin(self.time)

        rpm = max(800, min(8000, int(rpm)))

        load = rpm / 8000

        self.data.rpm = rpm

        self.data.boost = round(load * 1.5, 2)

        self.data.coolant = int(85 + load * 40)

        self.data.oil = int(90 + load * 50)

        self.data.voltage = round(14.2 - load * 0.8, 1)

        self.data.egt = int(400 + load * 600)

        self.data.lambda_value = round(1.0 - load * 0.12, 2)

        self.data.afr = round(self.data.lambda_value * 14.7, 1)

        self.data.fuel_press = round(3.8 + load * 1.5, 1)

        self.data.intake = int(20 + load * 30)

        self.data.fuel_temp = int(30 + load * 25)

        self.data.ambient = 20

        self.data.tps = int(load * 100)

        self.data.oil_press = round(1.2 + load * 4.3, 1)

        self.data.gps_speed = int(rpm / 30)

        self.data.gps_fix = rpm > 900

        if rpm > 7000:
            self.data.mode = "RACE"

        elif rpm > 5500:
            self.data.mode = "SPORT"

        else:
            self.data.mode = "NORMAL"

    # -------------------------------------------------
    # ECU
    # -------------------------------------------------

    def _update_speeduino(self):

        # Здесь позже будет подключение Speeduino
        pass

    def _update_maxxecu(self):

        # Здесь позже будет подключение MaxxECU
        pass

    def _update_ecumaster(self):

        # Здесь позже будет подключение ECUMaster
        pass

    def _update_obd(self):

        # Здесь позже будет подключение OBD-II
        pass

    # -------------------------------------------------

    def get_dict(self):

        return {
            "rpm": self.data.rpm,
            "boost": self.data.boost,
            "coolant": self.data.coolant,
            "oil": self.data.oil,
            "voltage": self.data.voltage,
            "egt": self.data.egt,
            "lambda": self.data.lambda_value,
            "afr": self.data.afr,
            "fuelPress": self.data.fuel_press,
            "intake": self.data.intake,
            "fuelTemp": self.data.fuel_temp,
            "ambient": self.data.ambient,
            "tps": self.data.tps,
            "oilPress": self.data.oil_press,
            "gps": self.data.gps_speed,
            "gpsFix": self.data.gps_fix,
            "mode": self.data.mode
        }


