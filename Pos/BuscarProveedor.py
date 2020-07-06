# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BuscarProveedor.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import logoproveedorbuscar
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import pymysql
import InicioEmpleado

global idLocal, nombreloc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 561)
        MainWindow.setStyleSheet("\n"
"background-color: rgb(247, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ID = QtWidgets.QTextEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(150, 90, 191, 31))
        self.ID.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ID.setObjectName("ID")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 130, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(450, 460, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")

        # self.tableView = QtWidgets.QTableView(self.centralwidget)
        # self.tableView.setGeometry(QtCore.QRect(40, 200, 521, 192))
        # self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        # self.tableView.setObjectName("tableView")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(50, 210, 411, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Bahnschrift Condensed\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
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

        self.nombre = QtWidgets.QTextEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(150, 140, 191, 31))
        self.nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombre.setObjectName("nombre")
        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(370, 90, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.agregar.setObjectName("agregar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 80, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, -10, 131, 91))
        self.label_2.setStyleSheet("image: url(:/logo8/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 26))
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
        self.cancelar.setText(_translate("MainWindow", "Atrás"))
        self.agregar.setText(_translate("MainWindow", "Buscar"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">ID de proveedor</span></p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ProveedorId"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Direccion"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Telefono"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Empresa"))
        self.cancelar.clicked.connect(ui.other)
        


    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos")

    def tomar_datos(self):
        global idLocal, nombreloc

        idLocal = ui.ID.toPlainText()
        nombreloc = ui.nombre.toPlainText()

    def verificar_producto_exist(self):
        #se verificara que los parametros que paso el usuario no existan ya en la bdd y si es asi solo se actualizaran
        #o se mostrara una advertencia al usuario del caso.
        global idLocal, data
        cursor = db.cursor()

        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT ProveedorId, Nombre, Direccion, Telefono, Empresa FROM proveedor WHERE ProveedorId = %s OR Nombre = %s"
        val = (idLocal,nombreloc)

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
    ui.agregar.clicked.connect(ui.llamar_a_las_demas)
    sys.exit(app.exec_())
