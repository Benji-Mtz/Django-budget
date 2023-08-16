# Ejecucion del proyecto

Para este caso solo necesitamos descargar el proyecto con el comando:

`git clone https://github.com/Benji-Mtz/Django-budget.git`

y seguimos los siguientes pasos:

```sh
cd Django-budget

# Creamos un entorno virtual
python3 -m venv .venv

# activamos el entorno virtual (en Linux) 
source .venv/bin/activate

# activamos el entorno virtual (en Windows)
.venv\Scripts\activate

# Instalamos las dependencias
pip install -r requirements.txt

# revisamos que se instalaron correctamente con 
pip freeze

# Ejecutamos las migraciones
python manage.py migrate

# Corremos la app con 
python manage.py runserver

# Entramos al navegador a la siguiente URL
http://127.0.0.1:8000/
```
Solo en caso de no obtener respuesta del servidor o tener algún error podemos correr los siguientes comandos y entrar a `http://127.0.0.1:8000/`

```
python manage.py makemigrations 
python manage.py migrate
```
Todo en la carpeta raíz del proyecto.