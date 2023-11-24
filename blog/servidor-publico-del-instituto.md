

# Un servidor público como red social adolescente

Hoy me apetece hablar sobre un proyecto en el que llevo trabajando a ratos durante los últimos dos años. El proyecto puede sonar descabellado así que antes de juzgarme como un loco os pido que leáis un rato más y quizás, solo quizás, os haga ver que no estoy tan loco ... o si. 

Hace unos dos años, se me ocurrió la idea de montar un servidor multiusario público para que cualquier alumno del instituto donde trabajo pudiera conectarse y usarlo. La idea es más antigua que el bosque. Cualquiera que conozca la filosofía de los [tildeservers o del tildeverso](https://tildeverse.org/) no le sonará a nuevo. Pero montar algo así pensando que a alumnos que se inician en la informática (o incluso en etapas más tempranas como el bachillerato) les pudiera resultar atractivo, no me negareis que es cuanto menos, arriesgado. Soy profesor de Formación Profesional, de la especialidad de informática, y entre otras asignaturas enseño sistemas operativos a futuros administradores de sistemas. Es un objetivo de esa asignatura que los alumnos adquieran una habilidad y una agilidad avanzada en el uso de sistemas Linux y de su consola de comandos. Conseguir esto en una máquina virtual, fría y solitaria es complicado por poco motivador para el alumno. Así que me propuse crear un entorno «social» donde los alumnos pudieran conectarse y, no solo trabajar, sino también interactuar de diferentes maneras. Así que preparé una máquina en la que instalé Linux y algunas otras herramientas y servicios. La máquina, por seguridad y confidencialidad no tiene casi ningún servicio expuesto. Esto quiere decir que los alumnos han de conectarse vía SSH a ella e interactuar desde dentro. Todo sin un entorno gráfico. Solo una interfaz de texto y comandos. Ahora mismo tengo funcionando allí las siguientes aplicaciones:

* Una herramienta (artesanal) de *bulletin board* donde todos pueden publicar, leer publicaciones de los demás y contestarlas.

* Un cliente de IRC que te permite solo conectarte al servidor IRC de la propia máquina para chatear en tiempo real con quien allí este conectado.

* Un CMS estático (artesanal)  que permite publicar artículos en un blog colaborativo. Los artículos se editan en Markdown y son moderados por mi antes de su publicación.

* Varios editores de texto para que trasteen y prueben.

* Varios compiladores e intérpretes para que trasteen y prueben.

* Un juego de ajedrez (artesanal) que permite jugar sobre la consola entre dos jugadores conectados al servidor.

* Por supuesto `tmux` para poder trabajar con sesiones y entornos.

* Y el resto de vitaminas que Debian trae de serie ...

Con todo esto listo y configurado empecé la promoción y la divulgación de las bondades de tener un usuario en el servidor. Di alguna charla rápida y estuve un tiempo proponiendo pequeños retos que consistían en buscar palabras escondidas entre cientos de ficheros con contenido «basura» y que obligaban a usar comandos básicos que estábamos viendo en clase: `head`,  `tail`, `wc`, `tr`, `grep`, `find`, `sed`, etc. 

Seguramente, si has llegado hasta aquí te intrigue saber como ha ido o está yendo la experiencia. Pues bien, nadie se extrañará si os digo que no ha sido un éxito abrumador. Es verdad que durante la publicación de los retos (el curso pasado) y tras las charlas se solía generar una expectativa alta y un pico de solicitudes acorde. Lo normal es que luego esto no se tradujera en una población estable y que la mayoría de esas altas abandonaba. Aún así, me quedo con la satisfacción de tener un pequeño grupo de usuarios para los que la máquina les está descubriendo un ecosistema nuevo para ellos: el de los servidores multiusuario. 

Hemos creado entre nosotros una especie de club «friki» que les está sirviendo de acicate para explorar el sistema y conocer muchas cosas fuera del currículum propuesto en sus asignaturas. Solo por eso, esta pequeña locura ya ha merecido la pena.



---

Noviembre 2023
