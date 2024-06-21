#Importaciones
from base_de_datos import BaseDatos, config_bd

# Creamos un objeto base de datos
bd = BaseDatos(**config_bd)

# Mostramos algunas de las tablas
bd.mostrar_tablas()

# Una query sencilla devolviendo el primer resultado
select_query = "SELECT * FROM socioscompleto"
select_query_results = bd.consulta_one(select_query, display=False)

# Extraer los campos de una tabla
nombre_campos_tabla = bd.get_table_fields_names("socioscompleto")
print("\n***********************************************************************\n")

# Una query sencilla devolviendo todos los resultados y con display
select_query = "SELECT idSocio, FechaAltaSocio, TelefonoSocio FROM socioscompleto"
select_query_results = bd.consulta_one(select_query, display=True)

