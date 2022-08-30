% Enseñando a programar a un niño (II)

- [1º Parte](enseñando-programar-niños.md.html)
- [Inicio](../index.html)

Hemos estado estas últimas semanas trabajando en sesiones cortas con Logo y creo que hemos avanzado bastante. Voy a resumiros brevemente los principales avances con algunos ejercicios que he planteado. Lo primero, lógicamente, ha sido comprender los comandos básicos (avanzar o `fd`, girar `rt` o `lt`, etc.). Para ello usar figuras sencillas como rectángulos o cuadrados es fundamental.

Veamos un ejemplo de cuadrado sencillo dibujado hacia arriba y hacia la derecha de la posición inicial de la tortuga (que en los diagramas he representado con una `@`):

```	

	+-----------+
	|           |
	|           |
	|           |
	|           |
	|           |
	|           |
	@-----------+
	

	? fd 50
	? rt 90
	? fd 50
	? rt 90
	? fd 50
	? rt 90
	? fd 50
	? rt 90
```

El cuadrado además nos ha permitido trabajar en la idea de patrón. Una secuencia de instrucciones que puede repetirse y que se puede expresar, por tanto, con una instrucción iterativa más sencilla. En el caso de Logo, con la instrucción `repeat`.

Logo permite secuenciar instrucciones en una sola línea. Usando su limpia sintaxis donde cada instrucción solo admite un parámetro separado por espacio podemos tener entonces secuencias muy claras y legibles. Tras unos minutos de explicación, el patrón de la secuencia anterior se saca fácilmente y, se entiende que debe repetirse 4 veces para formar el cuadrado anterior.

Usamos entonces la instrucción `repeat` y se comprueba que el trazado de la tortuga es similar al primero.

```
	? repeat 4 [ fd 50 rt 90 ]
```

Trabajamos en esto mismo un par de sesiones cortas más y el mecanismo de extracción de un patrón que se repite queda bastante claro. !Primer éxito!

Con este concepto bien asentado vamos un paso más allá, hacia la reutilización de patrones usando procedimientos. Para explicar esto al niño uso metáforas ya conocidas como los juegos de construcción de bloques. La idea que transmito es que podemos "enseñar" al computador ideas de nuestro mundo, como lo que es un cuadrado, y hacer que el las repita cuando queramos. Para ello usamos la instrucción `to` que nos permite crear el procedimiento `cuadrado`.

```
	? to cuadrado
	> repeat 4 [ fd 50 rt 90 ]
	> end
	cuadrado defined
``` 

Ahora ya solo falta acabar de ilustrar como reutilizar esta nueva pieza en un montaje algo más complejo. Dibujamos en un papel cuadriculado (que por cierto es fundamental tener a mano cuando trabajamos con Logo), la figura que queremos representar. El niño entiende a la primera que el cuadrado será reutilizado tres veces pero lo más complicado de hacerle ver es que además de dibujar el cuadrado hemos de resituar la tortuga cada vez que terminemos un cuadrado.

Tras terminar cada cuadrado, la tortuga finaliza mirando hacia arriba y en la esquina inferior izquierda del cuadrado. El cuadrado siguiente ha de partir sobre la esquina superior derecha, así que hemos de llevar hasta allí a la tortuga antes de reutilizar el procedimiento `cuadrado`.

Tras un par de ensayos erróneos consigue dar con la secuencia correcta ¡Segundo éxito!

```


	                        +-----------+
	                        |           |
	                        |           |
	                        |           |
	                        |           |
	                        |           |
		                    |           |
	            +-----------+-----------+
	            |           |
	            |           |
	            |           |
	            |           |
	            |           |
		        |           |
	+-----------+-----------+
	|           |
	|           |
	|           |
	|           |
	|           |
	|           |
	@-----------+


	? repeat 3 [cuadrado fd 50 rt 90 fd 50 lt 90]

```

Todo esto ha sido el trabajo de unas cuatro sesiones de aproximadamente veinte minutos separadas entre cuatro y siete días cada una. Personalmente, cuanto más uso esta herramienta más convencido estoy de que es ideal para transmitir pensamiento computacional a niños entre los 8 y los 11 o 12 años.




---

Diciembre 2021
