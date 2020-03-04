import sqlite3

class conect ():

    def __init__ (self):
        self.conector = sqlite3.connect("ejercicio")
        self.cursor = self.conector.cursor()

    def peticion(self, sql):

        self.cursor.execute(sql)

        self.conector.commit()

        self.conector.close()
    
 
        

