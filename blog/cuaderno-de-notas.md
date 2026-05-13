# Mi cuaderno de notas

Hoy por fin me he decidido a escribir un artículo sobre mi sistema de gestión de notas. Es algo que tenía pendiente de hacer desde hace tiempo y lo había dejado en la lista de artículos pendientes demasiado tiempo. Gestionar las notas y apuntes del día a día ha sido para mi siempre un tema que he necesitado revisar permanentemente. Desde que era joven he necesitado cuadernos y agendas para intentar recordarlo todo. Envidio a la gente que es capaz de llevar su vida en su cabeza. Yo desde luego no puedo. Siempre he buscado sistemas fáciles de usar, fáciles de gestionar y que pudiera llevar siempre encima.

Como podéis imaginar que he pasado por casi todos los sistemas: agendas, cuadernos «para todo», *bullet journal*, Google Keep, OrgZly, Evernote, etc. Desde hace aproximadamente siete u ocho años he conseguido consolidar un mecanismo sencillo, portable y de fácil acceso a través de todos mis dispositivos móviles y fijos. Este sistema no es ni más ni menos que un repositorio Git privado. Este repositorio lo visito, edito y sincronizo cómodamente desde cualquier equipo usando Emacs. Desde el teléfono o desde la tablet uso [ZettelNotes](https://www.zettelnotes.com/). Una aplicación pensada para el sistema [ZettelKasten](https://es.wikipedia.org/wiki/Zettelkasten) que yo no uso, pero que me permite sincronizar y visualizar un repo Git perfectamente. El *repo* en cuestión tiene el siguiente aspecto:

```
notebook/
    ├── articulos
    ├── bici
    ├── bin
    ├── ies
    ├── img
    ├── libros
    ├── notas
    └── tareas
        ├── 20251215121942.md
        ├── 20260423094329.md
        └── ...
```

El directorio que más uso en el día a día es `notas`. En el guardo ficheros en formato Markdown sobre aspectos de mi vida diaria. Cosas que tengo que recordar, listas de la compra, detalles sobre chapuzas, apuntes sobre reuniones, etc. Yo lo veo como un gran panel de *post-it*. No tiene subdirectorios porque quiero evitar navegaciones profundas, así que es una gran acumulación de ficheros. Cuando quiero buscar algo solo tengo que usar `grep` o el sistema de búsqueda de ZettelNotes. El directorio `ies` es algo parecido a notas pero solo para temas de trabajo y del instituto.

Otro directorio importante es `tareas`. En el guardo un fichero diferente por cada tarea que tengo pendiente por completar. Es un fichero sencillo, donde en el título escribo la tarea y en cuerpo del texto puedo incluir datos adicionales que me interesen. Cada fichero se nombra con la marca de tiempo en que se creó. Cuando la tarea se completa simplemente borro su fichero. Para llevar la cuenta del histórico de tareas completadas uso Git y recupero la lista de ficheros borrados en ese directorio con un pequeño script llamado `tareas-borradas`:

```
echo " Creada    -       Fichero            -  Título"
echo " ======            =======               ======"
git log -n $max_limit --diff-filter=D --pretty=format:'%H %ad' --date=short -- tareas | \
while read commit date; do
  git show --diff-filter=D --name-only --pretty=format: "$commit" -- tareas | \
  while read file; do
    title=$(git show "$commit"^:"$file" 2>/dev/null | head -n 1)
    echo "$date - $file - $title"
  done
done
```

El directorio `articulos` tiene artículos que voy guardando de entre todo lo que leo por ahí. Normalmente si un artículo me gusta suelo guardarme en enlace en un fichero dentro del directorio `notas`. Tengo varios ficheros llamados `notas/enlaces2026.md`, `notas/enlaces2025.md`, ... Pero cuando quiero conservar un artículo porque realmente me ha gustado mucho y creo que merece mucho la pena, directamente los descargo, lo limpio y lo guardo en formato Markdown en este directorio.

El directorio `bici` guarda notas sobre la bicicleta, rutas míticas en formato GPX, ficheros CSV con estadísticas e históricos, tutoriales sobre mantenimiento, bitácoras sobre las chapuzas que voy haciéndoles a mis bicis, etc. El directorio `libros` es algo parecido al anterior pero para la lectura. En el guardo la lista con todo lo que leo y estoy leyendo. Reseñas y notas sobre cada libro que termino y que suelo escribir para evitar olvidarlo. Hay también un subdirectorio llamado `citas` donde meto un archivo Markdown por cada autor, con citas que voy recopilando de sus libros.

Por último os hablaré de los dos únicos directorios que manejan ficheros que no son Markdown. Por un lado tengo el directorio `img` donde añado imágenes necesarias para algunas notas que tengo en `notas`. Intento evitar almacenar imágenes siempre pero hay veces que no tengo otra opción: diagramas, fotografías, capturas, etc. En ese caso las dejo siempre en este directorio. Y otro directorio especial es `bin`. En el recopilo todos los *scripts* artesanales que he ido desarrollando para mi día a día y que necesito en cada una de las máquinas donde trabajo. 

Es un sistema que nació de forma improvisada y que ha ido creciendo año a año. (ahora mismo tiene 448 archivos!). No tiene dependencias externas al margen de ZettelNotes que simplemente me sirve para editar y sincronizar por Git los ficheros en el móvi y por ello, tampoco la considero crítica. Seguramente no os parezca el mejor pero para mi lo importante es que me sirve y que lo tengo totalmente integrado en mi día a día tanto desde el móvil como desde los equipos de sobremesa con los que trabajo. Y esto es justo lo más importante del sistema. Me sirve y satisface todas mis necesidades y mientras lo haga, lo seguiré usando.

---
Mayo 2026
