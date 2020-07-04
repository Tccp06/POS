# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModificarProducto.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql
import logomodificarproveedor


global idloc,nombreloc, descripcionloc, proveedorloc, preciounven, preciouncom
global db,data
global prodex,id

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(466, 600)
        MainWindow.setStyleSheet("background-color: rgb(247, 255, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.id = QtWidgets.QTextEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(190, 80, 171, 31))
        self.id.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.id.setObjectName("id")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 111, 81))
        self.label_2.setStyleSheet("image: url(:/logomp/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.nombre = QtWidgets.QTextEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(190, 130, 171, 31))
        self.nombre.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nombre.setObjectName("nombre")
        self.descripcion = QtWidgets.QTextEdit(self.centralwidget)
        self.descripcion.setGeometry(QtCore.QRect(190, 180, 171, 31))
        self.descripcion.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.descripcion.setObjectName("descripcion")
        self.precioUnitarioVenta = QtWidgets.QTextEdit(self.centralwidget)
        self.precioUnitarioVenta.setGeometry(QtCore.QRect(190, 330, 171, 31))
        self.precioUnitarioVenta.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.precioUnitarioVenta.setObjectName("precioUnitarioVenta")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(40, 320, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.proveedor = QtWidgets.QTextEdit(self.centralwidget)
        self.proveedor.setGeometry(QtCore.QRect(190, 280, 171, 31))
        self.proveedor.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.proveedor.setObjectName("proveedor")
        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(170, 430, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(255, 230, 109);")
        self.agregar.setObjectName("agregar")
        self.precioUnitarioCompra = QtWidgets.QTextEdit(self.centralwidget)
        self.precioUnitarioCompra.setGeometry(QtCore.QRect(190, 380, 171, 31))
        self.precioUnitarioCompra.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.precioUnitarioCompra.setObjectName("precioUnitarioCompra")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(110, 270, 71, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 370, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 120, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 170, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(120, 220, 61, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.categoria = QtWidgets.QComboBox(MainWindow)
        self.categoria.setGeometry(QtCore.QRect(190, 230, 171, 31))
        self.categoria.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.categoria.setObjectName("categoria")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(170, 490, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(100, 70, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 466, 26))
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
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Precio Unitario Venta</span></p></body></html>"))
        self.agregar.setText(_translate("MainWindow", "Editar"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Proveedor</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Precio Unitario Compra</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Nombre</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Descripción</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Categoria</span></p></body></html>"))
        self.cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">ProductoID</span></p></body></html>"))
        self.categoria.setItemText(1,_translate("Form","Abarrotes"))
        self.categoria.setItemText(2,_translate("Form","Enlatados"))
        self.categoria.setItemText(3,_translate("Form","Lacteos"))
        self.categoria.setItemText(4,_translate("Form","Botanas"))
        self.categoria.setItemText(5,_translate("Form","Cofinterias"))
        self.categoria.setItemText(6,_translate("Form","Harinas"))
        self.categoria.setItemText(7,_translate("Form","Frutas y verduras"))

    def conectar_bdd(self):
        global db
        ############### CONFIGURAR ESTO ###################
        # Abre conexion con la base de datos
        db = pymysql.connect("localhost","root","","pos2")




    def verificar_producto_exist(self):
        #se verificara que los parametros que paso el usuario no existan ya en la bdd y si es asi solo se actualizaran
        #o se mostrara una advertencia al usuario del caso.
        global idloc
        global db, data
        global prodex,id

        cursor = db.cursor()
        # ejecuta el SQL query usando el metodo execute().
        sql = "SELECT ProductoId FROM producto WHERE ProductoId=%s"
        val = (idloc)

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

        global idloc,nombreloc, descripcionloc, categorialoc, proveedorloc, preciounven, preciouncom
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
        else:
            cursor = db.cursor()
            sql="UPDATE producto SET Nombre = %s, Descripcion = %s, CategoriaId=%s, ProveedorId =%s, PrecioUnitarioVenta = %s, PrecioUnitarioCompra = %s WHERE ProductoId=%s"
            val = (nombreloc, descripcionloc,categorialoc, proveedorloc, preciounven,  preciouncom, idloc)
            cursor.execute(sql,val)
            db.commit()
            data = cursor.fetchone()
            print("Actualizado")



    def tomar_datos(self):
        global idloc,nombreloc, descripcionloc, categorialoc,proveedorloc, preciounven, preciouncom

        idloc= ui.id.toPlainText()
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
