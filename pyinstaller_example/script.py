import sys
import os

from PySide2 import QtWidgets


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path)


def main():
    path = resource_path("example.txt")

    with open(path) as file:
        text = file.read()

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QLabel(text)
    window.show()
    app.exec_()
