# Como construyo esta web

Hace casi dos años que empecé a publicar este blog. Anteriormente he tenido
otros, en otros formatos: Wordpress, Blogger, Github, etc. Centrados en
temáticas concretas y siempre quedaban abandonados por pereza y desánimo de
escribir generalmente. Así que al replantearme lo de escribir de nuevo en mi
blog me centré en dos aspectos sobre los que haría girar esto: 

* El blog sería totalmente generalista. Escribiría de cualquier asunto fuera
  cual fuera su temática: programación, libros, series, pensamientos, etc.
  
* Quería algo totalmente construido por mi, estático, autoalojado y sin
  maquinaria adicional de ningún tipo. Algo basado en la llamada [Small
  Web](https://web0.small-web.org/) o web0.
  
Los contenidos deberían quedar plasmados en simples archivos en formato Markdown
y de ahí construir una página principal, un índice de artículos ordenados por
fecha y alguna cosa más que se me ocurriera. Me puse manos a la obra con un
simple [script de Python de 500
líneas](https://github.com/sdemingo/web/blob/main/build) (que podría ser mucho
más limpio y compacto) surgió esta web.

Hoy he aprovechado a darle una capa de pintura nueva y actualizar algo la
visualización. Así que aprovechando que tengo el salón recién pintado vengo a
hablaros de como funciona el invento y así, quien le apetezca tener un rincón
personal, sencillo y práctico en Internet puede copiarme la idea. El script de
construcción tiene la siguiente funcionalidad:

* Convierte cada artículo en Markdown en un documento en HTML
* Crea un documento índice en HTML donde cada de los anteriores está enlazado
  indicando la fecha de publicación
* Crea un feed RSS para que quien quiera pueda estar al día de mis publicaciones
* Construye un documento HTML con las últimas lecturas que he anotado en
  Goodreads
* Repite todo lo anterior exportándolo todo a
  [Gemini](https://geminiprotocol.net/docs/es/faq.gmi)
  
## Construcción del blog

La base principal de la web claramente es el blog. Cuando pensé en como
organizar mis artículos quería que cada uno de ellos estuviera aislado en un
fichero diferente en mi disco. Quería además poder nombrar ese fichero usando
una cadena de letras que hiciera referencia al título. Nada de numerajos para la
fecha. Usar fechas en formato numérico para nombrar ficheros utilizando el
formato `AAAAMMDD` (siendo AAAA el año, MM el mes y DD el día) es obviamente la
solución más sencilla para tener perfectamente ordenados los ficheros del
blog. Te soluciona fácilmente el problema de ir procesándolos en orden también,
pues el sistema operativo le dará a Python una lista ya ordenada con ellos. Pero
yo no quería este formato. 

Así que en un directorio guardo todos mis artículos nombrados con palabras y
guiones y además, almaceno un fichero adicional donde relaciono la fecha de
publicación de cada artículo y el nombre del fichero donde escribí el
artículo. Así tengo el problema solucionado. Algo similar a:

```
25/04/2022  articulo-inicial.md libros,pensamientos
23/07/2022  otro-articulo-mas-sobre-otra-cosa.md novedades
30/11/2022  seguimos-escribiendo.md novedades
...
```

En este fichero guardo también una serie de palabras clave o categorías que
definen la temática del artículo y que irán reflejadas en el índice final del
blog. Están colocadas en la tercera columna, tras el nombre del fichero de cada
artículo. Para convertir cada documento Markdown en HTML simplemente utilizo la
librería [Markdown](https://pypi.org/project/Markdown/) de Python. Y tras
obtener el HTML en crudo le aplico una plantilla para adornarlo con la
estructura HTML básica que quiero para mi artículo. Esto lo hago usando objetos
`Template`. Evidentemente tengo guardado los ficheros plantilla en otro
directorio aparte.

```
rawhtml = markdown.markdown(mdcontent)
  html=postTemplate.substitute(post=rawhtml,post_title=title)
  with open(HTML_ROOT + HTML_BLOG + "/" +mdfile+".html","w") as fh:
    fh.write(html)
    fh.close();
```


## Construcción del feed RSS

Cuando construí el blog quería también tener un feed RSS para permitir que todo
aquel que quisiera pudiera suscribirse a mis actualizaciones. Para generarlo
utilizo la librería
[FeedGenerator](https://pypi.org/project/feedgenerator/). Esta librería es muy
sencilla de usar y basta con ir artículo a artículo construyendo una entrada
nueva en el feed con los datos que nos interesen de cada artículo:

```
for fileInfo in files:
    fe = fg.add_entry()
    url="http://"+urllib.parse.quote("panicerror.org/blog/"+fileInfo[0]+".html")
    fe.id(url)
    fe.title(fileInfo[1])
    tdate=datetime.strptime(fileInfo[2],"%d/%m/%Y").replace(tzinfo=timezone.utc)
    fe.published(tdate)
    fe.updated(tdate)
    fe.content(fileInfo[5],type="html")
    fe.link(href=url)
```

Al principio no metía el texto completo de los artículos en el feed simplemente
por no llenarlo en exceso pero luego cambié de opinión. Yo mismo soy de los que
les gusta leer nuevos post directamente en el lector de feeds y no me gusta que
me obliguen a salir de el, así que cambié y ahora meto todo el contenido del
artículo.



## Lista de lecturas

Una cosa que añadí más tarde es los últimos libros que he leído. Estos los saco
de mi feed de Goodreads. El feed lo obtengo a través de una url con todas mis
lecturas que proceso con
[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). Esta
archiconocida librería es una de las mejores a la hora de *scrapear* fácilmente
contenido web. Simplemente busco etiquetas con la clase `item` y de ahí extraigo
los diferentes atributos de cada lectura: el título, el autor, incluso la imagen
de portada.

```
for item in soup.findAll("item"):
      title=item.title.text
      imglink=item.book_medium_image_url.text
      booklink=item.link.text
      author=item.author_name.text
      description=item.book_description.text
      read_at=item.user_read_at.text
      reads.append((title,author,imglink,booklink,description,read_at))
```


## Exportar a Gemini

Todo esto lo quería también publicar en mi cápsula Gemini que tengo alojada en
el tilde hispanohablante [TextoPlano](https://texto-plano.xyz/). Para convertir
a Gemtext cada archivo Markdown simplemente utilizo la librería
[md2gemini](https://pypi.org/project/md2gemini/). Al principio yo mismo hacía la
conversión pero resulta más sencillo utilizar esta librería porque reconoce
casos que yo no llegaba a terminar de procesar. 

```
gemini = md2gemini(markdown, links="at-end")
```


La generación del índice en la cápsula gemini lo realizo usando el mismo proceso
de plantillas o *templates* que uso para la publicación en HTML.


## Y esto sería todo

El script es tremendamente artesanal y no creo que pueda ser utilizado
directamente por nadie pero pongo todo esto por aquí por si os sirve de
inspiración para crear vuestra propia web autoalojada. Existen multitud de
generadores sencillos que os permitirán hacer cosas parecidas de forma mucho más
profesional como Pelican, Github Pages, o Codeberg. Pero a mi, personalmente me
encanta haber perdido el tiempo en hacerme mi propio apaño.




---

Noviembre 2023
