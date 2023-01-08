# Diario personal en texto plano

Llega un nuevo año, un nuevo enero y normalmente la mayoría lo empezamos
planteándonos una serie de propósitos y proyectos. Yo este año, igual que hice
el pasado mi único propósito es el de seguir tirando más o menos haciendo lo
mismo. Falta de ambición, conservadurismo o lo que queráis pero es un buen
método para evitar frustraciones y malos rollos al terminar el año. Sobre el
teclado seguir tirando algo de Rust, olvidado desde hace dos o tres semanas,
sobre la bici intentar mantener el kilometraje de este año y además de todo
esto, seguir sacando algo de tiempo para leer a ratos.

Relacionado con todo esto, un propósito que me plantee hace ahora dos años y
que, contra todo pronóstico he seguido realizando diariamente ha sido la
elaboración de un pequeño diario o bitácora personal. La idea de esta bitácora
no era tanto expresar o anotar sentimientos personales sino más bien reflejar lo
acontecido a modo de bitácora *marinera* clásica. Me gustaba y me interesaba un
lugar donde poder reflejar aquellos pequeños eventos que suelen tener lugar en
nuestra vida diaria y que olvidamos con frecuencia: cruzarte con un compañero y
comentar un tema del trabajo, una pequeña compra que olvidas cuando la hiciste,
un arreglo que has hecho a la bicicleta, una serie de la que te han hablado o un
libro que has prestado, etc...

Cada uno de estos simples eventos los dejo reflejados con una frase corta, sin
florituras, y así cada día esta descrito por un párrafo fácil de leer. Las ideas
sobre las que construir esta bitácora cuando me la planteé eran, más o menos,
las siguientes:

* Debía de ser sencilla de mantener.
* Debía de poder se editada en todos mis dispositivos (móvil, portátil, pc, etc.).
* Debía de poder permitir buscar fácilmente acontecimientos pasados.
* Debía de ser concisa y compacta. 

Con estas ideas en la cabeza me puse a pensar y rápidamente me salió un formato
sencillo que tomó cuerpo rápidamente. Como formato utilicé ficheros de texto
plano que alojo en un repositorio git. Esto me permite editar esta bitácora de
forma sencilla en cualquier lugar. Para tenerla organizada uso sistema de
directorios sencillos que agrupan cada fichero de cada mes:


```
 bitacora
     |
     |------ 2022
     |       |------ 2022-01.md
     |       |------ 2022-02.md
     |       |------ 2022-03.md
     |       |------ un fichero por mes
     |
     |------ 2021
     |------ 2020
     |------ un directorio por año

```

Cada fichero de texto agrupa las entradas de cada día escritas en formato
Markdown. Cada entrada posee solo un título con la fecha de la entrada y el
texto asociado a ese día. Intento no escribir nada más que un párrafo por día
usando frases cortas para evitar enrollarme. 

Más adelante además he incorporado una extensión que me está siendo muy útil:
las etiquetas. Después de este primer párrafo donde cuento ligeramente lo que he
hecho en el día pongo frases o párrafos separados prefijados por una
palabra. Esta palabra la uso como etiqueta de ese párrafo y así puedo sacar (con
un pequeño programa del que ahora hablaré) todos los párrafos marcados con una
etiqueta concreta de un día o periodo de tiempo. Resumiendo, un fichero mensual
como los que uso tiene una forma parecida a esta:

```
# Marzo

## Sábado - 3 de Marzo

Nullam eu ante vel est convallis dignissim.  Fusce suscipit, wisi nec facilisis
facilisis, est dui fermentum leo, quis tempor ligula erat quis odio.  Nunc porta
vulputate tellus.  Nunc rutrum turpis sed pede.

trabajo: Aenean in sem ac leo mollis blandit.
deporte: Donec neque quam, dignissim in, mollis nec, sagittis eu, wisi.

## Viernes - 2 de Marzo

Fusce sagittis, libero non molestie
mollis, magna orci ultrices dolor, at vulputate neque nulla lacinia eros.  Sed
id ligula quis est convallis tempor.  Curabitur lacinia pulvinar nibh.  Nam a
sapien.

deporte: Aenean in sem ac leo mollis blandit.
```

Para hacer búsquedas rápidas, que es algo para lo que más me interesaba este
sistema, se pueden utilizar las herramientas clásicas de Linux como `grep` o
cualquier otro sistema de filtrado de patrones de tu editor de texto
favorito. El formato se puede extender mucho más allá como la inclusión de
menciones, imágenes incrustadas, etc. Por ahora, a mi este me sirve y me resulta
útil.

Además y con idea de practicar mi Rust, he construido una pequeña aplicación
llamada `journal` que me permite buscar entradas de días concretos, patrones o
filtrar por etiquetas. Si os interesa la tenéis alojada en [mi
github](https://github.com/sdemingo/journal). Y si alguien está interesado en que
describa algo más en detalle la aplicación que me lo haga saber por
correo/mastodon/... y añado una entrada sobre el tema.



---

Enero 2023
