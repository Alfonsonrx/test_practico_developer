# Test Practico Developer con Python <a href="https://www.python.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/python-colored.svg" width="36" height="36" alt="Python" /></a> y PostGre <a href="https://www.postgresql.org/" target="_blank" rel="noreferrer"><img src="https://raw.githubusercontent.com/danielcranney/readme-generator/main/public/icons/skills/postgresql-colored.svg" width="36" height="36" alt="PostgreSQL" /></a>

### Nota: 
Para la tarea 1, debido a lo extenso de la respuesta de la api, se dividio en 2 modelos: Station y Extra
Extra vendria siendo una extension de Station, con su respectiva clave foranea, esto para no alargar la tabla de station y reducir la complejidad

## Crear el ambiente
<p>Antes de empezar a ejecutar, se requiere crear un ambiente virtual con las librerias necesarias, por lo cual debera ejecutar los siguientes comandos en la carpeta principal del repositorio:</p>

```
python -m venv venv

.\venv\Scripts\activate

pip install -r .\requirements.txt
```

## Migrar modelos a BDD
Tambien debemos ambientar la base de datos con la estructura necesaria, para ello hay que ejecutar los siguientes comandos en la carpeta "tareas_dev"

```
py .\manage.py makemigrations tarea1
py .\manage.py makemigrations tarea2

py .\manage.py migrate
```

## Conseguir los datos de proyectos
Debido a su demora y a que sera necesario despues la prioridad aqui sera el script de la tarea 2

Para ejecutar el script no hace falta mas que posicionar la terminal en la carpeta principal "tareas_dev" y ejecutar el siguiente comando:

```
python .\tarea2\contact_service.py
```

Y dejarlo corriendo hasta recolectar los datos y guardarlos en 'archivos_json/datos_proyectos.json'

## Correr el servidor
Ya con el ambiente dispuesto, para guardar la informacion e iniciar la app web, solamente hay que ejecutar

```
python .\manage.py runserver
```

La primera vez demorara un poco, luego ya teniendo la base de datos cargada iniciara de forma normal

## Visualizar la informacion en el administrador
Para visualizar la pagina de administrador y por tanto el primer punto opcional de cada tarea

Se requiere iniciar el servidor y dirigirse al link'http://127.0.0.1:8000/admin'

Recordatorio: Para ingresar se requiere super usuario, se puede crear uno con el comando:

```
py .\manage.py createsuperuser
```

# Nota Final
Por cuestiones de tiempo, realice esto la mitad del tiempo dispuesto en las instrucciones, por lo que asumo que no logre de momento realizar vistas con 
la informacion en bootstrap 5, a pesar de ser opcional estaba en mi objetivo cumplirlo tambien
