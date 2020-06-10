import pymysql

############### CONFIGURAR ESTO ###################
# Abre conexion con la base de datos
db = pymysql.connect("localhost","root","","pos")
##################################################

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql ="INSERT INTO acceso(EmpleadoID,Usuario, Contrasena)\
    VALUES (NULL,'{0}','{1}'".format("admin","1234")
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# desconecta del servidor
db.close()