
Este sencillo script es usado para construir mi blog personal tanto en formato
html como en gemini.

# Configuración de la cuenta de goodreads

Para construir la lista libros desde Goodreads es necesario crear un fichero
llamado `goodreads.py` con las urls de los feeds en RSS que este servicio nos
ofrece. El fichero debe tener el siguiente aspecto:

```
currently="[url con la lista de los libros que actualmente estás leyendo]"
lasts="[url con la lista de los últimos libros]"
```

Estas urls las puedes conseguir dentro de tu perfil, en la parte inferior de la
página de "My Books". 

# Construcción y actualización

Para incluir un nuevo post en el blog hemos de crear el fichero `.md` y luego
incluir su nombre al final del fichero `blog/INDEX`. Tras esto podemos ejecutar
el comando 

- `build.py --blog`: Para construir el blog
- `build.py --books`: Para construir la lista de últimas lecturas (solo si
  `goodreads.py` esta creado)
- `build.py --all`: Para construirlo todo

