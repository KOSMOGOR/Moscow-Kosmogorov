import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import UI_Form
from random import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        UI_Form.setupUI()
        self.flag = False
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            r, g, b = randint(0, 255), randint(0, 255), randint(0, 255)
            qp.setPen(QColor(r, g, b))
            qp.setBrush(QColor(r, g, b))
            x1 = randint(0, 780)
            y1 = randint(0, 500)
            self.x, self.y = x1, y1
            self.drawEll(qp)
            qp.end()

    def drawEll(self, qp):
        qp.drawEllipse(self.x, self.y, randint(10, 250), randint(10, 250))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())