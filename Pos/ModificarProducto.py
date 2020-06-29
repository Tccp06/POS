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
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color: rgb(157, 155, 155);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, -10, 181, 131))
        self.label_2.setStyleSheet("image: url(:/logomp/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.id = QtWidgets.QTextEdit(self.centralwidget)
        self.id.setGeometry(QtCore.QRect(280, 110, 191, 41))
        self.id.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.id.setObjectName("id")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(120, 110, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.nombre = QtWidgets.QTextEdit(self.centralwidget)
        self.nombre.setGeometry(QtCore.QRect(280, 160, 191, 41))
        self.nombre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.nombre.setObjectName("nombre")
        self.descripcion = QtWidgets.QTextEdit(self.centralwidget)
        self.descripcion.setGeometry(QtCore.QRect(280, 220, 191, 41))
        self.descripcion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.descripcion.setObjectName("descripcion")
        self.precioUnitarioVenta = QtWidgets.QTextEdit(self.centralwidget)
        self.precioUnitarioVenta.setGeometry(QtCore.QRect(280, 390, 191, 41))
        self.precioUnitarioVenta.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.precioUnitarioVenta.setObjectName("precioUnitarioVenta")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 390, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.proveedor = QtWidgets.QTextEdit(self.centralwidget)
        self.proveedor.setGeometry(QtCore.QRect(280, 330, 191, 41))
        self.proveedor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.proveedor.setObjectName("proveedor")
        self.agregar = QtWidgets.QPushButton(self.centralwidget)
        self.agregar.setGeometry(QtCore.QRect(450, 500, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(54, 159, 224);")
        self.agregar.setObjectName("agregar")
        self.precioUnitarioCompra = QtWidgets.QTextEdit(self.centralwidget)
        self.precioUnitarioCompra.setGeometry(QtCore.QRect(280, 450, 191, 41))
        self.precioUnitarioCompra.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.precioUnitarioCompra.setObjectName("precioUnitarioCompra")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(130, 330, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 450, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 160, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(110, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 270, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 0, 281, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.categoria =QtWidgets.QTextEdit(MainWindow)
        self.categoria.setGeometry(QtCore.QRect(280, 270, 191, 41))
        self.categoria.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.categoria.setObjectName("categoria")
        self.cancelar = QtWidgets.QPushButton(self.centralwidget)
        self.cancelar.setGeometry(QtCore.QRect(630, 500, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
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
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Precio Unitario Venta</span></p></body></html>"))
        self.agregar.setText(_translate("MainWindow", "Agregar"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Proveedor</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt;\">Precio Unitario Compra</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Nombre</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Descripción</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Categoria</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p>Modificar Producto</p></body></html>"))
        self.cancelar.setText(_translate("MainWindow", "Cancelar"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">ProductoID</span></p></body></html>"))

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
        categorialoc = ui.categoria.toPlainText()
        proveedorloc = ui.proveedor.toPlainText()
        preciounven = ui.precioUnitarioVenta.toPlainText()
        preciouncom = ui.precioUnitarioVenta.toPlainText()





    def llamar_a_las_demas(self):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        ui.conectar_bdd()
        ui.tomar_datos()
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
    ui,cancelar
    sys.exit(app.exec_())
