### Respuestas ejercicio 1

1. Get titulares
    ~~~~
    curl -H 'Accept: application/json; indent=4' -u admin:admin http://localhost:8000/titulares/
    ~~~~

2. Post titular persona fisica
    ~~~~
    curl -X POST -H "Content-Type: application/json" -H 'Accept: application/json; indent=4' -u admin:admin http://localhost:8000/titulares/ --data '{"cuit": 23000000009, "tipo": 1}'
    ~~~~

3. Post titular persona juridica
    ~~~~
    curl -X POST -H "Content-Type: application/json" -H 'Accept: application/json; indent=4' -u admin:admin http://localhost:8000/titulares/ --data '{"cuit": 23000000019, "tipo": 2}'
    ~~~~

4. GET titular
    ~~~
    curl -H 'Accept: application/json; indent=4' -u admin:admin http://localhost:8000/titulares/1/
    ~~~

5. PUT titular
    ~~~~
    curl -X PUT -H "Content-Type: application/json" -H 'Accept: application/json; indent=4' -u admin:admin http://localhost:8000/titulares/1/ --data '{"cuit": 23000000009, "tipo": 2}'
    ~~~~

6. DELETE titular
    ~~~~
    curl -X DELETE -H 'Accept: application/json; indent=4' -u admin:admin http://localhost:8000/titulares/1/
    ~~~~

7. POST datos del titular en el caso de que la persona sea una persona FISICA
    ~~~~
    curl -X POST -H "Content-Type: application/json" -H 'Accept: application/json; indent=4' -u admin:admin http://localhost:8000/titulares/1/datos/ --data '{"nombre": "Tomas", "apellido": "Bargut", "dni": 39951593}'
    ~~~~

8. POST datos del titular en el caso de que sea una persona JURIDICA
    ~~~~
    curl -X POST -H "Content-Type: application/json" -H 'Accept: application/json; indent=4' -u admin:admin http://localhost:8000/titulares/2/datos/ --data '{"razon_social": "TB SA","anio_fundacion": 1996}'
    ~~~~

9. GET datos del titular
    ~~~~
    curl -H 'Accept: application/json; indent=4' -u admin:admin http://localhost:8000/titulares/1/datos/
    ~~~~
   
10. PUT datos datos en el caso de que sea una persona FISICA
    ~~~~
    curl -X PUT -H "Content-Type: application/json" -H 'Accept: application/json; indent=4' -u admin:admin http://localhost:8000/titulares/1/datos/ --data '{"nombre": "Tomas I", "apellido": "Bargut", "dni": 39951593}'
    ~~~~
    
11. PUT datos del titular en el caso sea persona JURIDICA
    ~~~~
    curl -X PUT -H "Content-Type: application/json" -H 'Accept: application/json; indent=4' -u admin:admin http://localhost:8000/titulares/2/datos/ --data '{"razon_social": "TB SA","anio_fundacion": 1995}'
    ~~~~

12. DELETE datos del titular
    ~~~~
    curl -X DELETE -u admin:admin DELETE http://localhost:8000/titulares/1/datos/