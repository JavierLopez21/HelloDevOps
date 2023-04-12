# HelloDevOps: Productivización de dashboard con Plotly en Nginx.

El propósito de este laboratorio es poder ejemplificar el usu de un ambiente de DevOps para el desarrollo de software, se tiene que considerar que los recursos que necesita el proyecto son grandes. Las fases que comprenden este proyecto son las siguientes:

## Entorno de versionado de código

La plataforma utilizada es GitHub, el cual cuenta con los WebHooks necesarios para poder integrarse a la plataforma de compilado y pruebas unitarias.

## Compilado y pruebas unitarias

La plataforma utilizada es Jenkins, éste paso fue construido a partir de un Webhook que apunta a un URL generado por ngrok el cual expone el servidor local de Jenkins a usuarios externos. Los elementos necesarios para su correcto funcionamiento son los siguientes:

<ul style="list-style-type:circle">
<li>Configuración Ngrok: Aquí se requiere apuntar de manera correcta el puerto en el cual se ejecuta el contenedor de Jenkins dentro de la máquina local, de tal forma que el URL que se genere pueda apuntar correctamente al servidor de Jenkins. La plataforma requiere de un token de autenticación de usuario que se puede generar a partir de la plataforma de Ngrok creando una cuenta gratuita.</li>
<li>Credenciales: Para la correcta integración del Webhook con la plataforma de jenkins se nececitan; un token generado por la palaforma de Jenkins para habiiltar el uso correcto de la API, el token generado para hacer uso de la API de GitHub con los permisos necesarios para que el Webhook se pueda ejecutar correctamente.</li>
</ul>
<b>NOTA</b>: Los URLs generados por Ngrok son validos hasta por 8 horas, por lo que cada sesión en la cual se desee ejecutar este entorno de DevOps será necesario actualizar dicho URL en las configuraciones de Jenkins y del Webhook.

## Almacén de imágenes

La plataforma utilizada es JFrog. Para su correcta automatización solo se requiere de las credenciales con las cuales se puede ingresar al contenedor de JFrog, de tal forma que al ejecutarse el proyecto construido en Jenkins las imágenes involucradas puedan guardarse de manera correcta.

## Despliegue de contenedores

La plataforma usada es Kubernetes.

## Almacén de información sensible

La plataforma usada es Hashicorp Vault.

## License

[MIT](https://choosealicense.com/licenses/mit/)
