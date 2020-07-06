# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BuscarProducto.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import logoproductobuscar

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import InicioEmpleado
import pymysql

global idLocal, nombreLoc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(607, 554)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 130, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(150, 200, 303, 211))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Bahnschrift Condensed\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        item.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)


        # self.tableView = QtWidgets.QTableView(self.centralwidget)
        # self.tableView.setGeometry(QtCore.QRect(50, 200, 451, 211))
        # self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.tableView.setObjectName("tableView")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.nombre = QtWidgets.QTextEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(140, 140, 191, 31))
        self.nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombre.setObjectName("nombre")
        self.ID = QtWidgets.QTextEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(140, 90, 191, 31))
        self.ID.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ID.setObjectName("ID")
        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(370, 90, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.agregar.setObjectName("agregar")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(340, 440, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -10, 121, 81))
        self.label_2.setStyleSheet("image: url(:/logo7/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 607, 26))
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nombre</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">ID de producto</span></p></body></html>"))
        self.agregar.setText(_translate("MainWindow", "Buscar"))
        self.cancelar.setText(_translate("MainWindow", "Atrás"))

        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ProductoId"))

        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))

        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Descripcion"))

        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "CategoriaId"))

        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ProveedorId"))

        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "PrecioUnitarioVenta"))

        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "PrecioUnitarioCompra"))

        self.agregar.clicked.connect(ui.llamar_a_las_demas)
        self.cancelar.clicked.connect(ui.other)
    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos")

    def tomar_datos(self):
        global idLocal, nombreLoc

        idLocal = ui.ID.toPlainText()
        nombreLoc = ui.nombre.toPlainText()

    def verificar_producto_exist(self):
        #se verificara que los parametros que paso el usuario no existan ya en la bdd y si es asi solo se actualizaran
        #o se mostrara una advertencia al usuario del caso.
        global idLocal, data
        cursor = db.cursor()

        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT ProductoId, Nombre, Descripcion, CategoriaId, ProveedorId, PrecioUnitarioVenta, PrecioUnitarioCompra  FROM producto WHERE ProductoId = %s OR Nombre = %s"
        val = (idLocal, nombreLoc)

        cursor.execute(sql, val)
        data = cursor.fetchone()

        if(data==None):
            prodex = 0
            print("Esta compra nunca fue hecha")
            print(data)
        else:
            prodex = 1
            db.commit()
            idLocal=data
            print("Ahi stan los datos")
        
    def datos_tabla(self):
        global datos, data
        self.datos = []
        self.datos.append((data))

    def agregar_datos_tabla(self):
        global datos, tableWidget
        fila = 0
        for registro in self.datos:
            columna = 0
            ui.tableWidget.insertRow(fila)
            for elemento in registro:
                elemento = str(elemento)
                celda = QTableWidgetItem(elemento)
                ui.tableWidget.setItem(fila,columna,celda)
                columna+=1
            fila +=1
    def llamar_a_las_demas(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        ui.conectar_bdd()
        ui.tomar_datos()
        ui.verificar_producto_exist()
        ui.datos_tabla()
        ui.agregar_datos_tabla()
    #Abrir otra ventana
    def other(self):
        self.MainWindow2 = QtWidgets.QMainWindow()
        self.ui = InicioEmpleado.Ui_MainWindowEmpleado()
        self.ui.setupUi(self.MainWindow2)
        self.MainWindow2.show()
        MainWindow.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
