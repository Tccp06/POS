# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InicioEmpleado.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import logoinicio2
import Vender
import AgregarMenu
import EditarMenu
import ListadoMenu
import ListadoAlmacen
import EliminarMenu
import BuscarMenu
import Login



class Ui_MainWindowEmpleado(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 595)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);\n")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 400, 201, 211))
        self.label_2.setStyleSheet("image: url(:/logoxd/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 90, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.eliminar.setGeometry(QtCore.QRect(420, 320, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.eliminar.setFont(font)
        self.eliminar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.eliminar.setObjectName("eliminar")
        self.listado = QtWidgets.QPushButton(self.centralwidget)
        self.listado.setGeometry(QtCore.QRect(500, 230, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.listado.setFont(font)
        self.listado.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.listado.setObjectName("listado")
        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(170, 230, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.agregar.setObjectName("agregar")
        self.modificarProducto = QtWidgets.QPushButton(self.centralwidget)
        self.modificarProducto.setGeometry(QtCore.QRect(340, 230, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.modificarProducto.setFont(font)
        self.modificarProducto.setStyleSheet("background-color: rgb(255, 230, 109);\n"
"")
        self.modificarProducto.setObjectName("modificarProducto")
        self.inventario_2 = QtWidgets.QPushButton(self.centralwidget)
        self.inventario_2.setGeometry(QtCore.QRect(250, 320, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.inventario_2.setFont(font)
        self.inventario_2.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.inventario_2.setObjectName("inventario_2")
        self.ventaProducto = QtWidgets.QPushButton(self.centralwidget)
        self.ventaProducto.setGeometry(QtCore.QRect(320, 150, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.ventaProducto.setFont(font)
        self.ventaProducto.setStyleSheet("background-color: rgb(78, 205, 196);\n"
"")
        self.ventaProducto.setObjectName("ventaProducto")
        self.buscar = QtWidgets.QPushButton(self.centralwidget)
        self.buscar.setGeometry(QtCore.QRect(580, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.buscar.setFont(font)
        self.buscar.setStyleSheet("background-color: rgb(78, 205, 196);\n"
"")
        self.buscar.setObjectName("buscar")
        self.cerrarCaja = QtWidgets.QPushButton(self.centralwidget)
        self.cerrarCaja.setGeometry(QtCore.QRect(630, 500, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.cerrarCaja.setFont(font)
        self.cerrarCaja.setStyleSheet("background-color: rgb(247, 33, 33);")
        self.cerrarCaja.setObjectName("cerrarCaja")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 799, 26))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Bienvenido </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Cajero</p></body></html>"))
        self.eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.listado.setText(_translate("MainWindow", "Listado"))
        self.agregar.setText(_translate("MainWindow", "Agregar "))
        self.modificarProducto.setText(_translate("MainWindow", "Editar"))
        self.inventario_2.setText(_translate("MainWindow", "Inventario"))
        self.ventaProducto.setText(_translate("MainWindow", "Vender"))
        self.buscar.setText(_translate("MainWindow", "Buscar "))
        self.cerrarCaja.setText(_translate("MainWindow", "Menu"))
        
        self.agregar.clicked.connect(self.menuagregar)
        self.modificarProducto.clicked.connect(self.menueditar)
        self.listado.clicked.connect(self.menulistado)
        self.inventario_2.clicked.connect(self.menuinventario)
        self.eliminar.clicked.connect(self.menueliminar)
        self.buscar.clicked.connect(self.menubuscar)
        self.cerrarCaja.clicked.connect(self.login)
        self.ventaProducto.clicked.connect(self.vender)
    def menuagregar(self):
        self.agregarMenu = QtWidgets.QMainWindow()
        self.ui = AgregarMenu.Ui_AgregarMenu()
        self.ui.setupUi(self.agregarMenu)
        self.agregarMenu.show()
        #MainWindow.hide()

    def menueditar(self):
        self.editarMenu = QtWidgets.QMainWindow()
        self.ui = EditarMenu.Ui_EditarMenu()
        self.ui.setupUi(self.editarMenu)
        self.editarMenu.show()
        #MainWindow.hide()

    def menulistado(self):
        self.listadoMenu = QtWidgets.QMainWindow()
        self.ui = ListadoMenu.Ui_ListadoMenu()
        self.ui.setupUi(self.listadoMenu)
        self.listadoMenu.show()
        #MainWindow.hide()

    def menuinventario(self):
        self.inventarioMenu = QtWidgets.QMainWindow()
        self.ui = ListadoAlmacen.Ui_ListadoAlmacen()
        self.ui.setupUi(self.inventarioMenu)
        self.inventarioMenu.show()
        #MainWindow.hide()

    def menueliminar(self):
        self.eliminarMenu = QtWidgets.QMainWindow()
        self.ui = EliminarMenu.Ui_EliminarMenu()
        self.ui.setupUi(self.eliminarMenu)
        self.eliminarMenu.show()
        #MainWindow.hide()

    def menubuscar(self):
        self.buscarMenu = QtWidgets.QMainWindow()
        self.ui = BuscarMenu.Ui_BuscarMenu()
        self.ui.setupUi(self.buscarMenu)
        self.buscarMenu.show()
        #MainWindow.hide()

    def login(self):
        self.log = QtWidgets.QMainWindow()
        self.ui = Login.Ui_Login()
        self.ui.setupUi(self.log)
        self.log.show()
        #MainWindow.hide()
        
    def vender(self):
        self.MainWindow3 = QtWidgets.QMainWindow()
        self.ui =Vender.Ui_VenderWindow()
        self.ui.setupUi(self.MainWindow3)
        self.MainWindow3.show()
        #MainWindow.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowEmpleado()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
