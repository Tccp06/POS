# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ListadoMenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import logomenulistado

class Ui_ListadoMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 336)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, -20, 121, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.proveedor = QtWidgets.QPushButton(self.centralwidget)
        self.proveedor.setGeometry(QtCore.QRect(420, 160, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.proveedor.setFont(font)
        self.proveedor.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.proveedor.setObjectName("proveedor")
        self.almacen_2 = QtWidgets.QPushButton(self.centralwidget)
        self.almacen_2.setGeometry(QtCore.QRect(50, 80, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.almacen_2.setFont(font)
        self.almacen_2.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.almacen_2.setObjectName("almacen_2")
        self.regresar = QtWidgets.QPushButton(self.centralwidget)
        self.regresar.setGeometry(QtCore.QRect(410, 240, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.regresar.setFont(font)
        self.regresar.setStyleSheet("background-color: rgb(247, 33, 33);")
        self.regresar.setObjectName("regresar")
        self.compras = QtWidgets.QPushButton(self.centralwidget)
        self.compras.setGeometry(QtCore.QRect(350, 80, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.compras.setFont(font)
        self.compras.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.compras.setObjectName("compras")
        self.producto = QtWidgets.QPushButton(self.centralwidget)
        self.producto.setGeometry(QtCore.QRect(270, 160, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.producto.setFont(font)
        self.producto.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.producto.setObjectName("producto")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-20, 220, 151, 91))
        self.label_2.setStyleSheet("image: url(:/asd/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.categoria = QtWidgets.QPushButton(self.centralwidget)
        self.categoria.setGeometry(QtCore.QRect(200, 80, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.categoria.setFont(font)
        self.categoria.setStyleSheet("background-color: rgb(255, 230, 109);\n"
"")
        self.categoria.setObjectName("categoria")
        self.empleado = QtWidgets.QPushButton(self.centralwidget)
        self.empleado.setGeometry(QtCore.QRect(120, 160, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.empleado.setFont(font)
        self.empleado.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.empleado.setObjectName("empleado")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 577, 26))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Listado</p></body></html>"))
        self.proveedor.setText(_translate("MainWindow", "Proveedor"))
        self.almacen_2.setText(_translate("MainWindow", "Almacen"))
        self.regresar.setText(_translate("MainWindow", "Regresar"))
        self.compras.setText(_translate("MainWindow", "Compras"))
        self.producto.setText(_translate("MainWindow", "Producto"))
        self.categoria.setText(_translate("MainWindow", "Categoria"))
        self.empleado.setText(_translate("MainWindow", "Empleado"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
