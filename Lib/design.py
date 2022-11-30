import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QComboBox
from PyQt5.QtWidgets import QLabel, QLineEdit, QTextBrowser, QTextEdit, QInputDialog
from PyQt5.QtGui import QFont
from datetime import datetime
import docx
import sqlite3
from PyQt5.QtCore import Qt


class WINDOW_IZM(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.orient_left = True

    def initUI(self):
        self.setGeometry(0, 0, 784, 850)
        self.setWindowTitle('Изменения в расписании')

        self.main_title = QLabel(self)
        self.main_title.setText("ИЗМЕНЕНИЯ В РАСПИСАНИИ")
        self.main_title.setGeometry(10, 10, 401, 20)
        self.main_title.setFont(QFont("Franklin Gothic Demi", 18))

        self.textBrowse = QTextBrowser(self)
        self.textBrowse.setGeometry(180, 41, 601, 751)
        self.textBrowse.setFont(QFont("Franklin Gothic Demi", 14))

        self.button_goMain = QPushButton(self)
        self.button_goMain.setText("На главную")
        self.button_goMain.setGeometry(620, 10, 161, 28)
        self.button_goMain.clicked.connect(lambda x: self.run("_0_"))

        self.label_time = QLabel(self)
        self.label_time.setText(datetime.now().strftime("%H:%M"))
        self.label_time.setGeometry(10, 730, 161, 61)
        self.label_time.setFont(QFont("Stencil", 36))

        push_buttons(self)

    def run(self, key_sort):
        if key_sort != "_0_":
            self.label_time.setText(datetime.now().strftime("%H:%M"))
            self.textBrowse.setText(read_from_word_doc(key_sort))
        else:
            ex = WINDOW_MAIN()
            ex.show()
            self.close()


class WINDOW_MAIN(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.orient_left = True

    def initUI(self):
        self.setGeometry(0, 0, 784, 308)
        self.setWindowTitle('ГЛАВНАЯ')

        self.title = QLabel(self)
        self.title.setText("ГЛАВНАЯ")
        self.title.setFont(QFont("Franklin Gothic Demi", 36))
        self.title.setGeometry(10, 10, 251, 51)

        self.label_time = QLabel(self)
        self.label_time.setText(datetime.now().strftime("%H:%M"))
        self.label_time.setGeometry(620, 0, 161, 61)
        self.label_time.setFont(QFont("Stencil", 36))

        self.button_RASP = QPushButton(self)
        self.button_RASP.setText("РАСПИСАНИЕ")
        self.button_RASP.setFont(QFont("Segoe Print", 20))
        self.button_RASP.setGeometry(110, 80, 571, 41)
        self.button_RASP.clicked.connect(lambda x: self.run(1))

        self.button_IZM = QPushButton(self)
        self.button_IZM.setText("ИЗМЕНЕНИЯ В РАСПИСАНИИ")
        self.button_IZM.setFont(QFont("Segoe Print", 20))
        self.button_IZM.setGeometry(110, 140, 571, 41)
        self.button_IZM.clicked.connect(lambda x: self.run(2))

        self.button_NOTES = QPushButton(self)
        self.button_NOTES.setText("ЗАМЕТКИ")
        self.button_NOTES.setFont(QFont("Segoe Print", 20))
        self.button_NOTES.setGeometry(110, 200, 571, 41)
        self.button_NOTES.clicked.connect(lambda x: self.run(3))

    def run(self, key_what):
        self.label_time.setText(datetime.now().strftime("%H:%M"))
        if key_what == 1:
            ex = WINDOW_RASP1()
            ex.show()
            self.close()
        elif key_what == 2:
            ex = WINDOW_IZM()
            ex.show()
            self.close()
        elif key_what == 3:
            ex = WINDOW_ZAM()
            ex.show()
            self.close()

    def keyPressEvent(self, event):
        if int(event.modifiers()) == (Qt.AltModifier + Qt.ShiftModifier):
            if event.key() == Qt.Key_Q:
                ex = WINDOW_COMMANDS()
                ex.show()
                self.close()


class WINDOW_ZAM(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.orient_left = True

    def initUI(self):
        self.setGeometry(0, 0, 784, 854)
        self.setWindowTitle("ЗАМЕТКИ")

        self.title = QLabel(self)
        self.title.setText("ЗАМЕТКИ")
        self.title.setFont(QFont("Franklin Gothic Demi", 36))
        self.title.setGeometry(10, 10, 261, 51)

        self.label_time = QLabel(self)
        self.label_time.setText(datetime.now().strftime("%H:%M"))
        self.label_time.setGeometry(620, 0, 161, 61)
        self.label_time.setFont(QFont("Stencil", 36))

        self.go_main = QPushButton(self)
        self.go_main.setText("На главную")
        self.go_main.setGeometry(620, 60, 151, 28)
        self.go_main.clicked.connect(lambda x: self.run("main"))

        self.inputPlace = QTextEdit(self)
        self.inputPlace.setGeometry(10, 110, 321, 681)

        self.outputPlace = QTextBrowser(self)
        self.outputPlace.setGeometry(340, 90, 431, 701)

        self.open = QPushButton(self)
        self.open.setText("ОТКРЫТЬ")
        self.open.setGeometry(10, 80, 81, 28)
        self.open.clicked.connect(lambda x: self.run("open"))

        self.create = QPushButton(self)
        self.create.setText("СОЗДАТЬ")
        self.create.setGeometry(90, 80, 81, 28)
        self.create.clicked.connect(lambda x: self.run("create new"))

        self.save = QPushButton(self)
        self.save.setText("СОХРАНИТЬ")
        self.save.setGeometry(170, 80, 81, 28)
        self.save.clicked.connect(lambda x: self.run("save"))

        self.delete = QPushButton(self)
        self.delete.setText("УДАЛИТЬ")
        self.delete.setGeometry(250, 80, 81, 28)
        self.delete.clicked.connect(lambda x: self.run("delete"))

    def run(self, key):
        self.label_time.setText(datetime.now().strftime("%H:%M"))
        if key == "create new":
            self.inputPlace.setText("")
            self.outputPlace.setText("")
        elif key == "save":
            name, ok_pressed = QInputDialog.getText(self, "Сохранение...",
                                                    "Введите название")
            if ok_pressed:
                con = sqlite3.connect("zametki.db")
                cur = con.cursor()

                wht_add = self.inputPlace.toPlainText()
                time_added = datetime.now().strftime("%D %H:%M")
                cur.execute(f"""INSERT INTO main VALUES ('{name}', '{time_added}', '{wht_add}')""").fetchall()
                con.commit()
                con.close()
        elif key == "open":
            name, ok_pressed = QInputDialog.getText(self, "Открываем...", "Введите название")
            # self.inputPlace.setText("") НУЖНО ЛИ???
            if ok_pressed:
                con = sqlite3.connect("zametki.db")
                cur = con.cursor()

                textResult = cur.execute(f"""SELECT zn from main WHERE name = '{name}'""").fetchall()

                if textResult:
                    self.outputPlace.setText(textResult[0][0])
                else:
                    self.outputPlace.setText("Ничего не найдено :(")

                con.commit()
                con.close()
        elif key == "delete":
            name, ok_pressed = QInputDialog.getText(self, "Удаляем...", "Введите название")
            if ok_pressed:
                con = sqlite3.connect("zametki.db")
                cur = con.cursor()

                cur.execute(f"""DELETE from main WHERE name = '{name}'""").fetchall()
                con.commit()
                con.close()
        elif key == "main":
            ex = WINDOW_MAIN()
            ex.show()
            self.close()


class WINDOW_RASP1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.orient_left = True

    def initUI(self):
        self.setGeometry(0, 0, 784, 367)
        self.setWindowTitle('РАСПИСАНИЕ')

        self.title = QLabel(self)
        self.title.setText("РАСПИСАНИЕ")
        self.title.setFont(QFont("Franklin Gothic Demi", 36))
        self.title.setGeometry(10, 10, 371, 51)

        self.label_time = QLabel(self)
        self.label_time.setText(datetime.now().strftime("%H:%M"))
        self.label_time.setGeometry(620, 0, 161, 61)
        self.label_time.setFont(QFont("Stencil", 36))

        self.button_RASP = QPushButton(self)
        self.button_RASP.setText("ОТКРЫТЬ ПОЛНОЕ")
        self.button_RASP.setFont(QFont("Segoe Print", 20))
        self.button_RASP.setGeometry(30, 80, 721, 41)
        self.button_RASP.clicked.connect(lambda x: self.run(1))

        self.button_IZM = QPushButton(self)
        self.button_IZM.setText("ОТКРЫТЬ ПО КЛАССАМ")
        self.button_IZM.setFont(QFont("Segoe Print", 20))
        self.button_IZM.setGeometry(30, 140, 721, 41)
        self.button_IZM.clicked.connect(lambda x: self.run(2))

        self.button_NOTES = QPushButton(self)
        self.button_NOTES.setText("ОТКРЫТЬ ВМЕСТЕ С ИЗМЕНЕНИЯМИ")
        self.button_NOTES.setFont(QFont("Segoe Print", 20))
        self.button_NOTES.setGeometry(30, 200, 721, 41)
        self.button_NOTES.clicked.connect(lambda x: self.run(3))

        self.button_goMain = QPushButton(self)
        self.button_goMain.setText("НА ГЛАВНУЮ")
        self.button_goMain.setFont(QFont("Segoe Print", 20))
        self.button_goMain.setGeometry(30, 260, 721, 41)
        self.button_goMain.clicked.connect(lambda x: self.run("main"))

    def run(self, key_what):
        self.label_time.setText(datetime.now().strftime("%H:%M"))
        if key_what == "main":
            ex = WINDOW_MAIN()
            ex.show()
            self.close()
        elif key_what == 1:
            pass  # тут будет класс с изм
        elif key_what == 2:
            pass  # тут будет класс с изм
        elif key_what == 3:
            pass  # тут будет класс с изм

class WINDOW_RASPmain(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.orient_left = True

    def initUI(self):
        self.setGeometry(0, 0, 784, 367)
        self.setWindowTitle('РАСПИСАНИЕ')

        self.title = QLabel(self)
        self.title.setText("РАСПИСАНИЕ")
        self.title.setFont(QFont("Franklin Gothic Demi", 36))
        self.title.setGeometry(10, 10, 371, 51)

        self.label_time = QLabel(self)
        self.label_time.setText(datetime.now().strftime("%H:%M"))
        self.label_time.setGeometry(620, 0, 161, 61)
        self.label_time.setFont(QFont("Stencil", 36))

        self.button_RASP = QPushButton(self)
        self.button_RASP.setText("ОТКРЫТЬ ПОЛНОЕ")
        self.button_RASP.setFont(QFont("Segoe Print", 20))
        self.button_RASP.setGeometry(30, 80, 721, 41)
        self.button_RASP.clicked.connect(lambda x: self.run(1))

        self.button_IZM = QPushButton(self)
        self.button_IZM.setText("ОТКРЫТЬ ПО КЛАССАМ")
        self.button_IZM.setFont(QFont("Segoe Print", 20))
        self.button_IZM.setGeometry(30, 140, 721, 41)
        self.button_IZM.clicked.connect(lambda x: self.run(2))

        self.button_NOTES = QPushButton(self)
        self.button_NOTES.setText("ОТКРЫТЬ ВМЕСТЕ С ИЗМЕНЕНИЯМИ")
        self.button_NOTES.setFont(QFont("Segoe Print", 20))
        self.button_NOTES.setGeometry(30, 200, 721, 41)
        self.button_NOTES.clicked.connect(lambda x: self.run(3))

        self.button_goMain = QPushButton(self)
        self.button_goMain.setText("НА ГЛАВНУЮ")
        self.button_goMain.setFont(QFont("Segoe Print", 20))
        self.button_goMain.setGeometry(30, 260, 721, 41)
        self.button_goMain.clicked.connect(lambda x: self.run("main"))

    def run(self, key_what):
        self.label_time.setText(datetime.now().strftime("%H:%M"))
        if key_what == "main":
            ex = WINDOW_MAIN()
            ex.show()
            self.close()
        elif key_what == 1:
            pass  # тут будет класс с изм
        elif key_what == 2:
            pass  # тут будет класс с изм
        elif key_what == 3:
            pass  # тут будет класс с изм

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

    self.button_1.clicked.connect(lambda x: self.run("1-"))
    self.button_2.clicked.connect(lambda x: self.run("2-"))
    self.button_3.clicked.connect(lambda x: self.run("3-"))
    self.button_4.clicked.connect(lambda x: self.run("4-"))
    self.button_5.clicked.connect(lambda x: self.run("5-"))
    self.button_6.clicked.connect(lambda x: self.run("6-"))
    self.button_7.clicked.connect(lambda x: self.run("7-"))
    self.button_8.clicked.connect(lambda x: self.run("8-"))
    self.button_9.clicked.connect(lambda x: self.run("9-"))
    self.button_10.clicked.connect(lambda x: self.run("10-"))
    self.button_11.clicked.connect(lambda x: self.run("11-"))

class WINDOW_COMMANDS(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.orient_left = True

    def initUI(self):
        self.setGeometry(0, 0, 547, 832)
        self.setWindowTitle('КОМАНДНАЯ СТРОКА')

        self.command_input = QTextEdit(self)
        self.command_input.setGeometry(10, 10, 521, 761)

        self.button_send = QPushButton(self)
        self.button_send.setText("ОТПРАВИТЬ")
        self.button_send.setGeometry(430, 730, 93, 31)
        self.button_send.clicked.connect(self.run)
    def run(self):
        command = self.command_input.toPlainText()
        if command == "back":
            ex = WINDOW_MAIN()
            ex.show()
            self.close()
        else:
            con = sqlite3.connect("zametki.db")
            cur = con.cursor()

            cur.execute(command).fetchall()
            con.commit()
            con.close()

def read_from_word_doc(key_sort, name="IZM.docx"):
    document = docx.Document(name)
    string_return = ""
    for par in document.paragraphs:
        if key_sort in par.text:
            for_new_str = par.text.split()
            new_string = for_new_str[0] + " " + for_new_str[1] + "  " + for_new_str[2] + "   " + " ".join(
                for_new_str[3:])
            string_return += new_string + "\n\n"
    return string_return



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WINDOW_MAIN()
    ex.show()
    sys.exit(app.exec())
