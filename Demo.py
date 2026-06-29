"""
Race Dash Pro
Demo ECU Driver

Имитирует работу двигателя.
"""

from dataclasses import dataclass
import math
import time

@dataclass
class DemoData:
    rpm: int = 850
    boost: float = 0.0
    coolant: int = 85
    oil: int = 90
    voltage: float = 14.2
    egt: int = 450
    lambda_value: float = 1.00
    afr: float = 14.7
    fuelPress: float = 3.8
    intake: int = 22
    fuelTemp: int = 28
    ambient: int = 20
    tps: int = 0
    oilPress: float = 1.5
    gps: int = 0
    gpsFix: bool = True
    mode: str = "IDLE"

class DemoECU:

    def __init__(self):

        self.data = DemoData()

        self.start_time = time.time()

    def update(self):

        t = time.time() - self.start_time

        # Цикл разгона 12 секунд
        phase = t % 12

        if phase < 2:
            rpm = 850

        elif phase < 5:
            rpm = 850 + (phase - 2) * 2200

        elif phase < 7:
            rpm = 7500

        elif phase < 9:
            rpm = 7500 - (phase - 7) * 3200

        else:
            rpm = 1100 + 250 * math.sin(t * 3)

        rpm = int(max(850, min(8000, rpm)))

        load = rpm / 8000

        self.data.rpm = rpm
        self.data.boost = round(load * 1.6, 2)
        self.data.coolant = int(85 + load * 25)
        self.data.oil = int(90 + load * 35)
        self.data.voltage = round(14.3 - load * 0.6, 1)
        self.data.egt = int(420 + load * 550)
        self.data.lambda_value = round(1.02 - load * 0.15, 2)
        self.data.afr = round(self.data.lambda_value * 14.7, 1)
        self.data.fuelPress = round(3.8 + load * 1.8, 1)
        self.data.intake = int(20 + load * 28)
        self.data.fuelTemp = int(28 + load * 18)
        self.data.ambient = 20
        self.data.tps = int(load * 100)
        self.data.oilPress = round(1.3 + load * 4.5, 1)

        self.data.gps = int(rpm / 32)
        self.data.gpsFix = True

        if rpm > 7000:
            self.data.mode = "RACE"
        elif rpm > 5000:
            self.data.mode = "SPORT"
        elif rpm > 1200:
            self.data.mode = "NORMAL"
        else:
            self.data.mode = "IDLE"

    def get(self):

        self.update()

        return {
            "rpm": self.data.rpm,
            "boost": self.data.boost,
            "coolant": self.data.coolant,
            "oil": self.data.oil,
            "voltage": self.data.voltage,
            "egt": self.data.egt,
            "lambda": self.data.lambda_value,
            "afr": self.data.afr,
            "fuelPress": self.data.fuelPress,
            "intake": self.data.intake,
            "fuelTemp": self.data.fuelTemp,
            "ambient": self.data.ambient,
            "tps": self.data.tps,
            "oilPress": self.data.oilPress,
            "gps": self.data.gps,
            "gpsFix": self.data.gpsFix,
            "mode": self.data.mode
        }



