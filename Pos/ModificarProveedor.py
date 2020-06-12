# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModificarProveedor.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(157, 155, 155);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(150, 340, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(620, 490, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.id = QtWidgets.QTextEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(270, 130, 191, 41))
        self.id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id.setObjectName("id")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 180, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(470, 490, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(54, 159, 224);")
        self.agregar.setObjectName("agregar")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 280, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(150, 230, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.categoria = QtWidgets.QListView(self.centralwidget)
        self.categoria.setGeometry(QtCore.QRect(270, 280, 191, 41))
        self.categoria.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.categoria.setObjectName("categoria")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 10, 181, 131))
        self.label_2.setStyleSheet("image: url(:/logompr/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(120, 130, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 20, 301, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.proveedor = QtWidgets.QTextEdit(self.centralwidget)
        self.proveedor.setGeometry(QtCore.QRect(270, 340, 191, 41))
        self.proveedor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.proveedor.setObjectName("proveedor")
        self.descripcion = QtWidgets.QTextEdit(self.centralwidget)
        self.descripcion.setGeometry(QtCore.QRect(270, 230, 191, 41))
        self.descripcion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.descripcion.setObjectName("descripcion")
        self.nombre = QtWidgets.QTextEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(270, 180, 191, 41))
        self.nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombre.setObjectName("nombre")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Empresa</span></p></body></html>"))
        self.cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Nombre</span></p></body></html>"))
        self.agregar.setText(_translate("MainWindow", "Agregar"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Teléfono</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Direccion</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">ProveedorID</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Modificar Proveedor</p></body></html>"))
import logomodificarproducto_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
