# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgregarMenu.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(528, 307)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 0, 121, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 210, 91, 61))
        self.label_2.setStyleSheet("image: url(:/logoxd/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);\n"
"image: url(:/asd/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.producto_2 = QtWidgets.QPushButton(self.centralwidget)
        self.producto_2.setGeometry(QtCore.QRect(210, 100, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.producto_2.setFont(font)
        self.producto_2.setStyleSheet("background-color: rgb(255, 230, 109);\n"
"")
        self.producto_2.setObjectName("producto_2")
        self.producto = QtWidgets.QPushButton(self.centralwidget)
        self.producto.setGeometry(QtCore.QRect(60, 100, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.producto.setFont(font)
        self.producto.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.producto.setObjectName("producto")
        self.empleado = QtWidgets.QPushButton(self.centralwidget)
        self.empleado.setGeometry(QtCore.QRect(360, 100, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.empleado.setFont(font)
        self.empleado.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.empleado.setObjectName("empleado")
        self.regresar = QtWidgets.QPushButton(self.centralwidget)
        self.regresar.setGeometry(QtCore.QRect(360, 210, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(14)
        self.regresar.setFont(font)
        self.regresar.setStyleSheet("background-color: rgb(247, 33, 33);")
        self.regresar.setObjectName("regresar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 528, 26))
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
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Agregar</p></body></html>"))
        self.producto_2.setText(_translate("MainWindow", "Proveedor"))
        self.producto.setText(_translate("MainWindow", "Producto"))
        self.empleado.setText(_translate("MainWindow", "Empleado"))
        self.regresar.setText(_translate("MainWindow", "Regresar"))
import logomenuagregar_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
