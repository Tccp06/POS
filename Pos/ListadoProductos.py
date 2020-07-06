# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListadoProductos.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import pymysql
import ListadoMenu
import logolistadoproductos

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(745, 600)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 500, 111, 61))
        self.label_2.setStyleSheet("image: url(:/logo15/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(550, 510, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 0, 441, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(30, 90, 661, 391))
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 745, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 90, 661, 391))
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
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cancelar.setText(_translate("MainWindow", "Ok"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Acerca de los productos</p></body></html>"))
        self.cancelar.setText(_translate("MainWindow", "Ok"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Productos en almacen</p></body></html>"))
        
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

        
        self.llamar_a_las_demas()
        self.cancelar.clicked.connect(ui.other)
    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos")
    def verificar_producto_exist(self):
        #se verificara que los parametros que paso el usuario no existan ya en la bdd y si es asi solo se actualizaran
        #o se mostrara una advertencia al usuario del caso.
        global idLocal, data
        cursor = db.cursor()

        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT * FROM producto"
        #val = (idLocal)
        #SELECT Fecha FROM compra WHERE CompraId = %s
        cursor.execute(sql)
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
        ui.verificar_producto_exist()
        ui.datos_tabla()
        ui.agregar_datos_tabla()

#Abrir otra ventana
    def other(self):
        self.MainWindow2 = QtWidgets.QMainWindow()
        self.ui = ListadoMenu.Ui_ListadoMenu()
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
