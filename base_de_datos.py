import mysql.connector

# conexion con la base de datos
config_bd = {"host": "127.0.0.1",
            "user": "root",
            "password": "",
            "database": "practica2_8"}

class BaseDatos:
    # Conexión y cursor
    def __init__(self, **kwargs):
        self.conector = mysql.connector.connect(**kwargs)
        self.cursor = self.conector.cursor(buffered=True)
    
    # Método de apoyo para mostrar resultados en consola 
    def display_row(self, row):
        for item in row:
            print(item, end="\t")
        print()

    # Consultas SQL: ONE
    def consulta_one(self, sql, display=True):
        self.cursor.execute(sql)
        resultados = self.cursor.fetchone()
        if display:
            self.display_row(resultados)
        return resultados
    
    # Consultas SQL: ALL
    def consulta_all(self, sql, display=True):
        self.cursor.execute(sql)
        resultados = self.cursor.fetchall()
        if display:
            for row in resultados:
                self.display_row(row)
        return resultados
    
    # Campos de la tabla
    def get_table_fields_names(self, table):
        resultado = self.consulta_all(f"SHOW COLUMNS FROM {table}", display=False)
        fields = [item[0] for item in resultado]
        return fields

    # Mostrar bases de datos
    def mostrar_bbdd(self):
        self.cursor.execute("SHOW DATABASES")
        for bd in self.cursor:
            print(bd)

    # Mostrar tablas
    def mostrar_tablas(self):
        self.cursor.execute("SHOW TABLES")
        for table in self.cursor:
            print(table)

    # Eliminar tablas en las bases de datos dado el nombre de la tabla
    def eliminar_tabla(self, nombre_tabla):
        pass

    # Creamos una función para insertar datos data la tabla en cuestión y los datos a insertar
    def insert(self):
        pass

    # Creamos una función para actualizar datos data la tabla en cuestión y los datos a insertar
    def update(self):
        pass
