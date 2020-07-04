# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InicioAdmin.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import iniciologo
import AgregarMenu
import EditarMenu
import ListadoMenu
import ListadoAlmacen
import EliminarMenu


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(795, 606)
        Form.setStyleSheet("background-color: rgb(247, 255, 247);\n"
"\n"
"\n"
"")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 20, 221, 81))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(530, 30, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 430, 191, 131))
        self.label_2.setStyleSheet("background-image: url(:/logo2/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(110, 90, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.cerrarCaja = QtWidgets.QPushButton(Form)
        self.cerrarCaja.setGeometry(QtCore.QRect(620, 520, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.cerrarCaja.setFont(font)
        self.cerrarCaja.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"")
        self.cerrarCaja.setObjectName("cerrarCaja")
        self.buscar = QtWidgets.QPushButton(Form)
        self.buscar.setGeometry(QtCore.QRect(570, 80, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.buscar.setFont(font)
        self.buscar.setStyleSheet("background-color: rgb(78, 205, 196);\n"
"")
        self.buscar.setObjectName("buscar")
        self.listado = QtWidgets.QPushButton(Form)
        self.listado.setGeometry(QtCore.QRect(510, 200, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.listado.setFont(font)
        self.listado.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.listado.setObjectName("listado")
        self.eliminar = QtWidgets.QPushButton(Form)
        self.eliminar.setGeometry(QtCore.QRect(430, 290, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.eliminar.setFont(font)
        self.eliminar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.eliminar.setObjectName("eliminar")
        self.agregar = QtWidgets.QPushButton(Form)
        self.agregar.setGeometry(QtCore.QRect(180, 200, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.agregar.setObjectName("agregar")
        self.modificarProducto = QtWidgets.QPushButton(Form)
        self.modificarProducto.setGeometry(QtCore.QRect(350, 200, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.modificarProducto.setFont(font)
        self.modificarProducto.setStyleSheet("background-color: rgb(255, 230, 109);\n"
"")
        self.modificarProducto.setObjectName("modificarProducto")
        self.inventario = QtWidgets.QPushButton(Form)
        self.inventario.setGeometry(QtCore.QRect(260, 290, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.inventario.setFont(font)
        self.inventario.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.inventario.setObjectName("inventario")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Bienvenido </span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Admin</p></body></html>"))
        self.cerrarCaja.setText(_translate("Form", "Cerrar Caja"))
        self.buscar.setText(_translate("Form", "Buscar "))
        self.listado.setText(_translate("Form", "Listado"))
        self.eliminar.setText(_translate("Form", "Eliminar"))
        self.agregar.setText(_translate("Form", "Agregar "))
        self.modificarProducto.setText(_translate("Form", "Editar"))
        self.inventario.setText(_translate("Form", "Inventario"))

    def menuagregar(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = AgregarMenu.Ui_AgregarMenu()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        Form.hide()

    def menueditar(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = EditarMenu.Ui_EditarMenu()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        Form.hide()

    def menulistado(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = ListadoMenu.Ui_ListadoMenu()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        Form.hide()

    def menuinventario(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = ListadoAlmacen.Ui_ListadoAlmacen()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        Form.hide()

    def menueliminar(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = EliminarMenu.Ui_EliminarMenu()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        Form.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    ui.agregar.clicked.connect(ui.menuagregar)
    ui.modificarProducto.clicked.connect(ui.menueditar)
    ui.listado.clicked.connect(ui.menulistado)
    ui.inventario.clicked.connect(ui.menuinventario)
    ui.eliminar.clicked.connect(ui.menueliminar)
    sys.exit(app.exec_())
