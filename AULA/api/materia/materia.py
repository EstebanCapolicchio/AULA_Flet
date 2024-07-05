import psycopg2
import os

class Materia():
    def __init__(self, conn : psycopg2.connect):
        self.conn = conn
        self.cursor = self.conn.cursor()
    
    def get_materias(self):
        result = self.cursor.callproc("get_materias")
        return result

    def get_materia(self, codigo_guarani):
        result = self.cursor.callproc("get_materia", [codigo_guarani])
        return result

    def insert_materia(self, codigo_guarani : str, carrera : str, nombre : str, anio : str, cuatrimestre : str, taxonomia : str, horas_semanales : str, comisiones : str ):
        self.cursor.callproc("insert_materia", [codigo_guarani, carrera, nombre, anio, cuatrimestre, taxonomia, horas_semanales, comisiones])
        self.conn.commit()
        return True