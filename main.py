"""Основной файл программы, предназначенный для запуска приложения"""
from PyQt5.QtWidgets import QApplication

import front
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = front.Ui_MainWindow()
    window.show()
    sys.exit(app.exec())
