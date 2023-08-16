# Ejecucion del proyecto


```sh
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

# Corremos la app con 
python manage.py runserver

# Entramos al navegador a la siguiente URL
http://127.0.0.1:8000/
```

