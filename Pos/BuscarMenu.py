# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BuscarMenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 357)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.categoria = QtWidgets.QPushButton(self.centralwidget)
        self.categoria.setGeometry(QtCore.QRect(230, 70, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.categoria.setFont(font)
        self.categoria.setStyleSheet("background-color: rgb(255, 230, 109);\n"
"")
        self.categoria.setObjectName("categoria")
        self.empleado = QtWidgets.QPushButton(self.centralwidget)
        self.empleado.setGeometry(QtCore.QRect(150, 150, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)

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


        self.empleado.setFont(font)
        self.empleado.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.empleado.setObjectName("empleado")
        self.regresar = QtWidgets.QPushButton(self.centralwidget)
        self.regresar.setGeometry(QtCore.QRect(440, 230, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.regresar.setFont(font)
        self.regresar.setStyleSheet("background-color: rgb(247, 33, 33);")
        self.regresar.setObjectName("regresar")
        self.producto = QtWidgets.QPushButton(self.centralwidget)
        self.producto.setGeometry(QtCore.QRect(300, 150, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.producto.setFont(font)
        self.producto.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.producto.setObjectName("producto")
        self.almacen_2 = QtWidgets.QPushButton(self.centralwidget)
        self.almacen_2.setGeometry(QtCore.QRect(80, 70, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.almacen_2.setFont(font)
        self.almacen_2.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.almacen_2.setObjectName("almacen_2")
        self.proveedor = QtWidgets.QPushButton(self.centralwidget)
        self.proveedor.setGeometry(QtCore.QRect(450, 150, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.proveedor.setFont(font)
        self.proveedor.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.proveedor.setObjectName("proveedor")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, -30, 121, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 230, 151, 91))
        self.label_2.setStyleSheet("image: url(:/asd/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);\n"
"image: url(:/asd/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.compras = QtWidgets.QPushButton(self.centralwidget)
        self.compras.setGeometry(QtCore.QRect(380, 70, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.compras.setFont(font)
        self.compras.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.compras.setObjectName("compras")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 601, 26))
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
        self.categoria.setText(_translate("MainWindow", "Categoria"))
        self.empleado.setText(_translate("MainWindow", "Empleado"))
        self.regresar.setText(_translate("MainWindow", "Regresar"))
        self.producto.setText(_translate("MainWindow", "Producto"))
        self.almacen_2.setText(_translate("MainWindow", "Almacen"))
        self.proveedor.setText(_translate("MainWindow", "Proveedor"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Buscar</p></body></html>"))
        self.compras.setText(_translate("MainWindow", "Compras"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "CompraId"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Fecha"))
        
#import logobuscarmenu_rc
    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos")

    def tomar_datos(self):
        global idLocal

        idLocal = ui.ID.toPlainText()

    def verificar_producto_exist(self):
        #se verificara que los parametros que paso el usuario no existan ya en la bdd y si es asi solo se actualizaran
        #o se mostrara una advertencia al usuario del caso.
        global idLocal, data
        cursor = db.cursor()

        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT CompraId, ProductoId, CantidadProducto, NumeroDeArticulos, Total FROM detallecompra WHERE CompraId = %s"
        val = (idLocal)

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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
