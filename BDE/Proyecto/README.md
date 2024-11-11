# Desarrollo

En el deber ser, cuando se desarrollan proyectos de software con calidad existen tres entornos:

- local : tu maquina o pc en la que trabajas
- testing : entorno en donde se hacen pruebas antes de realizar los cambios
- produccion : entorno en donde esta alojado la aplicacion que actualmente esta siendo utilizada por los clientes(que pueden ser usarios finales o incluso otras aplicaciones/programas)

En este caso si continúan con la instalación escarian trabajando de manera local

## Local(opccionl)

### Instalación de Docker

Para el entorno de pruebas les recomiendo usar docker ya que es una tecnología que se van a encontrar en el futuro o alguna variante de ella. La siguiente es una guía para su instalación

**Nota:** Pueden pensar que 'contenedor' es lo mismo que una maquina virtual, es como si tuvieran una computadora dentro de otra computadora lo cual es util porque permite mantener las cosas separadas y en este caso instalar una base de datos de manera sencilla y en el momento que lo decidan pueden eliminarla sin tener que preocupares de desinstalar cosas

#### Windows

1. Descarga el instalador de Docker Desktop desde [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-windows).
2. Ejecuta el instalador y sigue las instrucciones en pantalla.
3. Una vez instalado, inicia Docker Desktop desde el menú de inicio.
4. Verifica la instalación abriendo una terminal y ejecutando:

    ```sh
    docker --version
    ```

#### macOS

1. Descarga el instalador de Docker Desktop desde [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-mac).
2. Abre el archivo `.dmg` y arrastra Docker a la carpeta de Aplicaciones.
3. Inicia Docker desde la carpeta de Aplicaciones.
4. Verifica la instalación abriendo una terminal y ejecutando:

    ```sh
    docker --version
    ```

#### Linux

Visita el siguiente [link](https://docs.docker.com/desktop/install/linux/) y selecciona la distribución. Verifica la instalación con:

```sh
    docker --version
```

Es probable que tengas que usar sudo como prefijo. Existan maneras de solucionar lo anterior agregando el usuario a un grupo especial.

### Replicar entorno Remoto en local

Una vez instalado docker podrán levantar una 'copia' de las configuraciones en el servidor remoto. Esto para que puedan hacer pruebas locales.
Ejecutar en el siguiente nivel de carpetas el comando `docker compose up -d`

```sh
./
├── docker-compose.yaml
└── sql
    └── 004_modelo_fisico.sql
```

Los siguientes comandos son los mas comunes:

```sh
# Construir las imágenes y levantar los contenedores en segundo plano
docker compose up -d

# Verificar el estado de los contenedores
docker compose ps

# Ver los logs de los contenedores
docker compose logs

# Detener y eliminar los contenedores, redes y volúmenes creados por docker-compose up
docker compose down
#Detener y eliminar la información de la base de datos
docker compose down -v
```

### Conexion al Docker

Para conectarse a la base de datos que está en el contenedor de Docker, se pueden utilizar los siguientes comandos de `psql`. A continuación, se detallan los valores específicos de la configuración y las credenciales:

- **Usuario**: `bde_user`
- **Contraseña**: `bd3_User#`
- **Base de datos**: `proyecto_final`
- **Host**: `localhost`
- **Puerto**: `5432`

#### Conexión a la base de datos

1. Abre una terminal.
2. Ejecuta el siguiente comando para conectarte a la base de datos:

    ```sh
    psql -h localhost -p 5432 -U bde_user -d proyecto_final
    ```

3. Cuando se te solicite, ingresa la contraseña: `bd3_User#`.

Estos pasos te permitirán conectarte a la base de datos `proyecto_final` que está ejecutándose en el contenedor de Docker.
