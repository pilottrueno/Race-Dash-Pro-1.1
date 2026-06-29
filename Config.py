"""
Race Dash Pro
config.py

Менеджер конфигурации приложения.
"""

from pathlib import Path
import json

class ConfigManager:
    CONFIG_FILE = Path("config.json")

    DEFAULT_CONFIG = {
        "general": {
            "demo_mode": True,
            "fullscreen": True,
            "fps": 60,
            "language": "ru"
        },

        "display": {
            "theme": 0,
            "brightness": 100,
            "night_mode": False
        },

        "dashboard": {
            "max_rpm": 8000,
            "shift_rpm": 7000,
            "warning_rpm": 6500
        },

        "logging": {
            "enabled": True,
            "interval_ms": 1000,
            "max_minutes": 60,
            "sqlite": False
        },

        "gps": {
            "enabled": False,
            "port": "/dev/ttyUSB0",
            "baudrate": 9600
        },

        "ecu": {
            "type": "demo",
            "port": "/dev/ttyUSB0",
            "baudrate": 115200
        }
    }

    def __init__(self):
        self.data = {}
        self.load()

    def load(self):
        """Загрузка конфигурации."""
        if self.CONFIG_FILE.exists():
            try:
                with open(self.CONFIG_FILE, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            except Exception:
                self.data = self.DEFAULT_CONFIG.copy()
                self.save()
        else:
            self.data = self.DEFAULT_CONFIG.copy()
            self.save()

    def save(self):
        """Сохранение конфигурации."""
        with open(self.CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(
                self.data,
                f,
                indent=4,
                ensure_ascii=False
            )

    def get(self, section, key=None):
        """Получить значение."""
        if key is None:
            return self.data.get(section)

        return self.data.get(section, {}).get(key)

    def set(self, section, key, value):
        """Изменить значение."""
        if section not in self.data:
            self.data[section] = {}

        self.data[section][key] = value
        self.save()

    def reset(self):
        """Сбросить настройки."""
        self.data = self.DEFAULT_CONFIG.copy()
        self.save()


