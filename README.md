####Herramientas necesarias
- Pycharm Community   ( Versión homologada: 2020.1.1)
- git                 ( Versión homologada: 2.26.2 )
- python              ( Versión homologada: 3.8.2 )
- pip                 ( Versión homologada: 20.0.2 )
- django              ( Versión homologada: 3.0.6 )
- djangorestframework ( Versión homologada: 3.11.0 )
- curl                ( Versión homologada: 7.70.0 )

####Descargando el repositorio:
~~~~
 git clone git@gitlab.tecso.coop:tecso-public/test-python-level-1.git
~~~~

####Probando controllers (views django):
	
Obtener todos los paises:
~~~~
	curl -H 'Accept: application/json; indent=4' -u admin:admin http://localhost:8000/countries/
~~~~

Obtener el país con id = 3:
~~~~
	curl -H 'Accept: application/json; indent=4' -u admin:admin http://localhost:8000/countries/3/
~~~~

####Workflow:

- Descargar repositorio.
- Validar funcionamiento del proyecto ejecutando las indicaciones en **DJANGO.md** y utilizando los requests de prueba
mediante la utilizacion de "curl".
- Desde el Pycharm Community, importar el proyecto.
- Resolver los ejercios indicados.  Ver enuciados en **EJERCICIOS.md**.
- Agregar un archivo llamado **RESPUESTAS.md** que contenga todas las "curl requests" que permitan probar las
funcionalidades agregadas. 
- Crear nuevo proyecto GIT (en gitlab o github), pushear en este nuevo espacio el proyecto con todos los ejercicios
resueltos y enviar la url del repositorio para revision de las soluciones implementadas.  
- Asegurarse que los permisos de acceso al repositorio sean adecuados para que quien reciba la url pueda realizar
el clonado.

