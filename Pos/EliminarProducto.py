# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EliminarProducto.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import logobuscarcompra
from PyQt5.QtWidgets import QTableWidgetItem
import pymysql
import logoproducto
import InicioAdmin

global db,data
global id

class Ui_EliminarProducto(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 554)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 70, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(370, 90, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.agregar.setObjectName("agregar")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(370, 450, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(255, 101, 103);\n"
"\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 120, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(640, 20, 121, 81))
        self.label_2.setStyleSheet("image: url(:/logo12/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.ID = QtWidgets.QTextEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(150, 80, 191, 31))
        self.ID.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ID.setObjectName("ID")
        self.nombre = QtWidgets.QTextEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(150, 130, 191, 31))
        self.nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombre.setObjectName("nombre")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 180, 521, 192))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
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
        self.eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.eliminar.setGeometry(QtCore.QRect(370, 390, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.eliminar.setFont(font)
        self.eliminar.setStyleSheet("background-color: rgb(213, 28, 28);")
        self.eliminar.setObjectName("eliminar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 26))
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
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">ID de producto</span></p></body></html>"))
        self.agregar.setText(_translate("MainWindow", "Buscar"))
        self.cancelar.setText(_translate("MainWindow", "Atrás"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nombre</span></p></body></html>"))
        self.eliminar.setText(_translate("MainWindow", "Eliminar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Descripcion"))
        self.agregar.clicked.connect(self.llamar_a_las_demas)
        self.eliminar.clicked.connect(self.eliminar_cosas)
        #ui.cancelar.clicked.connect(ui.regresar_menu)


    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos2")

    def datos_tabla(self):
        global datos,data
        self.datos = []
        self.datos.append((data))

    def agregar_datos_tabla(self):
        global datos, tableWidget
        fila = 0
        for registro in self.datos:
            columna = 0
            self.tableWidget.insertRow(fila)
            for elemento in registro:
                celda = QTableWidgetItem(elemento)
                self.tableWidget.setItem(fila,columna,celda)
                columna+=1
            fila +=1

    def eliminar_registro(self):
        global db, data, id

        cursor = db.cursor()
        sql="DELETE FROM producto WHERE ProductoId = %s"
        cursor.execute(sql, (id,))
        print(id)
        # procesa una unica linea usando el metodo fetchone().
        data = cursor.fetchone()
        #cursor.execute(sql, val)
        print("Row eliminado")
        db.commit()




    def eliminar_cosas(self):
        global id
        print ("Botoneliminar")
        self.conectar_bdd()
        self.tomar_datos()
        print(id)
        self.eliminar_registro()
        db.close()



    def verificar_producto_exist(self):
        #se verificara que los parametros que paso el usuario no existan ya en la bdd y si es asi solo se actualizaran
        #o se mostrara una advertencia al usuario del caso.
        global db, data
        global id

        cursor = db.cursor()
        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT Nombre,Descripcion FROM producto WHERE ProductoId = %s"
        val = (id)
        cursor.execute(sql, val)
        #myresult = cursor.fetchall()
        data = cursor.fetchone()


    def tomar_datos(self):
        global id
        id = self.ID.toPlainText()

    def llamar_a_las_demas(self):
        self.conectar_bdd()
        self.tomar_datos()
        self.verificar_producto_exist()
        self.datos_tabla()
        self.agregar_datos_tabla()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_EliminarProducto()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
