import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt5 import uic
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.params = {}
        self.con = sqlite3.connect('coffee.db')
        self.pushButton.clicked.connect(self.select)

    def select(self):
        req = f'SELECT * FROM Coffees WHERE id = {self.lineEdit.text()}'
        cur = self.con.cursor()
        result = cur.execute(req).fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())