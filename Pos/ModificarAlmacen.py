# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModificarAlmacen.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import logomodificaralmacen

global idloc,cantidadloc
global db,data
global alex


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(157, 155, 155);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.id = QtWidgets.QTextEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(260, 170, 191, 41))
        self.id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id.setObjectName("id")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(570, 500, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 20, 181, 131))
        self.label_2.setStyleSheet("image: url(:/logoma/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);\n"
"image: url(:/lma/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(110, 170, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(420, 500, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(54, 159, 224);")
        self.agregar.setObjectName("agregar")
        self.cantidad = QtWidgets.QTextEdit(self.centralwidget)
        self.cantidad.setGeometry(QtCore.QRect(260, 220, 191, 41))
        self.cantidad.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cantidad.setObjectName("cantidad")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 60, 301, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 220, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
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
        self.cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">ProductoID</span></p></body></html>"))
        self.agregar.setText(_translate("MainWindow", "Agregar"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Modificar Almacen</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Cantidad</span></p></body></html>"))

    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos2")

    def verificar_almacen_existente(self):
        global idloc,cantidadloc
        global db, data
        global alex

        cursor = db.cursor()

        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT ProductoId FROM almacen  WHERE ProductoId=%s"
        val = (idloc)
        # procesa una unica linea usando el metodo fetchone().
        cursor.execute(sql, val)

        data = cursor.fetchone()

        if(data==None):
            alex = 0
        else:
            alex = 1
            db.commit()
            print("Existente ID")

    def insertar_datos(self):
        global idloc,cantidadloc
        global db, data,usex
        if(alex!=1):
            cursor = db.cursor()
            sql="INSERT INTO almacen (ProductoId,CantidadProducto) VALUES (%s,%s)"
            val = (idloc,cantidadloc)
            cursor.execute(sql,val)
            data = cursor.fetchone()
            db.commit()
            print(cursor.rowcount, "record inserted.")
        else:
            cursor = db.cursor()
            sql="UPDATE almacen SET ProductoId=%s, CantidadProducto=%s WHERE ProductoId=%s"
            val = (idloc,cantidadloc,idloc)
            cursor.execute(sql,val)
            db.commit()
            data = cursor.fetchone()

            print("Actualizado")


    def tomar_datos(self):
        global idloc,cantidadloc
        idloc = ui.id.toPlainText()
        cantidadloc = ui.cantidad.toPlainText()


    def llamar_a_las_demas(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        ui.conectar_bdd()
        ui.tomar_datos()
        ui.verificar_almacen_existente()
        ui.insertar_datos()
        db.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.agregar.clicked.connect(ui.llamar_a_las_demas)
    sys.exit(app.exec_())
