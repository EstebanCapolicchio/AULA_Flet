import psycopg2
import os

class Recursos():
    def __init__(self, conn : psycopg2.connect):
        self.conn = conn
        self.cursor = self.conn.cursor()
    
    def get_recursos(self):
        result = self.cursor.callproc("get_recursos")
        return result

    def get_recurso(self, id_recurso):
        result = self.cursor.callproc("get_recurso", [id_recurso])
        return result

    def insert_recurso(self, id_recurso : int, nombre : str, descripción : str):
        self.cursor.callproc("insert_recurso", [id_recurso, nombre, descripción])
        self.conn.commit()
        return True