# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModificarEmpleado.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import InicioAdmin

global idloc,nombreloc, apellidoloc, telefonoloc, sexoloc
global db,data
global usex

class Ui_ModificarEmpleado(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(415, 542)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.id = QtWidgets.QTextEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(130, 100, 171, 31))
        self.id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id.setObjectName("id")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 90, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 140, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.apellido = QtWidgets.QTextEdit(self.centralwidget)
        self.apellido.setGeometry(QtCore.QRect(130, 200, 171, 31))
        self.apellido.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.apellido.setObjectName("apellido")
        self.nombre = QtWidgets.QTextEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(130, 150, 171, 31))
        self.nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombre.setObjectName("nombre")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 30, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(150, 420, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(150, 360, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.agregar.setObjectName("agregar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 190, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 240, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(130, 300, 171, 31))
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 290, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 81, 61))
        self.label_2.setStyleSheet("image: url(:/logoma/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.telefono = QtWidgets.QTextEdit(self.centralwidget)
        self.telefono.setGeometry(QtCore.QRect(130, 250, 171, 31))
        self.telefono.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.telefono.setObjectName("telefono")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 26))
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
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">EmpleadoID</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nombre</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Editar empleados</span></p><p><br/></p></body></html>"))
        self.cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.agregar.setText(_translate("MainWindow", "Editar"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Apellido</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Teléfono</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Sexo</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Femenino"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Masculino"))
        self.agregar.clicked.connect(self.llamar_a_las_demas)

    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos2")

    def verificar_usuario_existente(self):
        global idloc,nombreloc, apellidoloc, telefonoloc, sexoloc
        global db, data
        global usex

        cursor = db.cursor()

        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT EmpleadoId FROM empleado  WHERE EmpleadoId=%s"
        val = (idloc)
        # procesa una unica linea usando el metodo fetchone().
        cursor.execute(sql, val)

        data = cursor.fetchone()

        if(data==None):
            usex = 0
        else:
            usex = 1
            db.commit()
            print("Existente ID")

    def insertar_datos(self):
        global idloc,nombreloc, apellidoloc, telefonoloc, sexoloc
        global db, data,usex
        if(usex!=1):
            cursor = db.cursor()
            sql="INSERT INTO empleado (Nombre,Apellido,Telefono,Sexo) VALUES (%s,%s,%s,%s)"
            val = (nombreloc, apellidoloc, telefonoloc, sexoloc)
            cursor.execute(sql,val)
            data = cursor.fetchone()
            db.commit()
            print(cursor.rowcount, "record inserted.")
        else:
            cursor = db.cursor()
            sql="UPDATE empleado SET Nombre=%s, Apellido=%s, Telefono=%s, Sexo=%s WHERE EmpleadoId=%s"
            val = (nombreloc, apellidoloc, telefonoloc, sexoloc,idloc)
            cursor.execute(sql,val)
            db.commit()
            data = cursor.fetchone()

            print("Actualizado")


    def tomar_datos(self):
        global idloc,nombreloc, apellidoloc, telefonoloc, sexoloc
        idloc = self.id.toPlainText()
        nombreloc = self.nombre.toPlainText()
        apellidoloc = self.apellido.toPlainText()
        telefonoloc = self.telefono.toPlainText()
        sexoloc = self.comboBox.currentText()

    def llamar_a_las_demas(self):
        self.conectar_bdd()
        self.tomar_datos()
        self.verificar_usuario_existente()
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
    ui = Ui_ModificarEmpleado()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
