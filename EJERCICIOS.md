###Ejercicio 1:

Desarrollar todos los elementos necesarios: controladores (views django), rutas, repositorio, modelos, etc..) para
implementar un CRUD + listado de **titulares de cuentas corrientes** según las siguientes consideraciones:

- Un titular puede ser tanto una persona física como jurídica.
- Si el titular es una persona física, los atributos requeridos	serán los siguientes:
    - nombre (maximo 80 caracteres)
    - apellido (maximo 250 caracteres)
	- DNI
- Si el titular es una persona jurídica, los atributos requeridos serán los siguientes:
    - razon social (maximo 100 caracteres)
    - año de fundación
- Tanto para las personas fisicas como jurídicas, se requiere CUIT.
- No pueden existir 2 titulares con el mismo CUIT. 

Las funcionalidades requeridas (creacion, lectura, modificacion, borrado y listado) deberán exponerse en la API Rest.
Ademas de la implementación, se requieren tambien las request que permitan probar los endpoints utilizando la herramienta curl

###Bonus

Para mejorar la evaluación realizar las siguientes actividaes
- Api para obtener listado de personas según el tipo.
- Implementar pruebas de unidad con pyTest.
- Configurar un sistema de logs en archivos con rotacion por dia. Loguear como mínimo request y responses.
