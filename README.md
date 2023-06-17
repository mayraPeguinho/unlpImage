{Bienvenido a UNLP IMAGE}

Éste programa tiene cómo objetivo el poder crear memes y collages en base a diferentes imágenes, las cuales también pueden ser clasificadas mediante etiquetas y descripciones, todo esto hecho mediante distintos perfiles de usuarios los cuales también pueden configurar donde almacenar esos memes y collages creados, además de poder configurar el repositorio del cual se van a obtener esas imágenes. 

{COMO INSTALAR Y EJECUTAR CORRECTAMENTE EL PROGRAMA}

Para que el programa pueda correr y ejecutarse de manera correcta, es necesario tener instalado Python en su versión 3.11.2 o superior, además de las librerías PySimpleGUI en su versión 4.60.4 o superior y Pillow en su versión 9.5.0 o superior. 
Se recomienda ejecutar el comando "pip install -r requirements.txt"  desde alguna terminal ya sea desde Windows o Linux estando dentro del directorio raíz del programa para descargar las librerías utilizadas.
También, para un correcto funcionamiento del programa, se sugiere no eliminar el archivo de configuración ni modificar los permisos de acceso a los archivos del programa, el mismo podrá ejecutarse pero podría no funcionar de manera adecuada. 
Para utilizar la aplicación se deberá ejecutar el programa desde el archivo unlpimage.py

{PRIMEROS PASOS}

Para comenzar a utilizar UNLP image, lo primero que debemos hacer es crear nuestro perfil, haciendo click en el botón “+” completando los campos necesarios y eligiendo nuestra imágen de perfil. Si nuestro perfil ya fue creado anteriormente, solo debemos hacer click en nuestro perfil. 
En caso de querer editar el perfil, debemos hacer click en la foto elegida una vez que estemos en el menú principal del programa y completamos los campos a editar para luego aceptar estos cambios.


{COMO CONFIGURAR MIS DIRECTORIOS}

Para configurar nuestros directorios donde almacenar esos memes y collages creados, además del repositorio a donde iremos a buscar estas imágenes, debemos primeramente hacer clic en “Configuración” y luego elegimos cada directorio. Sugerimos no modificar la configuración por defecto para “Repositorio de imágenes” puesto que de momento UNLP image sólo puede crear memes con plantillas que ya están predefinidas y almacenadas en la carpeta que verán configurada por defecto. Además, es importante aclarar que estas carpetas deben estar o ser creadas dentro del repositorio raíz del programa, es decir, dentro de la carpeta donde se encuentra “UNLPimage.py” o cualquier subcarpeta que esté en su mismo directorio.



{COMO CREAR UN MEME}

Para crear un meme un UNLP image, una vez que iniciamos el programa y elegimos el perfil a utilizar, es hacer click en “Generar meme”, esto nos llevará a una pantalla donde tendremos acceso a nuestra carpeta repositorio de imágenes (en donde se encuentran todas las imágenes disponibles en nuestro programa, tanto para hacer memes como para hacer collages) y es ahí donde debemos seleccionar el template (plantilla) que vamos a usar, al ir moviéndonos entre los archivos de imágenes, el mismo programa nos indicará si la imagen que estamos intentando abrir es o no un template. 
Una vez que encontramos la imágen que queremos utilizar para generar el meme, hacemos click en “Generar”, lo que nos lleva a la siguiente pantalla. En esta pantalla, tenemos un botón para elegir la fuente que queremos utilizar, las cuales se encuentran en la carpeta “/grupo06/fuentes”, una vez seleccionada la fuente, elegimos que texto poner en cada cuadro de texto y podemos ir haciendo click en “Actualizar” para chequear que el texto se vea como nosotros deseamos o ir cambiandolo. 
Una vez que tenemos la imágen que queremos editada de la forma en que lo queremos, debemos hacer click en “Generar” y el sistema nos indicará que se creo un nuevo meme con éxito. 


{COMO CREAR UN COLLAGE}

Para crear un collage en UNLP image, desde el menú principal del usuario al seleccionar la opción “Generar Collage”, se muestra una pantalla, en dónde se muestran los distintos diseños para crear el  collage. Una vez seleccionado el diseño, se muestra la pantalla de creación , ahí se podrán seleccionar cada una de las imágenes a utilizar y el título que se desee.
Al hacer clic  en “Actualizar ”, se inserta el título sobre el collage. Finalmente una vez seleccionadas todas las imágenes y el título, al hacer clic en "Guardar", se solicita el ingreso del nombre con el cuál se desea guardar el collage y se muestra un mensaje de éxito, indicando que se guardó correctamente.
Es importante aclarar que es necesario completar todos los campos e imágenes para que el collage se genere correctamente, caso contrario el programa advertirá que no podrá crear el collage solicitado. 

{CÓMO CLASIFICAR IMÁGENES}

Para clasificar o etiquetar imágenes, debemos hacer click desde el menú principal en el botón “Etiquetar imágenes”, y accederemos a una pantalla que nos muestra del lado izquierdo los nombres de las imágenes almacenadas en nuestro repositorio y del lado derecho podremos visualizar la imágen en cuestión. Basta con agregar o eliminar tags y luego hacer clic en “Guardar”, para que éste cambio surja efecto y la imagen sea correctamente editada. 
Es importante aclarar que estas imágenes son buscadas en el repositorio de imágenes y si no tienes permiso para acceder a determinada carpeta o imágen, el programa no podrá acceder y emitirá una advertencia. 

