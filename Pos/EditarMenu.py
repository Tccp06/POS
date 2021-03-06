# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditarMenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import logoeditarmenu
import InicioAdmin
import ModificarAcceso
import ModificarAlmacen
import ModificarEmpleado
import ModificarProducto
import ModificarProveedor


class Ui_EditarMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(523, 351)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 240, 91, 81))
        self.label_2.setStyleSheet("\n"
"image: url(:/asd/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.regresar = QtWidgets.QPushButton(self.centralwidget)
        self.regresar.setGeometry(QtCore.QRect(350, 260, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.regresar.setFont(font)
        self.regresar.setStyleSheet("background-color: rgb(247, 33, 33);")
        self.regresar.setObjectName("regresar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, -10, 91, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.almacen = QtWidgets.QPushButton(self.centralwidget)
        self.almacen.setGeometry(QtCore.QRect(200, 80, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.almacen.setFont(font)
        self.almacen.setStyleSheet("background-color: rgb(255, 230, 109);\n"
"")
        self.almacen.setObjectName("almacen")
        self.acceso = QtWidgets.QPushButton(self.centralwidget)
        self.acceso.setGeometry(QtCore.QRect(50, 80, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.acceso.setFont(font)
        self.acceso.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.acceso.setObjectName("acceso")
        self.proveedor = QtWidgets.QPushButton(self.centralwidget)
        self.proveedor.setGeometry(QtCore.QRect(290, 160, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.proveedor.setFont(font)
        self.proveedor.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.proveedor.setObjectName("proveedor")
        self.producto = QtWidgets.QPushButton(self.centralwidget)
        self.producto.setGeometry(QtCore.QRect(130, 160, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.producto.setFont(font)
        self.producto.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.producto.setObjectName("producto")
        self.empleado = QtWidgets.QPushButton(self.centralwidget)
        self.empleado.setGeometry(QtCore.QRect(350, 80, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.empleado.setFont(font)
        self.empleado.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.empleado.setObjectName("empleado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 523, 26))
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
        self.regresar.setText(_translate("MainWindow", "Regresar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Editar</p></body></html>"))
        self.almacen.setText(_translate("MainWindow", "Almacen"))
        self.acceso.setText(_translate("MainWindow", "Acceso"))
        self.proveedor.setText(_translate("MainWindow", "Proveedor"))
        self.producto.setText(_translate("MainWindow", "Producto"))
        self.empleado.setText(_translate("MainWindow", "Empleado"))
        self.almacen.clicked.connect(self.editar_almacen)
        self.acceso.clicked.connect(self.editar_acceso)
        self.empleado.clicked.connect(self.editar_empleado)
        self.producto.clicked.connect(self.editar_producto)
        self.proveedor.clicked.connect(self.editar_proveedor)
        


    def editar_almacen(self):
        self.editarAlmacen = QtWidgets.QMainWindow()
        self.ui = ModificarAlmacen.Ui_ModificarAlmacen()
        self.ui.setupUi(self.editarAlmacen)
        self.editarAlmacen.show()

    def editar_acceso(self):
        self.editarAcceso = QtWidgets.QMainWindow()
        self.ui = ModificarAcceso.Ui_ModificarAcceso()
        self.ui.setupUi(self.editarAcceso)
        self.editarAcceso.show()

    def editar_empleado(self):
        self.editarEmpleado = QtWidgets.QMainWindow()
        self.ui = ModificarEmpleado.Ui_ModificarEmpleado()
        self.ui.setupUi(self.editarEmpleado)
        self.editarEmpleado.show()

    def editar_producto(self):
        self.editarProducto = QtWidgets.QMainWindow()
        self.ui = ModificarProducto.Ui_ModificarProducto()
        self.ui.setupUi(self.editarProducto)
        self.editarProducto.show()

    def editar_proveedor(self):
        self.editarProveedor = QtWidgets.QMainWindow()
        self.ui = ModificarProveedor.Ui_ModificarProveedor()
        self.ui.setupUi(self.editarProveedor)
        self.editarProveedor.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
