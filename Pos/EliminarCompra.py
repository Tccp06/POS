# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EliminarCompra.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import logoeliminarempleado


global id
global db,data



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(551, 555)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(380, 440, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(255, 101, 103);\n"
"\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 70, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(360, 80, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.agregar.setObjectName("agregar")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 121, 71))
        self.label_2.setStyleSheet("image: url(:/logo9/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 150, 501, 192))
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setObjectName("tableView")
        self.ID = QtWidgets.QTextEdit(self.centralwidget)
        self.ID.setGeometry(QtCore.QRect(130, 80, 191, 31))
        self.ID.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ID.setObjectName("ID")
        self.eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.eliminar.setGeometry(QtCore.QRect(380, 380, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.eliminar.setFont(font)
        self.eliminar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"")
        self.eliminar.setObjectName("eliminar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 551, 26))
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
        self.cancelar.setText(_translate("MainWindow", "Atrás"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">ID de compra</span></p></body></html>"))
        self.agregar.setText(_translate("MainWindow", "Buscar"))
        self.eliminar.setText(_translate("MainWindow", "Eliminar"))

        self.agregar.clicked.connect(self.llamar_a_las_demas)
        self.eliminar.clicked.connect(self.eliminar_cosas)
        #self.cancelar.clicked.connect(self.regresar_menu)

    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos2")

    def datos_tabla(self):
        global datos,data
        if(data==None):
            data="No existe"
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
        sql="DELETE compra, detallecompra FROM compra join detallecompra on c.CompraId = d.CompraId WHERE c.CompraId = %s"
        cursor.execute(sql,(id))
        db.commit()
        print(id)
        # procesa una unica linea usando el metodo fetchone().
        data = cursor.fetchone()
        #cursor.execute(sql, val)
        print("Row eliminado")
        data = cursor.fetchone()



    def eliminar_cosas(self):
        global id
        self.conectar_bdd()
        self.tomar_datos()
        self.eliminar_registro()
        db.close()



    def verificar_producto_exist(self):
        #se verificara que los parametros que paso el usuario no existan ya en la bdd y si es asi solo se actualizaran
        #o se mostrara una advertencia al usuario del caso.
        global db, data
        global id
        cursor = db.cursor()
        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT Nombre,Apellido,Sexo FROM empleado WHERE EmpleadoId = %s"
        val = (id)
        cursor.execute(sql, val)
        #myresult = cursor.fetchall()
        data = cursor.fetchone()
        if(data==None):
            data="No existe"

    def tomar_datos(self):
        global id
        id = self.ID.toPlainText()

    def llamar_a_las_demas(self):
        global data
        self.conectar_bdd()
        self.tomar_datos()
        self.verificar_producto_exist()
        self.datos_tabla()
        self.agregar_datos_tabla()

    def regresar_menu(self):
        self.Form = QtWidgets.QWidget()
        self.ui = InicioAdmin.Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
        MainWindow.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_EliminarEmpleado()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
