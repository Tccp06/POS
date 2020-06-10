# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Inicio.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(795, 596)
        Form.setStyleSheet("background-color: rgb(157, 155, 155);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 10, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Form)
        self.dateTimeEdit.setGeometry(QtCore.QRect(10, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.ventaProducto = QtWidgets.QPushButton(Form)
        self.ventaProducto.setGeometry(QtCore.QRect(60, 120, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.ventaProducto.setFont(font)
        self.ventaProducto.setStyleSheet("background-color: rgb(25, 240, 97);")
        self.ventaProducto.setObjectName("ventaProducto")
        self.agregarProducto = QtWidgets.QPushButton(Form)
        self.agregarProducto.setGeometry(QtCore.QRect(60, 200, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.agregarProducto.setFont(font)
        self.agregarProducto.setStyleSheet("background-color: rgb(54, 159, 224);")
        self.agregarProducto.setObjectName("agregarProducto")
        self.eliminarProducto = QtWidgets.QPushButton(Form)
        self.eliminarProducto.setGeometry(QtCore.QRect(60, 280, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.eliminarProducto.setFont(font)
        self.eliminarProducto.setStyleSheet("background-color: rgb(54, 159, 224);")
        self.eliminarProducto.setObjectName("eliminarProducto")
        self.buscarProductos = QtWidgets.QPushButton(Form)
        self.buscarProductos.setGeometry(QtCore.QRect(540, 120, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.buscarProductos.setFont(font)
        self.buscarProductos.setStyleSheet("background-color: rgb(54, 159, 224);")
        self.buscarProductos.setObjectName("buscarProductos")
        self.inventario = QtWidgets.QPushButton(Form)
        self.inventario.setGeometry(QtCore.QRect(540, 200, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.inventario.setFont(font)
        self.inventario.setStyleSheet("background-color: rgb(54, 159, 224);")
        self.inventario.setObjectName("inventario")
        self.cerrarCaja = QtWidgets.QPushButton(Form)
        self.cerrarCaja.setGeometry(QtCore.QRect(540, 290, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.cerrarCaja.setFont(font)
        self.cerrarCaja.setStyleSheet("background-color: rgb(247, 33, 33);")
        self.cerrarCaja.setObjectName("cerrarCaja")
        self.registrarEmpleado = QtWidgets.QPushButton(Form)
        self.registrarEmpleado.setGeometry(QtCore.QRect(280, 380, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.registrarEmpleado.setFont(font)
        self.registrarEmpleado.setStyleSheet("background-color: rgb(54, 159, 224);")
        self.registrarEmpleado.setObjectName("registrarEmpleado")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(280, 130, 201, 211))
        self.label_2.setStyleSheet("background-image: url(:/logo2/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Bienvenido </span></p></body></html>"))
        self.ventaProducto.setText(_translate("Form", "Venta de Producto"))
        self.agregarProducto.setText(_translate("Form", "Agregar Productos"))
        self.eliminarProducto.setText(_translate("Form", "Eliminar Productos"))
        self.buscarProductos.setText(_translate("Form", "Buscar Productos"))
        self.inventario.setText(_translate("Form", "Inventario"))
        self.cerrarCaja.setText(_translate("Form", "Cerrar Caja"))
        self.registrarEmpleado.setText(_translate("Form", "Registrar Empleado"))
import iniciologo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
