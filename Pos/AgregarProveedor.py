# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgregarProveedor.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import logoproveedor
import InicioAdmin

global nombreloc, direccionloc, telefonoloc, empresaloc
global db,data
global provex,id


class Ui_AgregarProveedor(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 506)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nombre = QtWidgets.QTextEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(180, 70, 191, 31))
        self.nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombre.setObjectName("nombre")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, -20, 81, 91))
        self.label_2.setStyleSheet("image: url(:/logo5/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.telefono = QtWidgets.QTextEdit(self.centralwidget)
        self.telefono.setGeometry(QtCore.QRect(180, 170, 191, 31))
        self.telefono.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.telefono.setObjectName("telefono")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 160, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.empresa = QtWidgets.QTextEdit(self.centralwidget)
        self.empresa.setGeometry(QtCore.QRect(180, 220, 191, 31))
        self.empresa.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.empresa.setObjectName("sexo")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 210, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(140, 300, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.agregar.setObjectName("agregar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 110, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(140, 370, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.direccion = QtWidgets.QTextEdit(self.centralwidget)
        self.direccion.setGeometry(QtCore.QRect(180, 120, 191, 31))
        self.direccion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.direccion.setObjectName("direccion")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 26))
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nombre del proveedor</span></p><p><br/></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Telefono</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Empresa</span></p></body></html>"))
        self.agregar.setText(_translate("MainWindow", "Agregar"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Direccion</span></p></body></html>"))
        self.cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.agregar.clicked.connect(self.llamar_a_las_demas)
        self.cancelar.clicked.connect(self.regresar_menu)


    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos2")

    def verificar_proveedor_exist(self):
        #se verificara que los parametros que paso el usuario no existan ya en la bdd y si es asi solo se actualizaran
        #o se mostrara una advertencia al usuario del caso.
        global nombreloc, direccionloc, telefonoloc, empresaloc
        global db, data
        global provex,id

        cursor = db.cursor()
        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT ProveedorId FROM proveedor WHERE Nombre = %s AND Direccion = %s AND  Telefono =%s AND Empresa = %s"
        val = (nombreloc, direccionloc, telefonoloc, empresaloc)
        cursor.execute(sql, val)
        #myresult = cursor.fetchall()
        data = cursor.fetchone()
        if(data==None):
            provex = 0
        else:
            provex = 1
            #sql ="SELECT EmpleadoId from empleado where "
            db.commit()
            id=data
            print("Existente ID")

    def insertar_dato(self):

        global nombreloc, direccionloc, telefonoloc, empresaloc
        global db, data
        global provex,id

        if(provex!=1): #si no existe se creara uno nuevo
            cursor = db.cursor()
            sql="INSERT INTO proveedor (Nombre, Direccion, Telefono, Empresa) VALUES (%s,%s,%s,%s)"
            val = (nombreloc, direccionloc, telefonoloc, empresaloc)
            cursor.execute(sql,val)
            data = cursor.fetchone()
            db.commit()
            print(cursor.rowcount, "record inserted.")
        else:
            cursor = db.cursor()
            sql="UPDATE proveedor SET Nombre = %s AND Direccion = %s AND  Telefono =%s AND Empresa = %s"
            val = (nombreloc, direccionloc, telefonoloc, empresaloc)
            cursor.execute(sql,val)
            db.commit()
            data = cursor.fetchone()

            print("Actualizado")

    def tomar_datos(self):
        global nombreloc, direccionloc, telefonoloc, empresaloc

        nombreloc = ui.nombre.toPlainText()
        direccionloc = ui.direccion.toPlainText()
        telefonoloc = ui.telefono.toPlainText()
        empresaloc = ui.empresa.toPlainText()



    def llamar_a_las_demas(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        ui.conectar_bdd()
        ui.tomar_datos()
        ui.verificar_proveedor_exist()
        ui.insertar_dato()
        ui.regresar_menu()
        db.close()

    def regresar_menu(self):
        self.Adminmenu = QtWidgets.QMainWindow()
        self.ui = InicioAdmin.Ui_InicioAdmin()
        self.ui.setupUi(self.Adminmenu)
        self.Adminmenu.show()
        MainWindow.hide()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AgregarProveedor()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
