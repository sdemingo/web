# Programar en Go



Estas navidades he aprovechado para ponerme a programar de nuevo en Go. Conozco este lenguaje desde su primera versión y he programado bastante con el. Recuerdo cuando se publicó esta primera versión, que gente como Rob Pike o Ken Thompson estuvieran detrás junto con toda la maquinaria de Google crearon muchas expectativas. En aquel momento muchos dijeron que venía a sustituir a C pero a poco que navegaras un poco en su arquitectura te dabas cuenta de que no podría ser así. La gestión de memoria, entre otras cosas hace que Go no sea el C-Killer que muchos todavía buscan cuando nos movemos cerca del metal a un nivel bajo.

De todas formas, creo que Go sigue siendo a día de hoy el mejor lenguaje en el campo de juego para el que está diseñado: sistemas concurrentes. Tiene una sintaxis sencilla y compacta que provoca que los códigos sean limpios y fáciles de depurar. Esto provoca, de manera implícita que los programas crezcan rápidos y sin muchos errores ocultos. Lo que convierte en un lenguaje de "alta productividad". Y además de todo esto posee un mecanismo de programación y comunicación entre hilos brutal.

Este fue sin duda lo que mas me atrajo de Go en sus orígenes. Por aquel entonces, (año 2011 o 2012 no recuerdo bien) yo estaba preparando mi tesis doctoral sobre sistemas distribuidos y trabajaba con sistemas como [Plan9](https://es.wikipedia.org/wiki/Plan_9) y un hermano pequeño llamado [Inferno](https://es.wikipedia.org/wiki/Inferno_%28sistema_operativo%29). Fue programando en aquel sistema cuando conocí la [comunicación CSP](https://en.wikipedia.org/wiki/Communicating_sequential_processes) y los canales. Esta es la arquitectura que usa Go para comunicar y sincronizar hilos dentro de un programa. Una mecanismo sencillo y fácil de gestionar que permite crear aplicaciones con un alto nivel de concurrencia de forma sencilla, rápida y sobre todo robusta.

Llevo casi diez años tirando código en Go, ahora que lo pienso y cada vez que vuelvo a el me encuentro lo mismo: una plataforma amigable y compacta, una documentación precisa y sin adornos y sobre todo, un lenguaje que permite escribir código a gran velocidad. Puedes tener un prototipo funcionando en unas horas y de ahí seguir hacia una aplicación completa en producción. En ese aspecto creo que solo puede rivalizar con Python, aunque Go cuenta para mi con la característica de ser tipado y compilado. Esto puede no ser algo que sume para todos pero para mi realmente lo es.

Go no llegó para "dominarnos a todos", llegó para tapar una necesidad que sus creadores, ingenieros de sistemas de Google principalmente, tenían: crear sistemas distribuidos y servidores de forma rápida y robusta. Y en mi opinión, es el mejor en lo suyo.


---

Enero 2022
