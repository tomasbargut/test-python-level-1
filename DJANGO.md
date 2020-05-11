####Creando el directorio del proyecto
~~~~
mkdir technical
cd technical
~~~~

#### Creando un entorno virtual para python 3
~~~~
python3 -m venv env
source env/bin/activate
~~~~

####Instalando Django y Django REST framework en el entorno virtual
~~~~
pip install django
pip install djangorestframework
~~~~

####Creando un nuevo proyecto con una aplicación
~~~~
django-admin startproject technical .
cd technical
django-admin startapp lab
cd ..
~~~~

####Sincronizando la base de datos por primera vez
~~~~
./manage.oy makemigrations
./manage.py migrate
./manage.py loaddata countries
~~~~

####Creando un usuario
~~~~
./manage.py createsuperuser --email admin@technical.coop --username admin
~~~~
