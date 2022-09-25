# COMPLETE!!!
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
import sys
import pandas as pd


global inp_DATA
global cursor
global sql
global auto
global df


class Ui_Portfolio(object):

    inp_DATA = []
    import sqlite3
    global df


    sql = sqlite3.connect('python.db')
    cur = sql.cursor()
    

    def setupUi(self, Portfolio):
        Portfolio.setObjectName("Portfolio")
        Portfolio.resize(479, 611)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        Portfolio.setFont(font)
        self.centralwidget = QtWidgets.QWidget(Portfolio)
        self.centralwidget.setObjectName("centralwidget")
        self.Surname_editor = QtWidgets.QLineEdit(self.centralwidget)
        self.Surname_editor.setGeometry(QtCore.QRect(160, 60, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Surname_editor.setFont(font)
        self.Surname_editor.setObjectName("Surname_editor")
        self.Name_editor = QtWidgets.QLineEdit(self.centralwidget)
        self.Name_editor.setGeometry(QtCore.QRect(160, 100, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Name_editor.setFont(font)
        self.Name_editor.setObjectName("Name_editor")
        self.LastName_editor = QtWidgets.QLineEdit(self.centralwidget)
        self.LastName_editor.setGeometry(QtCore.QRect(160, 140, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LastName_editor.setFont(font)
        self.LastName_editor.setObjectName("LastName_editor")
        self.Surname_Label = QtWidgets.QLabel(self.centralwidget)
        self.Surname_Label.setGeometry(QtCore.QRect(10, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Surname_Label.setFont(font)
        self.Surname_Label.setObjectName("Surname_Label")
        self.Name_Label = QtWidgets.QLabel(self.centralwidget)
        self.Name_Label.setGeometry(QtCore.QRect(10, 100, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Name_Label.setFont(font)
        self.Name_Label.setObjectName("Name_Label")
        self.LastName_label = QtWidgets.QLabel(self.centralwidget)
        self.LastName_label.setGeometry(QtCore.QRect(10, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LastName_label.setFont(font)
        self.LastName_label.setObjectName("LastName_label")
        self.Date_editor = QtWidgets.QDateEdit(self.centralwidget)
        self.Date_editor.setGeometry(QtCore.QRect(160, 180, 121, 31))
        self.Date_editor.setObjectName("Date_editor")
        self.Date_label = QtWidgets.QLabel(self.centralwidget)
        self.Date_label.setGeometry(QtCore.QRect(10, 180, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Date_label.setFont(font)
        self.Date_label.setObjectName("Date_label")
        self.Main_label = QtWidgets.QLabel(self.centralwidget)
        self.Main_label.setGeometry(QtCore.QRect(10, 10, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Main_label.setFont(font)
        self.Main_label.setObjectName("Main_label")
        self.Class_label = QtWidgets.QLabel(self.centralwidget)
        self.Class_label.setGeometry(QtCore.QRect(10, 220, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Class_label.setFont(font)
        self.Class_label.setObjectName("Class_label")
        self.Bukva_label = QtWidgets.QLabel(self.centralwidget)
        self.Bukva_label.setGeometry(QtCore.QRect(300, 220, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Bukva_label.setFont(font)
        self.Bukva_label.setObjectName("Bukva_label")
        self.Bukva_editor = QtWidgets.QComboBox(self.centralwidget)
        self.Bukva_editor.setGeometry(QtCore.QRect(360, 220, 51, 31))
        self.Bukva_editor.setObjectName("Bukva_editor")
        self.Bukva_editor.addItem("")
        self.Bukva_editor.addItem("")
        self.Bukva_editor.addItem("")
        self.Bukva_editor.addItem("")
        self.Bukva_editor.addItem("")
        self.Bukva_editor.addItem("")
        self.Level_label = QtWidgets.QLabel(self.centralwidget)
        self.Level_label.setGeometry(QtCore.QRect(10, 260, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Level_label.setFont(font)
        self.Level_label.setObjectName("Level_label")
        self.Level_editor = QtWidgets.QComboBox(self.centralwidget)
        self.Level_editor.setGeometry(QtCore.QRect(160, 260, 291, 31))
        self.Level_editor.setObjectName("Level_editor")
        self.Level_editor.addItem("")
        self.Level_editor.addItem("")
        self.Level_editor.addItem("")
        self.Level_editor.addItem("")
        self.Level_editor.addItem("")
        self.Level_editor.addItem("")
        self.Add_button = QtWidgets.QPushButton(self.centralwidget)
        self.Add_button.setGeometry(QtCore.QRect(10, 320, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Add_button.setFont(font)
        self.Add_button.setStyleSheet("background-color: rgb(65, 255, 128);")
        self.Add_button.setObjectName("Add_button")
        self.Class_editor = QtWidgets.QComboBox(self.centralwidget)
        self.Class_editor.setGeometry(QtCore.QRect(160, 220, 71, 31))
        self.Class_editor.setObjectName("Class_editor")
        self.Class_editor.addItem("")
        self.Class_editor.addItem("")
        self.Class_editor.addItem("")
        self.Class_editor.addItem("")
        self.Class_editor.addItem("")
        self.Class_editor.addItem("")
        self.Class_editor.addItem("")
        self.Class_editor.addItem("")
        self.Class_editor.addItem("")
        self.Class_editor.addItem("")
        self.Class_editor.addItem("")
        self.Load_Bt = QtWidgets.QPushButton(self.centralwidget)
        self.Load_Bt.setGeometry(QtCore.QRect(260, 320, 201, 31))
        self.Load_Bt.setObjectName("Load_Bt")
        Portfolio.setCentralWidget(self.centralwidget)

        self.retranslateUi(Portfolio)
        self.Add_button.clicked.connect(self.saver)
        self.Load_Bt.clicked.connect(self.outload)
        QtCore.QMetaObject.connectSlotsByName(Portfolio)

    def outload(self):
        global df
        import pandas as pd
        sql = sqlite3.connect('python.db')
        self.df = pd.read_sql('select * from Data', sql)
        self.df.to_excel(r'result.xlsx', index=False)


    def saver(self):
        import sqlite3
        global df
        sql = sqlite3.connect('python.db')
        cur = sql.cursor
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Data(
            AchievID INTEGER PRIMARY KEY,
            SName TEXT,
            Name TEXT,
            LName TEXT,
            Dat TEXT,
            Clas INT,
            Lit TEXT,
            Levl TEXT);
            """)
        self.sql.commit()
        global inp_DATA
        inp_DATA = []
        sur = self.Surname_editor.text()
        nam = self.Name_editor.text()
        las = self.LastName_editor.text()
        date = self.Date_editor.text()
        clas = self.Class_editor.currentText()
        lit = self.Bukva_editor.currentText()
        lev = self.Level_editor.currentText()
        inp_DATA.append(sur)
        inp_DATA.append(nam)
        inp_DATA.append(las)
        inp_DATA.append(date)
        inp_DATA.append(int(clas))
        inp_DATA.append(lit)
        inp_DATA.append(lev)
        self.cur.execute(f'''INSERT INTO Data (SName, Name, LName, Dat, Clas, Lit, Levl) VALUES(?, ?, ?, ?, ?, ?, ?)''', inp_DATA)
        self.sql.commit()
  


    def retranslateUi(self, Portfolio):
        _translate = QtCore.QCoreApplication.translate
        Portfolio.setWindowTitle(_translate("Portfolio", "Portfolio_editor"))
        self.Surname_Label.setText(_translate("Portfolio", "Фамилия"))
        self.Name_Label.setText(_translate("Portfolio", "Имя"))
        self.LastName_label.setText(_translate("Portfolio", "Отчество"))
        self.Date_label.setText(_translate("Portfolio", "Дата участия"))
        self.Main_label.setText(_translate("Portfolio", "Добавить достижение ученика"))
        self.Class_label.setText(_translate("Portfolio", "Класс"))
        self.Bukva_label.setText(_translate("Portfolio", "Буква"))
        self.Bukva_editor.setItemText(0, _translate("Portfolio", "А"))
        self.Bukva_editor.setItemText(1, _translate("Portfolio", "Б"))
        self.Bukva_editor.setItemText(2, _translate("Portfolio", "В"))
        self.Bukva_editor.setItemText(3, _translate("Portfolio", "Г"))
        self.Bukva_editor.setItemText(4, _translate("Portfolio", "Д"))
        self.Bukva_editor.setItemText(5, _translate("Portfolio", "Е"))
        self.Level_label.setText(_translate("Portfolio", "Уровень участия"))
        self.Level_editor.setItemText(0, _translate("Portfolio", "Школьная"))
        self.Level_editor.setItemText(1, _translate("Portfolio", "Городская"))
        self.Level_editor.setItemText(2, _translate("Portfolio", "Муниципальная"))
        self.Level_editor.setItemText(3, _translate("Portfolio", "Региональная"))
        self.Level_editor.setItemText(4, _translate("Portfolio", "Всероссийская"))
        self.Level_editor.setItemText(5, _translate("Portfolio", "Международная"))
        self.Add_button.setText(_translate("Portfolio", "Добавить достижение"))
        self.Class_editor.setItemText(0, _translate("Portfolio", "1"))
        self.Class_editor.setItemText(1, _translate("Portfolio", "2"))
        self.Class_editor.setItemText(2, _translate("Portfolio", "3"))
        self.Class_editor.setItemText(3, _translate("Portfolio", "4"))
        self.Class_editor.setItemText(4, _translate("Portfolio", "5"))
        self.Class_editor.setItemText(5, _translate("Portfolio", "6"))
        self.Class_editor.setItemText(6, _translate("Portfolio", "7"))
        self.Class_editor.setItemText(7, _translate("Portfolio", "8"))
        self.Class_editor.setItemText(8, _translate("Portfolio", "9"))
        self.Class_editor.setItemText(9, _translate("Portfolio", "10"))
        self.Class_editor.setItemText(10, _translate("Portfolio", "11"))
        self.Load_Bt.setText(_translate("Portfolio", "Выгрузить всю таблицу"))






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Portfolio = QtWidgets.QMainWindow()
    ui = Ui_Portfolio()
    ui.setupUi(Portfolio)
    Portfolio.show()
    sys.exit(app.exec_())
