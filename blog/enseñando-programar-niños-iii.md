# Enseñando a programar a un niño (III)

- [1º Parte](enseñando-programar-niños.md.html)

- [2º Parte](enseñando-programar-niños-ii.md.html)



La navidad ha pasado rápido y no hemos tenido tanto tiempo para practicar como
hubiéramos querido. Además, los reyes magos vinieron acompañados de un par de
juegos de la switch y eso, claro está, rivaliza muy seriamente con Logo. Por
todo ello se entiende que el alumno haya estado ciertamente disperso y
desconectado una temporadita.

A pesar de todo hemos conseguido atraparle un ratillo y hemos avanzado sobre un
concepto ya explicado en anteriores artículos: el de la rutina o
procedimiento y hemos incorporado un concepto nuevo: la variable.

La variable, aunque parezca mentira, no ha sido difícil de entender. Utilizando
la analogía de "lugar donde se guarda un dato" dentro del ordenador creo que ha
llegado a calar en el alumno. Para ayudar además he utilizado un mecanismo
tremendamente atractivo para cualquier niño: los números aleatorios. 

## La aleatoriedad mola

Después de explicarle brevemente lo que era un número aleatorio he utilizado un
generador de números pseudoaleatorios que trae Logo incorporado de serie usando
la instrucción `RANDOM`. De esta forma, he preferido explicarle el concepto de
variable como lugar donde el programa debe guardar el dato que ha generado o
creado para no perderlo. Por eso hemos de usar una variable. 

Vamos a hacer que la tortuga nos sorprenda y camine un número aleatorio de pasos:

```	
	make "numero (random 100)
	fd numero
```

Hay que reconocer que la aleatoriedad ha calado muy bien y le ha ayudado a
engancharse a lo explicado gracias a que el alumno es un "viciado" de
Minecraft. En este juego ya está más o menos familiarizado con el concepto de
semilla y de generador de aleatoriedad. Hay que motivar con lo que se tiene a
mano y en mi caso particular, sabía que esto iba a funcionarme. Después de
varias pruebas mezclando giros y repeticiones hemos creado varios patrones de
movimiento aleatorio en una serie que hemos llamado 'La tortuga borracha'.

## Procedimientos con parámetros

Viendo que tenía toda su atención he querido completar la sesión introduciendo
un concepto con el que trabajaremos bastante en las próximas sesiones: los
procedimientos con parámetros. En la sesión anterior ya hicimos un procedimiento
para hacer un cuadrado de tamaño fijo pero esta vez hemos visto como hacer que
un procedimiento te funcione para hacer cuadrados de cualquier tamaño. 

Esto ha sido más complicado porque el alumno, por su edad, aún no ha recibido los conceptos
algebraicos de incógnita que sin duda hubieran facilitado mucho entender todo
esto. Aún así creo que más o menos, algo ha pillado. Hemos creado el siguiente
procedimiento para construir cuadrados:


```
	? to cuadrado :lado
	> repeat 4 [ fd lado rt 90 ]
	> end
	cuadrado defined
	?
	?
	? cuadrado 50
	? cuadrado 100
	? cuadrado 200
``` 

Queda pendiente un ejercicio muy chulo que se me ha ocurrido y que, por falta de
tiempo no entró en esta sesión. El ejercicio sería algo así como mover repetidas
veces la tortuga a puntos aleatorios y dibujando sobre ellos cuadrados de tamaño
aleatorio. El resultado, siempre sorprendente, creo que ayudará a darle un toque
'mágico' a la práctica. Porque como he dicho ya, la aleatoriedad mola.



---

Enero 2022
