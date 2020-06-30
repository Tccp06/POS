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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(784, 588)
        Form.setStyleSheet("background-color: rgb(157, 155, 155);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 20, 251, 91))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nombre = QtWidgets.QTextEdit(Form)
        self.nombre.setGeometry(QtCore.QRect(260, 170, 191, 41))
        self.nombre.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.nombre.setObjectName("nombre")
        self.descripcion = QtWidgets.QTextEdit(Form)
        self.descripcion.setGeometry(QtCore.QRect(260, 230, 191, 41))
        self.descripcion.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.descripcion.setObjectName("descripcion")
        self.proveedor = QtWidgets.QTextEdit(Form)
        self.proveedor.setGeometry(QtCore.QRect(260, 340, 191, 41))
        self.proveedor.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.proveedor.setObjectName("proveedor")
        self.precioUnitarioVenta = QtWidgets.QTextEdit(Form)
        self.precioUnitarioVenta.setGeometry(QtCore.QRect(260, 400, 191, 41))
        self.precioUnitarioVenta.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.precioUnitarioVenta.setObjectName("precioUnitarioVenta")
        self.precioUnitarioCompra = QtWidgets.QTextEdit(Form)
        self.precioUnitarioCompra.setGeometry(QtCore.QRect(260, 460, 191, 41))
        self.precioUnitarioCompra.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.precioUnitarioCompra.setObjectName("precioUnitarioCompra")
        self.categoria =QtWidgets.QTextEdit(Form)
        self.categoria.setGeometry(QtCore.QRect(260, 280, 191, 41))
        self.categoria.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "font: 14pt \"Bahnschrift Condensed\";")
        self.categoria.setObjectName("categoria")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(120, 170, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(90, 230, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(110, 280, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(110, 340, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(30, 400, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 460, 201, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.agregar = QtWidgets.QPushButton(Form)
        self.agregar.setGeometry(QtCore.QRect(420, 530, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Condensed")
        font.setPointSize(16)
        self.agregar.setFont(font)
        self.agregar.setStyleSheet("background-color: rgb(54, 159, 224);")
        self.agregar.setObjectName("agregar")
        self.cancelar = QtWidgets.QPushButton(Form)
        self.cancelar.setGeometry(QtCore.QRect(610, 530, 141, 41))
        self.cancelar.setStyleSheet("background-color: rgb(247, 33, 33);\n"
"background-color: rgb(213, 28, 28);\n"
"font: 16pt \"Bahnschrift Condensed\";")
        self.cancelar.setObjectName("cancelar")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(570, 10, 181, 131))
        self.label_2.setStyleSheet("image: url(:/logo4/6df038e0-5ff1-44e3-a6d8-5ab453bee65b_200x200.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p>Agregar Producto</p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">Nombre</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">Descripción</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">Categoria</span></p></body></html>"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:18pt;\">Proveedor</span></p></body></html>"))
        self.label_7.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">Precio Unitario Venta</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt;\">Precio Unitario Compra</span></p></body></html>"))
        self.agregar.setText(_translate("Form", "Agregar"))
        self.cancelar.setText(_translate("Form", "Cancelar"))

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
        categorialoc = ui.categoria.toPlainText()
        proveedorloc = ui.proveedor.toPlainText()
        preciounven = ui.precioUnitarioVenta.toPlainText()
        preciouncom = ui.precioUnitarioVenta.toPlainText()


    def llamar_a_las_demas(self):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        ui.conectar_bdd()
        ui.tomar_datos()
        ui.verificar_producto_exist()
        ui.insertar_dato()
        db.close()

    def regresar_menu(self):
        self.Form = QtWidgets.QWidget()
        self.ui = InicioAdmin.Ui_Form()
        self.ui.setupUi(self.Form)
        self.Form.show()
        Form.hide()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    ui.agregar.clicked.connect(ui.llamar_a_las_demas)
    sys.exit(app.exec_())
