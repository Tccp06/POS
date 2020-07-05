# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AgregarProducto.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import logoproducto
import InicioAdmin

global nombreloc, descripcionloc, proveedorloc, preciounven, preciouncom
global db,data
global prodex,id

class Ui_AgregarProducto(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(444, 535)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.nombre = QtWidgets.QTextEdit(MainWindow)
        self.nombre.setGeometry(QtCore.QRect(190, 110, 191, 31))
        self.nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombre.setObjectName("nombre")
        self.descripcion = QtWidgets.QTextEdit(MainWindow)
        self.descripcion.setGeometry(QtCore.QRect(190, 160, 191, 31))
        self.descripcion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.descripcion.setObjectName("descripcion")
        self.proveedor = QtWidgets.QTextEdit(MainWindow)
        self.proveedor.setGeometry(QtCore.QRect(190, 260, 191, 31))
        self.proveedor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.proveedor.setObjectName("proveedor")
        self.precioUnitarioVenta = QtWidgets.QTextEdit(MainWindow)
        self.precioUnitarioVenta.setGeometry(QtCore.QRect(190, 310, 191, 31))
        self.precioUnitarioVenta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.precioUnitarioVenta.setObjectName("precioUnitarioVenta")
        self.precioUnitarioCompra = QtWidgets.QTextEdit(MainWindow)
        self.precioUnitarioCompra.setGeometry(QtCore.QRect(190, 360, 191, 31))
        self.precioUnitarioCompra.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.precioUnitarioCompra.setObjectName("precioUnitarioCompra")
        self.categoria = QtWidgets.QComboBox(MainWindow)
        self.categoria.setGeometry(QtCore.QRect(190, 210, 191, 31))
        self.categoria.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.categoria.setObjectName("categoria")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.label_3 = QtWidgets.QLabel(MainWindow)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(MainWindow)
        self.label_4.setGeometry(QtCore.QRect(90, 150, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(MainWindow)
        self.label_5.setGeometry(QtCore.QRect(100, 200, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(MainWindow)
        self.label_6.setGeometry(QtCore.QRect(100, 250, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(MainWindow)
        self.label_7.setGeometry(QtCore.QRect(30, 300, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(MainWindow)
        self.label_8.setGeometry(QtCore.QRect(20, 350, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.agregar = QtWidgets.QPushButton(MainWindow)
        self.agregar.setGeometry(QtCore.QRect(150, 410, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);\n"
"")
        self.agregar.setObjectName("agregar")
        self.cancelar = QtWidgets.QPushButton(MainWindow)
        self.cancelar.setGeometry(QtCore.QRect(150, 470, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 111, 81))
        self.label_2.setStyleSheet("image: url(:/logo4/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nombre del Producto</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Descripción</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Categoria</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Proveedor</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Precio Unitario Venta</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Precio Unitario Compra</span></p></body></html>"))
        self.agregar.setText(_translate("MainWindow", "Agregar"))
        self.cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.categoria.setItemText(1,_translate("MainWindow","Abarrotes"))
        self.categoria.setItemText(2,_translate("MainWindow","Enlatados"))
        self.categoria.setItemText(3,_translate("MainWindow","Lacteos"))
        self.categoria.setItemText(4,_translate("MainWindow","Botanas"))
        self.categoria.setItemText(5,_translate("MainWindow","Cofinterias"))
        self.categoria.setItemText(6,_translate("MainWindow","Harinas"))
        self.categoria.setItemText(7,_translate("MainWindow","Frutas y verduras"))
        self.agregar.clicked.connect(self.llamar_a_las_demas)
        self.cancelar.clicked.connect(self.regresar_menu)


    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos2")

    def verificar_producto_exist(self):
        #se verificara que los parametros que paso el usuario no existan ya en la bdd y si es asi solo se actualizaran
        #o se mostrara una advertencia al usuario del caso.
        global nombreloc, descripcionloc, categorialoc, proveedorloc, preciounven, preciouncom
        global db, data
        global prodex,id


        cursor = db.cursor()

        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT ProductoId FROM producto WHERE Nombre = %s AND Descripcion = %s AND CategoriaId=%s AND ProveedorId =%s AND PrecioUnitarioVenta = %s AND PrecioUnitarioCompra = %s"
        val = (nombreloc, descripcionloc, categorialoc, proveedorloc, preciounven, preciouncom)

        cursor.execute(sql, val)

        #myresult = cursor.fetchall()
        data = cursor.fetchone()

        if(data==None):
            prodex = 0
        else:
            prodex = 1
            #sql ="SELECT EmpleadoId from empleado where "
            db.commit()
            id=data
            print("Existente ID")


    def insertar_dato(self):

        global nombreloc, descripcionloc, categorialoc, proveedorloc, preciounven, preciouncom
        global db, data
        global prodex,id

        if(prodex!=1): #si no existe se creara uno nuevo
            cursor = db.cursor()
            sql="INSERT INTO producto (Nombre, Descripcion, CategoriaId,ProveedorId, PrecioUnitarioVenta, PrecioUnitarioCompra) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (nombreloc, descripcionloc,categorialoc, proveedorloc, preciounven, preciouncom)
            cursor.execute(sql,val)
            data = cursor.fetchone()
            db.commit()
            print(cursor.rowcount, "record inserted.")
            ui.regresar_menu()
        else:
            cursor = db.cursor()
            sql="UPDATE producto SET Nombre = %s AND Descripcion = %s AND CategoriaId=%s AND ProveedorId =%s AND PrecioUnitarioVenta = %s AND PrecioUnitarioCompra = %s WHERE ProductoId=%s"
            val = (nombreloc, descripcionloc,categorialoc, proveedorloc, preciounven,  preciouncom, id)
            cursor.execute(sql,val)
            db.commit()
            data = cursor.fetchone()

            print("Actualizado")
            ui.regresar_menu()

    def tomar_datos(self):
        global nombreloc, descripcionloc, categorialoc,proveedorloc, preciounven, preciouncom

        nombreloc = ui.nombre.toPlainText()
        descripcionloc = ui.descripcion.toPlainText()
        categorialoc = ui.categoria.currentText()
        proveedorloc = ui.proveedor.toPlainText()
        preciounven = ui.precioUnitarioVenta.toPlainText()
        preciouncom = ui.precioUnitarioVenta.toPlainText()

    def categoria_dato(self):
        global categorialoc,db

        cursor2 = db.cursor()
        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT CategoriaId FROM categoria WHERE Nombre = %s"
        val = (categorialoc)
        cursor2.execute(sql,val)
        data=cursor2.fetchone()
        categorialoc=data



    def llamar_a_las_demas(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        ui.conectar_bdd()
        ui.tomar_datos()
        ui.categoria_dato()
        ui.verificar_producto_exist()
        ui.insertar_dato()
        ui.regresar_menu()
        db.close()

    def regresar_menu(self):
        
        sys.exit(app.exec_())



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_AgregarProducto()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
