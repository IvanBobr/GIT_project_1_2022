import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.orient_left = True

    def initUI(self):
        self.setGeometry(750, 850, 400, 50)
        self.setWindowTitle('Изменения в расписании')

        self.main_title = QLabel(self)
        self.main_title.setText("ИЗМЕНЕНИЯ В РАСПИСАНИИ")
        self.main_title.setGeometry(10, 10, 401, 20)
        self.main_title.setFont(QFont("Franklin Gothic Demi", 18))

    def run(self):
        if self.orient_left:
            self.btn.setText("<-")
            self.input_1.setText(self.input_2.text())
            self.input_2.setText("")
            self.orient_left = False
        else:
            self.btn.setText("->")
            self.input_2.setText(self.input_1.text())
            self.input_1.setText("")
            self.orient_left = True


def start():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Example()
        ex.show()
        sys.exit(app.exec())
