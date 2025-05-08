import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="rootpass"
)

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS cartelera;")
cursor.execute("USE cartelera;")

cursor.execute("""
CREATE TABLE IF NOT EXISTS peliculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    genero VARCHAR(100),
    duracion INT
);
""")

print("Base de datos y tabla creadas correctamente.")
cursor.close()
conn.close()
