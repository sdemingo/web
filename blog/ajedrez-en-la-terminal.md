% Ajedrez en la terminal

- [Inicio](../index.html)


Llevo unos días trasteando con una pequeño programa que me encontré de casualidad rastreando por Github. Consistía en una pequeña interfaz de texto orientada a terminal de comandos construida sobre [Bubbletea](https://github.com/charmbracelet/bubbletea), una pequeña librería para hacer interfaces de texto con un aspecto muy cuidado. La interfaz, además de utilizar dicha librería para dibujar un tablero y las piezas utilizaba otra librería llamada [Dragontooth Movegen](https://pkg.go.dev/github.com/dylhunn/dragontoothmg) para controlar los movimientos legales del juego. Así que empecé a darle vueltas a la idea de engancharla un servidor para poder jugar partidas a dos. Sería una buena aplicación para poder utilizarla en un servidor compartido en el que no se disponga de entorno gráfico.

Me he puesto con ello a ratos y más o menos ayer conseguí tener una versión inicial de lo buscado. Ahora mismo tengo tanto la aplicación cliente llamada [gambit](https://github.com/sdemingo/gambit) como el servidor para jugar o [gambitsrv](https://github.com/sdemingo/gambitsrv) en una versión funcional. Ambos están programados en Go. Si alguien está interesado puede probarlo de forma sencilla arrancando, primero el servidor y luego dos clientes en su misma máquina (los clientes deben ser arrancado con nombres de jugadores diferentes).

Primero arrancamos el servidor que nos irá imprimiendo en pantalla mensajes de depuración que podemos redirigir a /dev/null.

```
$ gambitsrv
```

Ahora podemos arrancar el primer cliente. En caso de no pasarle un nombre de jugador con el argumento `-u` el cliente toma el nombre de tu usuario en el sistema.

```
$ gambit -u jugador1
```

Tras arrancar el primer cliente, el servidor nos devolverá en nuestra pantalla un identificador de 4 caracteres aleatorios. Esta es nuestra partida que hemos de comunicar al segundo jugador para que este pueda arrancar su cliente uniéndose a ella (usando el argumento `-g`):

```
$ gambit -u otrojugador -g edd4
```

Ahora mismo el cliente y el servidor utilizan un sencillo protocolo basando en mensajes muy sencillos que funciona sobre el puerto 22022. Cada mensaje está compuesto por:

* Un comando (byte)
* Jugador origen (string)
* Payload (string)

Estos mensajes se aplanan en JSON y se envían al servidor para que este los procese y los reenvíe al otro jugador en caso de ser necesario. Por ahora podemos crear tantas partidas simultáneas como queramos así que tengo algunas ideas para seguir avanzando en las próximas semanas:

* Añadir fichero con puntuaciones y clasificación
* Extender el protocolo para permitir ofrecer tablas
* Permitir que otros usuarios se unan a una partida en juego como espectadores
* ... 

Es posible que me falte algo de tiempo durante lo que queda de mes de Febrero porque mis Febreros suelen ser horripilantes. De todas las formas, como tampoco estamos hablando de una aplicación muy complicada, a ratos seguro que puedo meterla algo de código para ir avanzando.


---

Febrero 2022
