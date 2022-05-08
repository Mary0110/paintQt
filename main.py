import sys
from PyQt6.QtWidgets import QApplication
from UI.window import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())