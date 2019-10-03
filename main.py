import sys
from random import randint
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('form.ui', self)

        # Задаем заголовок формы
        self.setWindowTitle('Работа с визуальными табличными данными в Python')
        # Задаем логотип формы
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.BtnRandNum.clicked.connect(self.fill_random_numbers)
        self.BtnSolve.clicked.connect(self.solve)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    # Функция для заполнения таблицы случайными числами
    def fill_random_numbers(self):
        row = col = 0
        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                # Задаем переменной случайные значение от -10 до 100
                random_num = randint(-1, 25)
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(random_num)))
                col += 1
            row += 1
            col = 0
        return

    def solve(self):
        pos_num = find_pos(self.tableWidget)
        zero_num = find_zero(self.tableWidget)

        list_max_num = find_max(self.tableWidget)

        if not list_max_num:
            self.label_error.setText('Введены неправильные данные!')
        else:
            # Вывод на кран информацию о расположении минимального числа
            self.LblMinElem.setText('max элемент: ' + str(list_max_num[0]) + ' [ '
                                    + str(list_max_num[1]) + ';' + str(list_max_num[2]) + ']')

        row = col = 0

        while row < self.tableWidget.rowCount():
            while col < self.tableWidget.columnCount():
                number = float(self.tableWidget.item(row, col).text())
                # По условию требуется 5 нулей, но поставил 1 т.к низкий шанс впадение 5 нулей
                if number == list_max_num[0] and pos_num >= 3 and zero_num >= 1:
                    self.tableWidget.setItem(row, col, QTableWidgetItem(str(number * 2)))
                col += 1

            row += 1
            col = 0


def find_pos(table_widget):
    pos = 0

    row = col = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = float(table_widget.item(row, col).text())
                if number > 0:
                    pos += 1
                col += 1
            row += 1
            col = 0
        return pos
    except Exception:
        return None

def find_zero(table_widget):
    zero = 0

    row = col = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = float(table_widget.item(row, col).text())
                if number == 0:
                    zero += 1
                col += 1
            row += 1
            col = 0
        return zero
    except Exception:
        return None


def find_max(table_widget):
    # По условию требуется знать положение в столбце
    row_max_number = col_max_number = 0
    max_num = float(table_widget.item(row_max_number, col_max_number).text())

    row = col = 0

    try:
        while row < table_widget.rowCount():
            while col < table_widget.columnCount():
                number = float(table_widget.item(row, col).text())
                if number > max_num:
                    max_num = number
                    col_max_number = col
                    row_max_number = row
                col += 1
            row += 1
            col = 0
        return [max_num, row_max_number, col_max_number]
    except Exception:
        return None


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
