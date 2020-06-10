# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class DataBase:
    db = pymysql.connect("localhost","root","","pos")
    ##################################################

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # ejecuta el SQL query usando el metodo execute().
    cursor.execute("SELECT VERSION()")

    # procesa una unica linea usando el metodo fetchone().
    data = cursor.fetchone()
    print ("Database version : {0}".format(data))


def validarUser(usuario,contrasena):
    sql = 'SELECT contrasena FROM acceso WHERE Usuario = {usuario}'.format(id)
    try:
            self.cursor.execute(sql)
            user = selft.cursor.fetchone()
            if(contrasena!=user[0]):
                print("Error")
        #except Exception as e:
         #   raise



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(157, 155, 155);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(300, 20, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, -30, 231, 211))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 200, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 260, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.usuario = QtWidgets.QTextEdit(self.centralwidget)
        self.usuario.setGeometry(QtCore.QRect(310, 210, 241, 41))
        self.usuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.usuario.setObjectName("usuario")
        self.contrasena = QtWidgets.QTextEdit(self.centralwidget)
        self.contrasena.setGeometry(QtCore.QRect(310, 270, 241, 41))
        self.contrasena.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contrasena.setObjectName("contrasena")
        self.ingresar = QtWidgets.QPushButton(self.centralwidget)
        self.ingresar.setGeometry(QtCore.QRect(230, 390, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.ingresar.setFont(font)
        self.ingresar.setStyleSheet("background-color: rgb(54, 159, 224);")
        self.ingresar.setObjectName("ingresar")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(410, 390, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Bienvenido </span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/cct/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png\"/></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">Usuario</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:26pt;\">Contraseña</span></p></body></html>"))
        self.ingresar.setText(_translate("MainWindow", "Ingresar"))
        self.cancelar.setText(_translate("MainWindow", "Cancelar"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    database = DataBase()
    database.validarUser(usuario,contrasena)
    sys.exit(app.exec_())


# desconecta del servidor
db.close()
