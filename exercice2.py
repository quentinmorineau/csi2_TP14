from PySide2.QtWidgets import *

class Comment(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Commentaire")
        self.layout = QGridLayout()
        self.label = QLabel("ok")
        self.text = QTextEdit()
        self.button1 = QPushButton("Success")
        self.button2 = QPushButton("Cancel")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)

        
if __name__ == "__main__":
    app = QApplication([])
    a = Comment()
    a.show()
    app.exec_()
