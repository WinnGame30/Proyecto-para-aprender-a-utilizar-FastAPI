# Proyecto para aprender a utilizar FastAPI

Proyecto personal para aprender FastAPI y desarrollar APIs con Python

## Objetivo

Aprendizaje continuo y escalonado:
- APIs
- HTTP
- REST
- CRUD
- Manejo de Errores
- Documentación

## Contenido

- HTTP

### Notas Generales

#### 03/02/2026
##### HTTP
Protocolo de comunicación con el que seremos capaces de enviar y recibir información.

##### HTTPs
A diferencia de la primera, esta genera una conexión segura y encriptada entre el servidor y el cliente.

##### Cookies
Archivos que el cliente crea y almacena para guardar datos de navegación.

##### Sesión
Valores que se almacen en el servidor con la finalidad de almacenar información de una petición al pasar de una página a otra.

##### Verbos
Métodos para generar una buena comunicación entre el cliente y el servidor.
  - GET: Utilizar para obtener un objeto del servidor (imagén, video, etcétera)
  - POST: Crear recursos en el servidor (nuevos archivos)
  - PUT: Actualizar recursos en el servidor (registros o archivos existentes).
  - DELETE: Eliminar un recurso por parte del servidor.

##### Arquitectura CLIENTE-SERVIDOR
Un cliente (dispositivo) realiza una petición a un servidor (REQUEST) y el servidor entrega información (RESPONSE) al cliente mediante lo solicitado. Se utiliza el protocolo HTTP o HTTPS para realizar el envío de información entre uno y otro.

##### Status Code
Al utilizar, ya sea, el protocolo HTTP o HTTPS existen diferentes estatus para notificar el estado de una petición. Estos estatus se representan mediante un valor numérico, y a cada uno de estos valores se les conocen como status code.
Podemos agruparlos en 5 categorías.
  - Respuestas informativas (100–199),
  - Respuestas satisfactorias (200–299),
  - Redirecciones (300–399),
  - Errores de los clientes (400–499),
  - Errores de los servidores (500–599).

##### Arquitectura REST
Sistema que utiliza el Protocolo HTTP, y sus verbos (métodos), para definir las acciones a realizar. La utilización de las URLs como recursos para cada uno de los métodos, siendo capaz de tener 6 direcciones URL para cada recurso.

#### 04/02/2026

##### CURL
Herramienta de linea de comandos integrada para testear servicios web, transferir información para diferentes protocolos de internet (http, https, sttp, etcétera).

##### APIs
Siglas pertenecientes el título Apllication Programming Interface, utilizada para la comunicación entre aplicaciones. Existen 2 tipos de API:
  - Locales
  - Remotas: Se componen de servicios web

#### Buenas Practicas
- HATEOAS: La API se autodescribe; cada recurso tiene información de cual es el recurso siguiente o de la cantidad de recursos totales que hay.
- SEGURIDAD: Proteger las APIs privadas para evitar usurpación de información.
- TESTEAR: Para evitar problemas u errores mientras está en ejecución.
- DOCUMENTACION: Para poder compartir con los demás y sepan como funciona.