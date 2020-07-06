# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Vender.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import pymysql
import InicioEmpleado

class Ui_VenderWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 527)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.id_producto = QtWidgets.QTextEdit(self.centralwidget)
        self.id_producto.setGeometry(QtCore.QRect(120, 60, 141, 31))
        self.id_producto.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Bahnschrift Condensed\";")
        self.id_producto.setObjectName("id_producto")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 81, 51))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.nombre_producto = QtWidgets.QTextEdit(self.centralwidget)
        self.nombre_producto.setGeometry(QtCore.QRect(120, 100, 141, 31))
        self.nombre_producto.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Bahnschrift Condensed\";")
        self.nombre_producto.setObjectName("nombre_producto")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 90, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(300, 20, 451, 211))
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setObjectName("tableView")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(300, 20, 451, 211))
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 8pt \"Bahnschrift Condensed\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()

        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(100, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.agregar.setObjectName("agregar")
        self.cantidad = QtWidgets.QTextEdit(self.centralwidget)
        self.cantidad.setGeometry(QtCore.QRect(120, 140, 141, 31))
        self.cantidad.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Bahnschrift Condensed\";")
        self.cantidad.setObjectName("cantidad")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 130, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(300, 240, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.total = QtWidgets.QTextEdit(self.centralwidget)
        self.total.setEnabled(False)
        self.total.setGeometry(QtCore.QRect(380, 250, 171, 31))
        self.total.setStyleSheet("background-color: rgb(255, 255, 255);\n"

"font: 9pt \"Bahnschrift Condensed\";")
        self.total.setObjectName("total")
        self.pagar = QtWidgets.QPushButton(self.centralwidget)
        self.pagar.setGeometry(QtCore.QRect(120, 400, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.pagar.setFont(font)
        self.pagar.setStyleSheet("background-color: rgb(69, 153, 255);")
        self.pagar.setObjectName("pagar")
        self.recibido = QtWidgets.QTextEdit(self.centralwidget)
        self.recibido.setGeometry(QtCore.QRect(150, 300, 121, 31))
        self.recibido.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Bahnschrift Condensed\";")
        self.recibido.setObjectName("recibido")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 290, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 340, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.cambio = QtWidgets.QTextEdit(self.centralwidget)
        self.cambio.setEnabled(False)
        self.cambio.setGeometry(QtCore.QRect(150, 350, 121, 31))
        self.cambio.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Bahnschrift Condensed\";")
        self.cambio.setObjectName("cambio")
        self.eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.eliminar.setGeometry(QtCore.QRect(190, 190, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.eliminar.setFont(font)
        self.eliminar.setStyleSheet("background-color: rgb(247, 33, 33);")
        self.eliminar.setObjectName("eliminar")
        self.btn_punto = QtWidgets.QPushButton(self.centralwidget)
        self.btn_punto.setGeometry(QtCore.QRect(320, 420, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.btn_punto.setFont(font)
        self.btn_punto.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.btn_punto.setObjectName("btn_punto")
        self.btn_0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_0.setGeometry(QtCore.QRect(370, 420, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("background-color: rgb(247, 255, 247);\n"
"")
        self.btn_0.setObjectName("btn_0")
        self.btn_9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_9.setGeometry(QtCore.QRect(320, 380, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.btn_9.setFont(font)
        self.btn_9.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.btn_9.setObjectName("btn_9")
        self.btn_10 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_10.setGeometry(QtCore.QRect(370, 380, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.btn_10.setFont(font)
        self.btn_10.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.btn_10.setObjectName("btn_10")
        self.btn_11 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_11.setGeometry(QtCore.QRect(420, 380, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.btn_11.setFont(font)
        self.btn_11.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.btn_11.setObjectName("btn_11")
        self.btn_6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_6.setGeometry(QtCore.QRect(320, 340, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.btn_6.setFont(font)
        self.btn_6.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.btn_6.setObjectName("btn_6")
        self.btn_7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_7.setGeometry(QtCore.QRect(370, 340, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.btn_7.setFont(font)
        self.btn_7.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.btn_7.setObjectName("btn_7")
        self.btn_8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_8.setGeometry(QtCore.QRect(420, 340, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.btn_8.setFont(font)
        self.btn_8.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.btn_8.setObjectName("btn_8")
        self.btn_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_3.setGeometry(QtCore.QRect(320, 300, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.btn_3.setFont(font)
        self.btn_3.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_4.setGeometry(QtCore.QRect(370, 300, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.btn_4.setFont(font)
        self.btn_4.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.btn_4.setObjectName("btn_4")
        self.btn_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_5.setGeometry(QtCore.QRect(420, 300, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.btn_5.setFont(font)
        self.btn_5.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.btn_5.setObjectName("btn_5")
        self.btn_borrar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_borrar.setGeometry(QtCore.QRect(470, 300, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.btn_borrar.setFont(font)
        self.btn_borrar.setStyleSheet("background-color: rgb(247, 33, 33);")
        self.btn_borrar.setObjectName("btn_borrar")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(590, 390, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.cancelar.setFont(font)
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);")
        self.cancelar.setObjectName("cancelar")
        self.cancelar_2 = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar_2.setGeometry(QtCore.QRect(590, 330, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.cancelar_2.setFont(font)
        self.cancelar_2.setStyleSheet("background-color: rgb(78, 205, 196);")
        self.cancelar_2.setObjectName("cancelar_2")
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
        global aux, r
        r = 0
        aux = 0
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">ID producto</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nombre</span></p></body></html>"))
        self.agregar.setText(_translate("MainWindow", "Agregar"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Cantidad</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt;\">Total $</span></p></body></html>"))
        self.pagar.setText(_translate("MainWindow", "Pagar"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Recibido $</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Cambio $</span></p></body></html>"))
        self.eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.btn_punto.setText(_translate("MainWindow", "."))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_9.setText(_translate("MainWindow", "7"))
        self.btn_10.setText(_translate("MainWindow", "8"))
        self.btn_11.setText(_translate("MainWindow", "9"))
        self.btn_6.setText(_translate("MainWindow", "4"))
        self.btn_7.setText(_translate("MainWindow", "5"))
        self.btn_8.setText(_translate("MainWindow", "6"))
        self.btn_3.setText(_translate("MainWindow", "1"))
        self.btn_4.setText(_translate("MainWindow", "2"))
        self.btn_5.setText(_translate("MainWindow", "3"))
        self.btn_borrar.setText(_translate("MainWindow", "x"))
        self.cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.cancelar_2.setText(_translate("MainWindow", "Nueva venta"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Cantidad"))

        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Producto"))

        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PrecioUnitario"))

        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "PrecioTotal"))

        self.cancelar.clicked.connect(self.inicioEmpleado)
        self.agregar.clicked.connect(self.llamar_a_las_demas)
        self.eliminar.clicked.connect(self.eliminarProducto)
        self.cancelar_2.clicked.connect(self.nuevaVenta)

        #Numeros
        #self.btn_punto.clicked.connect(self.recibido.insertPlainText('.'))
    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos")
    
    def tomar_datos(self):
        global idLocal, nombreloc, cantidad

        idLocal = ui.id_producto.toPlainText()
        nombreloc = ui.nombre_producto.toPlainText()
        cantidad = ui.cantidad.toPlainText()
    def verificar_producto_exist(self):
        #se verificara que los parametros que paso el usuario no existan ya en la bdd y si es asi solo se actualizaran
        #o se mostrara una advertencia al usuario del caso.
        global idLocal, nombreloc, data
        cursor = db.cursor()

        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT Nombre, PrecioUnitarioVenta FROM producto WHERE ProductoId = %s OR Nombre = %s"
        val = (idLocal, nombreloc)

        cursor.execute(sql, val)
        data = cursor.fetchone()

        if(data==None):
            prodex = 0
            print("No existe producto ya")
            print(data)
        else:
            prodex = 1
            db.commit()
            idLocal=data
        
    def datos_tabla(self):
        global datos, data
        self.datos = []
        self.datos.append((data))

    def agregar_datos_tabla(self):
        global datos, tableWidget
        global fila, cantidad 
        fila = 0
        total = 0
        global aux 
        global r
        for registro in self.datos:
            columna = 1
            ui.tableWidget.insertRow(fila)
            for elemento in registro: 
                #insertar cantidad de productos    
                cant = QTableWidgetItem(cantidad)
                ui.tableWidget.setItem(fila,0,cant)
                if columna == 2:
                        #insertar precio total del producto
                        elemento = float(elemento)
                        cantidad = float(cantidad)
                        total = elemento * cantidad
                        aux += total
                        strTotal = str(total)
                        t = QTableWidgetItem(strTotal)
                        ui.tableWidget.setItem(fila,3,t) 
                #insertar desde la bdd
                elemento = str(elemento)
                celda = QTableWidgetItem(elemento)
                ui.tableWidget.setItem(fila,columna,celda)
                columna+=1  
                
            fila +=1
        ui.total.clear()    
        ui.total.insertPlainText(str(aux))  
        if r != True:
                ui.recibido.insertPlainText(str(0))    
                r = ui.recibido.toPlainText()
                r = float(r)
                ui.cambio.insertPlainText(str(recibido-aux))     
            
    def eliminarProducto(self):
        global datos, tableWidget
#         fila = ui.tableWidget.currentRow
#         ui.tableWidget.removeRow(fila)  
        filaActual = ui.tableWidget.currentRow()
        print(filaActual)
        ui.tableWidget.removeRow(filaActual)
    
    def nuevaVenta(self):
        global tableWidget
        ui.tableWidget.clearContents()
        ui.tableWidget.setRowCount(0)
               

    def llamar_a_las_demas(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        ui.conectar_bdd()
        ui.tomar_datos()
        ui.verificar_producto_exist()
        ui.datos_tabla()
        ui.agregar_datos_tabla()

    def validarAgregarProducto(self):
            pass
   
    #Boton cancelar
    def inicioEmpleado(self):
        self.MainWindow2 = QtWidgets.QMainWindow()
        self.ui = InicioEmpleado.Ui_MainWindowEmpleado()
        self.ui.setupUi(self.MainWindow2)
        self.MainWindow2.show()
        #MainWindow.hide()
   

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_VenderWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
