from PyQt6.QtWidgets import QWidget


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_widgets()

    def init_widgets(self):
        self.setWindowTitle('Nice useless paint')
        self.setGeometry(150, 100, 900, 600)
        self.setFixedSize(self.size())

        self.show()
