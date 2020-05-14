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
        self.label.setAlignment(Qt.AlignCenter)
        self.barre = QProgressBar()
        self.barre.setValue(75)
        self.line = QLineEdit()
        self.button = QPushButton("Cliquer ici !")
        self.button.setToolTip("Oui oui, ici !")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.barre)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        


if __name__ == "__main__":
    app = QApplication([])
    a = Hello()
    a.show()
    app.exec_()
