
Este sencillo script es usado para construir mi blog personal tanto en formato
html como en gemini.

## Configuración general del script

Para configurar correctamente el script a nuestro entorno hemos de dar el valor
adecuado a tres variables que encontraremos en la parte superior del fichero
`build`. Estas variables son:

- `INSTALL_BUILD`: Ruta de instalacion del script en nuestra cuenta
  personal. por defecto es `~/web`.
- `GEM_ROOT`: Ruta donde el script dejará los ficheros gemini. Por defecto es
  `~/public_gemini`.
- `HTML_ROOT`: Ruta donde el script dejará los ficheros HTML. Por defecto es
  `~/public_html`.


## Dependencias

Para que este script funcione correctamente es necesario utilizarlo sobre un
Linux convencional que debe tener instalado
[`pandoc`](https://pandoc.org). Además hemos de tener las siguientes librerías
de python disponibles en nuestro sistema:

- [md2gemini](https://pypi.org/project/md2gemini/)
- lxml
- beautifullsoup4
- feedgen
- markdown


## Configuración de la cuenta de goodreads

Para construir la lista libros desde Goodreads es necesario crear un fichero
llamado `goodreads.py` con las urls de los feeds en RSS que este servicio nos
ofrece. El fichero debe tener el siguiente aspecto:

```
currently="[url con la lista de los libros que actualmente estás leyendo]"
lasts="[url con la lista de los últimos libros]"
```

Estas urls las puedes conseguir dentro de tu perfil, en la parte inferior de la
página de "My Books". 


## Construcción y actualización

Para incluir un nuevo post en el blog hemos de crear el fichero `.md` dentro del
directorio `/blog`y luego incluir el nombre del fichero al final del fichero
`blog/INDEX`. Tras esto podemos ejecutar el comando

- `build --blog`: Para construir el blog
- `build --books`: Para construir la lista de últimas lecturas (solo si
  `goodreads.py` esta creado)
- `build --all`: Para construirlo tod
- `build --htmlonly`: Para construir solo el HTML o la versión web


```
$ cd ~/web
web$ echo "Nuevo post" > blog/nuevo-post.md
web$ echo "12/11/2022     blog/nuevo-post.md" >> blog/INDEX
web$ ./build --all
```
