 # -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BuscarMenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import logobuscarmenu
# import BuscarCompra
# import BuscarProducto
# import BuscarEmpleado
# import BuscarProveedor

class Ui_BuscarMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(601, 357)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.empleado = QtWidgets.QPushButton(self.centralwidget)
        self.empleado.setGeometry(QtCore.QRect(170, 150, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
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
        self.producto.setGeometry(QtCore.QRect(340, 150, 121, 51))
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
        self.proveedor.setGeometry(QtCore.QRect(420, 70, 121, 51))
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
        self.compras.setGeometry(QtCore.QRect(260, 70, 111, 51))
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
        self.empleado.setText(_translate("MainWindow", "Empleado"))
        self.regresar.setText(_translate("MainWindow", "Regresar"))
        self.producto.setText(_translate("MainWindow", "Producto"))
        self.almacen_2.setText(_translate("MainWindow", "Almacen"))
        self.proveedor.setText(_translate("MainWindow", "Proveedor"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Buscar</p></body></html>"))
        self.compras.setText(_translate("MainWindow", "Compras"))
        # self.empleado.clicked.connect(self.empleado_buscar)
        # self.almacen_2.clicked.connect(self.almacen_buscar)
        # self.proveedor.clicked.connect(self.proveedor_buscar)
        # self.producto.clicked.connect(self.producto_buscar)

    # def empleado_buscar(self):
    #     self.buscarEmpleado = QtWidgets.QMainWindow()
    #     self.ui = BuscarEmpleado.Ui_BuscarEmpleado()
    #     self.ui.setupUi(self.buscarEmpleado)
    #     self.buscarEmpleado.show()
    #
    # def almacen_buscar(self):
    #     self.buscarAlmacen = QtWidgets.QMainWindow()
    #     self.ui = BuscarAlmacen.Ui_BuscarAlmacen()
    #     self.ui.setupUi(self.buscarAlmacen)
    #     self.buscarAlmacen.show()
    #
    # def proveedor_buscar(self):
    #     self.buscarProveedor = QtWidgets.QMainWindow()
    #     self.ui = BuscarProveedor.Ui_BuscarProveedor()
    #     self.ui.setupUi(self.buscarProveedor)
    #     self.buscarProveedor.show()
    #
    # def producto_buscar(self):
    #     self.buscarProducto = QtWidgets.QMainWindow()
    #     self.ui = BuscarProducto .Ui_BuscarProducto ()
    #     self.ui.setupUi(self.buscarProducto )
    #     self.buscarProducto .show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_BuscarMenu()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
