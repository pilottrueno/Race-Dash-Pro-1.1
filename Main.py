import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

from dashboard import DashboardController
from config import ConfigManager

def main():
    app = QApplication(sys.argv)

    config = ConfigManager()
    dashboard = DashboardController(config)

    engine = QQmlApplicationEngine()
    engine.rootContext().setContextProperty("dashboard", dashboard)

    engine.load("qml/dashboard.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()



