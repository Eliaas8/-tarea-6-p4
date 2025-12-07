Biblioteca Personal – Flask + KeyDB
Descripción

Aplicación web desarrollada con Flask que permite gestionar una biblioteca personal.
Los datos se almacenan en KeyDB como objetos JSON usando estructuras clave-valor.

Tecnologías

Python

Flask

KeyDB

redis-py



Configuración

Crear el archivo .env:

KEYDB_HOST=localhost
KEYDB_PORT=6379
KEYDB_PASSWORD=
FLASK_SECRET=secret

Instalación
pip install -r requirements.txt

Ejecución

Iniciar KeyDB:

keydb-server


Ejecutar la aplicación:

python app.py


Abrir en el navegador:

http://127.0.0.1:5000

Funcionalidades

Agregar libros

Listar libros

Buscar libros

Editar libros

Eliminar libros

Almacenamiento en KeyDB

Clave:

libro:<id>


Valor:
JSON con los datos del libro (título, autor, género y estado).
