from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Hello(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(400,300)
        self.setWindowTitle("Hello World")
        self.icon = QIcon("fr-flag.png")
        self.setWindowIcon(self.icon)
        self.layout = QVBoxLayout()
        self.label = QLabel("Hello World")
        self.setAlignment(Qt.AlignCenter)
        self.barre = QProgressBar()
        


if __name__ == "__main__":
    app = QApplication([])
    a = Hello()
    a.show()
    app.exec_()
