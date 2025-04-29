import sqlite3
from DataBaseManager import DataBaseManager

dataBaseManager = DataBaseManager()


con = sqlite3.connect(dataBaseManager.database)
materia = (11, 'codificacion de software', 'Esau Perez Lopez', 8)
if dataBaseManager.es_materia_ya_registrada(con, materia):
    print("ya esta el registro")
else:
    dataBaseManager.registar_materia(con, materia)
cur = con.cursor()
cur.execute("Select * from materias;")
table_list = cur.fetchall()
for row in table_list:
    print(row)
con.close()