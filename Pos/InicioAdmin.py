# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InicioAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import iniciologo
import Login
import AgregarMenu
import EditarMenu
import ListadoMenu
import ListadoAlmacen
import EliminarMenu
import BuscarMenu


class Ui_InicioAdmin(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 606)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);\n")
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(40, 20, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(MainWindow)
        self.dateTimeEdit.setGeometry(QtCore.QRect(530, 30, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(30, 430, 191, 131))
        self.label_2.setStyleSheet("background-image: url(:/logo2/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(110, 90, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cerrarCaja = QtWidgets.QPushButton(MainWindow)
        self.cerrarCaja.setGeometry(QtCore.QRect(620, 520, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.cerrarCaja.setFont(font)
        self.cerrarCaja.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"")
        self.cerrarCaja.setObjectName("cerrarCaja")
        self.buscar = QtWidgets.QPushButton(MainWindow)
        self.buscar.setGeometry(QtCore.QRect(570, 80, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.buscar.setFont(font)
        self.buscar.setStyleSheet("background-color: rgb(78, 205, 196);\n"
"")
        self.buscar.setObjectName("buscar")
        self.listado = QtWidgets.QPushButton(MainWindow)
        self.listado.setGeometry(QtCore.QRect(510, 200, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.listado.setFont(font)
        self.listado.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.listado.setObjectName("listado")
        self.eliminar = QtWidgets.QPushButton(MainWindow)
        self.eliminar.setGeometry(QtCore.QRect(430, 290, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.eliminar.setFont(font)
        self.eliminar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.eliminar.setObjectName("eliminar")
        self.agregar = QtWidgets.QPushButton(MainWindow)
        self.agregar.setGeometry(QtCore.QRect(180, 200, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.agregar.setObjectName("agregar")
        self.modificarProducto = QtWidgets.QPushButton(MainWindow)
        self.modificarProducto.setGeometry(QtCore.QRect(350, 200, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.modificarProducto.setFont(font)
        self.modificarProducto.setStyleSheet("background-color: rgb(255, 230, 109);\n"
"")
        self.modificarProducto.setObjectName("modificarProducto")
        self.inventario = QtWidgets.QPushButton(MainWindow)
        self.inventario.setGeometry(QtCore.QRect(260, 290, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.inventario.setFont(font)
        self.inventario.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.inventario.setObjectName("inventario")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Bienvenido </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Admin</p></body></html>"))
        self.cerrarCaja.setText(_translate("MainWindow", "Cerrar Caja"))
        self.buscar.setText(_translate("MainWindow", "Buscar "))
        self.listado.setText(_translate("MainWindow", "Listado"))
        self.eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.agregar.setText(_translate("MainWindow", "Agregar "))
        self.modificarProducto.setText(_translate("MainWindow", "Editar"))
        self.inventario.setText(_translate("MainWindow", "Inventario"))
        self.agregar.clicked.connect(self.menuagregar)
        self.modificarProducto.clicked.connect(self.menueditar)
        self.listado.clicked.connect(self.menulistado)
        self.inventario.clicked.connect(self.menuinventario)
        self.eliminar.clicked.connect(self.menueliminar)
        self.buscar.clicked.connect(self.menubuscar)
        self.cerrarCaja.clicked.connect(self.login)

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
        MainWindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_InicioAdmin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
