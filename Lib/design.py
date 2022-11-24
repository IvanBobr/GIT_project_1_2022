import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextBrowser
from PyQt5.QtGui import QFont
from datetime import datetime


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.orient_left = True

    def initUI(self):
        self.setGeometry(0, 0, 750, 850)
        self.setWindowTitle('Изменения в расписании')

        self.main_title = QLabel(self)
        self.main_title.setText("ИЗМЕНЕНИЯ В РАСПИСАНИИ")
        self.main_title.setGeometry(10, 10, 401, 20)
        self.main_title.setFont(QFont("Franklin Gothic Demi", 18))

        self.textBrowse = QTextBrowser(self)
        self.textBrowse.setGeometry(180, 41, 561, 751)

        self.button_goMain = QPushButton(self)
        self.button_goMain.setText("На главную")
        self.button_goMain.setGeometry(582, 10, 161, 28)

        self.label_time = QLabel(self)
        self.label_time.setText(datetime.now().strftime("%H:%M"))
        self.label_time.setGeometry(10, 730, 161, 61)
        self.label_time.setFont(QFont("Stencil", 36))

        push_buttons(self)

    def run(self):
        self.label_time.setText(datetime.now().strftime("%H:%M"))


def push_buttons(self):
    self.button_1 = QPushButton(self)
    self.button_2 = QPushButton(self)
    self.button_3 = QPushButton(self)
    self.button_4 = QPushButton(self)
    self.button_5 = QPushButton(self)
    self.button_6 = QPushButton(self)
    self.button_7 = QPushButton(self)
    self.button_8 = QPushButton(self)
    self.button_9 = QPushButton(self)
    self.button_10 = QPushButton(self)
    self.button_11 = QPushButton(self)

    self.button_1.setText("1ые классы")
    self.button_2.setText("2ые классы")
    self.button_3.setText("3е классы")
    self.button_4.setText("4ые классы")
    self.button_5.setText("5ые классы")
    self.button_6.setText("6ые классы")
    self.button_7.setText("7ые классы")
    self.button_8.setText("8ые классы")
    self.button_9.setText("9ые классы")
    self.button_10.setText("10ые классы")
    self.button_11.setText("11ые классы")

    self.button_1.setGeometry(10, 50, 151, 28)
    self.button_2.setGeometry(10, 90, 151, 28)
    self.button_3.setGeometry(10, 130, 151, 28)
    self.button_4.setGeometry(10, 170, 151, 28)
    self.button_5.setGeometry(10, 210, 151, 28)
    self.button_6.setGeometry(10, 250, 151, 28)
    self.button_7.setGeometry(10, 290, 151, 28)
    self.button_8.setGeometry(10, 330, 151, 28)
    self.button_9.setGeometry(10, 370, 151, 28)
    self.button_10.setGeometry(10, 410, 151, 28)
    self.button_11.setGeometry(10, 450, 151, 28)

    self.button_1.setFont(QFont("MS Shell Dlg 2", 10))
    self.button_2.setFont(QFont("MS Shell Dlg 2", 10))
    self.button_3.setFont(QFont("MS Shell Dlg 2", 10))
    self.button_4.setFont(QFont("MS Shell Dlg 2", 10))
    self.button_5.setFont(QFont("MS Shell Dlg 2", 10))
    self.button_6.setFont(QFont("MS Shell Dlg 2", 10))
    self.button_7.setFont(QFont("MS Shell Dlg 2", 10))
    self.button_8.setFont(QFont("MS Shell Dlg 2", 10))
    self.button_9.setFont(QFont("MS Shell Dlg 2", 10))
    self.button_10.setFont(QFont("MS Shell Dlg 2", 10))
    self.button_11.setFont(QFont("MS Shell Dlg 2", 10))

    # self.button_.clicked.connect(lambda x: )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
