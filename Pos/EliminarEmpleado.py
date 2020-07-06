# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EliminarEmpleado.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import pymysql
import logoproducto
import InicioAdmin

global nombreloc, descripcionloc, proveedorloc, preciounven, preciouncom
global db,data
global id
import logoeliminarcompra

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(767, 587)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 111, 71))
        self.label_2.setStyleSheet("image: url(:/logo10/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.nombre = QtWidgets.QTextEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(160, 150, 191, 31))
        self.nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombre.setObjectName("nombre")
        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(370, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.agregar.setObjectName("agregar")
        self.eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.eliminar.setGeometry(QtCore.QRect(590, 430, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.eliminar.setFont(font)
        self.eliminar.setStyleSheet("background-color: rgb(247, 33, 33);")
        self.eliminar.setObjectName("eliminar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 90, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.ID = QtWidgets.QTextEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(160, 100, 191, 31))
        self.ID.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ID.setObjectName("ID")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 140, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(590, 490, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(255, 101, 103);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 210, 631, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Bahnschrift Condensed\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 767, 26))
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
        self.agregar.setText(_translate("MainWindow", "Buscar"))
        self.eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">ID de empleado</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nombre</span></p></body></html>"))
        self.cancelar.setText(_translate("MainWindow", "Atrás"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellido"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Sexo"))

    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos")

    def datos_tabla(self):
        global datos,data
        self.datos = []
        self.datos.append((data))

    def agregar_datos_tabla(self):
        global datos, tableWidget
        fila = 0
        for registro in self.datos:
            columna = 0
            ui.tableWidget.insertRow(fila)
            for elemento in registro:
                celda = QTableWidgetItem(elemento)
                ui.tableWidget.setItem(fila,columna,celda)
                columna+=1
            fila +=1

    def eliminar_registro(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        global db, data,id
        ui.tomar_datos()
        cursor = db.cursor()
        sql = "DELETE FROM empleado WHERE EmpleadoId = %s"
        val = (id)
        cursor.execute(sql, val)
        data = cursor.fetchone()


    def verificar_producto_exist(self):
        #se verificara que los parametros que paso el usuario no existan ya en la bdd y si es asi solo se actualizaran
        #o se mostrara una advertencia al usuario del caso.
        global db, data
        global id

        cursor = db.cursor()
        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT Nombre,Apellido,Sexo FROM empleado WHERE EmpleadoId = %s"
        val = (id)
        cursor.execute(sql, val)
        #myresult = cursor.fetchall()
        data = cursor.fetchone()

    def tomar_datos(self):
        global id
        id = ui.ID.toPlainText()

    def llamar_a_las_demas(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        ui.conectar_bdd()
        ui.tomar_datos()
        ui.verificar_producto_exist()
        ui.datos_tabla()
        ui.agregar_datos_tabla()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.agregar.clicked.connect(ui.llamar_a_las_demas)
    ui.eliminar.clicked.connect(ui.eliminar_registro)
    sys.exit(app.exec_())
