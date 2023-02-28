import concurrent.futures

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sys
import sqlite3
from PyQt5 import uic

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('Репозитории - доп.задачи 1')
        self.connection = sqlite3.connect('coffee.sqlite')
        self.cursor = self.connection.cursor()
        uic.loadUi('main.ui', self)
        self.unitUi()

    def unitUi(self):
        # Заполнение таблицы
        data = self.cursor.execute('SELECT * FROM info')
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['ID', 'Сорт', 'Обжарка', 'Тип', 'Описание', 'Цена', 'Вес(кг)'])
        for i, row in enumerate(data):
            self.table.setRowCount(
                self.table.rowCount() + 1)
            for j, elem in enumerate(row):
                self.table.setItem(
                    i, j, QTableWidgetItem(str(elem)))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())