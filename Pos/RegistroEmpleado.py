# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistroEmpleado.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

global nombreloc, apellidoloc, telefonoloc, sexoloc
global db,data
global usex

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(790, 588)
        Form.setStyleSheet("background-color: rgb(157, 155, 155);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(240, 20, 281, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.agregar = QtWidgets.QPushButton(Form)
        self.agregar.setGeometry(QtCore.QRect(420, 490, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(54, 159, 224);")
        self.agregar.setObjectName("agregar")
        self.cancelar = QtWidgets.QPushButton(Form)
        self.cancelar.setGeometry(QtCore.QRect(610, 490, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.nombre = QtWidgets.QTextEdit(Form)
        self.nombre.setGeometry(QtCore.QRect(180, 160, 191, 41))
        self.nombre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.nombre.setObjectName("nombre")
        self.apellido = QtWidgets.QTextEdit(Form)
        self.apellido.setGeometry(QtCore.QRect(180, 220, 191, 41))
        self.apellido.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.apellido.setObjectName("apellido")
        self.telefono = QtWidgets.QTextEdit(Form)
        self.telefono.setGeometry(QtCore.QRect(180, 280, 191, 41))
        self.telefono.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.telefono.setObjectName("telefono")
        self.sexo = QtWidgets.QTextEdit(Form)
        self.sexo.setGeometry(QtCore.QRect(180, 340, 191, 41))
        self.sexo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.sexo.setObjectName("sexo")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 160, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 220, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 280, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(100, 340, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(580, 0, 161, 151))
        self.label_2.setStyleSheet("image: url(:/logo3/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p>Registro Empleado</p></body></html>"))
        self.agregar.setText(_translate("Form", "Agregar"))
        self.cancelar.setText(_translate("Form", "Cancelar"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">Nombre</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">Apellido</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">Telefono</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">Sexo</span></p></body></html>"))
#import logoempleado_rc

    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos")

    def verificar_usuario_existente(self):
        global nombreloc, apellidoloc, telefonoloc, sexoloc
        global db, data
        global usex
        cursor = db.cursor()

        # ejecuta el SQL query usando el metodo execute().
        cursor.execute("SELECT Nombre,Apellido,Telefono,Sexo FROM empleado  WHERE Nombre = '{0}' AND Apellido = '{1}' AND Telefono = '{2}' AND Sexo = '{3}'".format(nombreloc, apellidoloc, telefonoloc, sexoloc))
        # procesa una unica linea usando el metodo fetchone().
        data = cursor.fetchone()
        if(data!=None):
            usex = 0
            db.commit()
            print("1 registro insertado, ID", cursor.lastrowid)
        else:
            usex = 1

    def tomar_datos(self):
        global nombreloc, apellidoloc, telefonoloc, sexoloc
        nombreloc = ui.nombre.toPlainText()
        apellidoloc = ui.apellido.toPlainText()
        telefonoloc = ui.telefono.toPlainText()
        sexoloc = ui.sexo.toPlainText()

    def llamar_a_las_demas(self):
        ui.conectar_bdd()
        ui.tomar_datos()
        ui.verificar_usuario_existente()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    ui.agregar.clicked.connect(ui.llamar_a_las_demas)
    sys.exit(app.exec_())
