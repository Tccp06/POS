# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModificarAcceso.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import logomodificarproveedor
import pymysql
import InicioAdmin

global idloc,usuarioloc, contrasenaloc
global db,data
global acex


class Ui_ModificarAcceso(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(481, 373)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 20, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.id = QtWidgets.QTextEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(200, 110, 161, 31))
        self.id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id.setObjectName("id")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(100, 100, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 150, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(240, 270, 101, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 161, 91))
        self.label_2.setStyleSheet("image: url(:/lmaacc/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(130, 270, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.agregar.setObjectName("agregar")
        self.usuario = QtWidgets.QTextEdit(self.centralwidget)
        self.usuario.setGeometry(QtCore.QRect(200, 160, 161, 31))
        self.usuario.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.usuario.setObjectName("usuario")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 200, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.contrasena = QtWidgets.QTextEdit(self.centralwidget)
        self.contrasena.setGeometry(QtCore.QRect(200, 210, 161, 31))
        self.contrasena.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.contrasena.setObjectName("contrasena")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 481, 26))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Editar permisos</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">EmpleadoID</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Usuario</span></p></body></html>"))
        self.cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.agregar.setText(_translate("MainWindow", "Cambiar"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Contraseña</span></p></body></html>"))
        self.agregar.clicked.connect(self.llamar_a_las_demas)

    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos2")

    def verificar_acceso_existente(self):
        global idloc,usuarioloc, contrasenaloc
        global db, data
        global acex

        cursor = db.cursor()
        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT EmpleadoId FROM acceso  WHERE EmpleadoId=%s"
        val = (idloc)
        # procesa una unica linea usando el metodo fetchone().
        cursor.execute(sql, val)

        data = cursor.fetchone()

        if(data==None):
            acex = 0
        else:
            acex = 1
            db.commit()
            print("Existente ID")

    def insertar_datos(self):
        global idloc,usuarioloc, contrasenaloc
        global db, data,acex
        if(acex!=1):
            cursor = db.cursor()
            sql="INSERT INTO acceso (EmpleadoId,Usuario, Contrasena) VALUES (%s,%s,%s)"
            val = (idloc,usuarioloc, contrasenaloc)
            cursor.execute(sql,val)
            data = cursor.fetchone()
            db.commit()
            print(cursor.rowcount, "record inserted.")
        else:
            cursor = db.cursor()
            sql="UPDATE acceso SET EmpleadoId=%s, Usuario=%s, Contrasena=%s WHERE EmpleadoId=%s"
            val = (idloc,usuarioloc, contrasenaloc,idloc)
            cursor.execute(sql,val)
            db.commit()
            data = cursor.fetchone()

            print("Actualizado")


    def tomar_datos(self):
        global idloc,usuarioloc, contrasenaloc
        idloc = self.id.toPlainText()
        usuarioloc = self.usuario.toPlainText()
        contrasenaloc = self.contrasena.toPlainText()

    def llamar_a_las_demas(self):
        self.conectar_bdd()
        self.tomar_datos()
        self.verificar_acceso_existente()
        self.insertar_datos()
        db.close()
        #self.regresar_menu()

    # def regresar_menu(self):
    #     self.Form = QtWidgets.QWidget()
    #     self.ui = InicioAdmin.Ui_Form()
    #     self.ui.setupUi(self.Form)
    #     self.Form.show()
    #     MainWindow.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ModificarAcceso()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.agregar.clicked.connect(ui.llamar_a_las_demas)
    sys.exit(app.exec_())
