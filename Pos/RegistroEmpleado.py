# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistroEmpleado.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import logolistadoproveedor
import logomodificaralmacen
import InicioAdmin

global nombreloc, apellidoloc, telefonoloc, sexoloc
global db,data
global usex,id

class Ui_RegistroEmpleado(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 514)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(110, 60, 221, 61))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.agregar = QtWidgets.QPushButton(MainWindow)
        self.agregar.setGeometry(QtCore.QRect(130, 340, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);\n"
"")
        self.agregar.setObjectName("agregar")
        self.cancelar = QtWidgets.QPushButton(MainWindow)
        self.cancelar.setGeometry(QtCore.QRect(130, 400, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.nombre = QtWidgets.QTextEdit(MainWindow)
        self.nombre.setGeometry(QtCore.QRect(120, 130, 181, 31))
        self.nombre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.nombre.setObjectName("nombre")
        self.apellido = QtWidgets.QTextEdit(MainWindow)
        self.apellido.setGeometry(QtCore.QRect(120, 180, 181, 31))
        self.apellido.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.apellido.setObjectName("apellido")
        self.telefono = QtWidgets.QTextEdit(MainWindow)
        self.telefono.setGeometry(QtCore.QRect(120, 230, 181, 31))
        self.telefono.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.telefono.setObjectName("telefono")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(50, 170, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(50, 220, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(70, 270, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 81))
        self.label_2.setStyleSheet("image: url(:/logo3/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);\n"
"image: url(:/logoma/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(MainWindow)
        self.comboBox.setGeometry(QtCore.QRect(120, 280, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Registrar empleado</span></p></body></html>"))
        self.agregar.setText(_translate("MainWindow", "Registrar"))
        self.cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nombre(s)</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Apellidos</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Telefono</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Sexo</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Femenino"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Masculino"))
        self.agregar.clicked.connect(self.llamar_a_las_demas)
        self.cancelar.clicked.connect(self.regresar_menu)

    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos2")

    def verificar_usuario_existente(self):
        global nombreloc, apellidoloc, telefonoloc, sexoloc
        global db, data
        global usex,id
        cursor = db.cursor()

        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT EmpleadoId FROM empleado  WHERE Nombre=%s AND Apellido=%s AND Telefono = %s AND Sexo = %s"
        val = (nombreloc, apellidoloc, telefonoloc, sexoloc)
        # procesa una unica linea usando el metodo fetchone().
        cursor.execute(sql, val)

        myresult = cursor.fetchall()
        data = cursor.fetchone()

        if(data==None):
            usex = 0
        else:
            usex = 1
            #sql ="SELECT EmpleadoId from empleado where "
            db.commit()
            id=data
            print("Existente ID")

    def insertar_datos(self):
        global nombreloc, apellidoloc, telefonoloc, sexoloc
        global db, data,usex,id
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
            sql="UPDATE empleado SET Nombre=%s AND Apellido=%s AND Telefono=%s AND Sexo=%s WHERE EmpleadoId=%s"
            val = (nombreloc, apellidoloc, telefonoloc, sexoloc,id)
            cursor.execute(sql,val)
            db.commit()
            data = cursor.fetchone()

            print("Actualizado")


    def tomar_datos(self):
        global nombreloc, apellidoloc, telefonoloc, sexoloc
        nombreloc = ui.nombre.toPlainText()
        apellidoloc = ui.apellido.toPlainText()
        telefonoloc = ui.telefono.toPlainText()
        sexoloc = self.comboBox.currentText()

    def llamar_a_las_demas(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        ui.conectar_bdd()
        ui.tomar_datos()
        ui.verificar_usuario_existente()
        ui.insertar_datos()
        db.close()
        ui.regresar_menu()

    def regresar_menu(self):
        MainWindow2.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_RegistroEmpleado()
    ui.setupUi(MainWindow2)
    MainWindow2.show()
    sys.exit(app.exec_())
