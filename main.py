import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from UI_form import UI_Form
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        UI_Form.setupUi()
        self.params = {}
        self.con = sqlite3.connect('data/coffee.db')
        self.pushButton.clicked.connect(self.select)
        self.pushButton_2.clicked.connect(self.update_elems)

    def select(self):
        self.id = self.lineEdit.text()
        req = f'SELECT * FROM Coffees WHERE id = {self.id}'
        cur = self.con.cursor()
        result = cur.execute(req).fetchall()
        if result:
            self.tableWidget.setRowCount(len(result))
            self.tableWidget.setColumnCount(len(result[0]))
            for i, elem in enumerate(result):
                for j, val in enumerate(elem):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        else:
            self.tableWidget.setRowCount(0)
            self.tableWidget.setColumnCount(0)
            
    def update_elems(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        valid = QMessageBox.question(self, '', f'Действительно заменить элементы с id {",".join(ids)}', QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            data = [self.tableWidget.item(0, x).text() for x in range(7)]
            data = [int(x) if x.isnumeric() else x for x in data]
            cur.execute(f'DELETE FROM Coffees where id = {self.id}')
            cur.execute('INSERT INTO Coffees VALUES (?, ?, ?, ?, ?, ?, ?)', data)
            self.con.commit()

    def add_elem(self):
        data = [self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text(), self.lineEdit_7.text()]
        data = [int(x) if x.isnumeric() else x for x in data]
        if all(data):
            cur = self.con.cursor()
            cur.execute('INSERT INTO Coffees (name, roasting, type, description, cost, size) VALUES (?, ?, ?, ?, ?, ?, ?)')
            self.con.commit()

app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())