

# Breve introducción a Python

Este tutorial esta basado en Python 2.6 que suele estar instalada de
serie en cualquier distribución de Linux moderna. Para realizar un
primer script en Python usaremos el siguiente esqueleto de archivo:

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
  
def main():
    codigo principal

if(__name__=='__main__'):
    main()

```

A partir de este momento, todo el código de los ejemplos del que no se
especifique lo contrario puede ser situado dentro de la función
principal llamada `main()`. Las dos primeras líneas permiten a bash
invocar el intérprete adecuado para ejecutar el resto de ordenes e
indicarle que está codificado en UTF-8.

Para ejecutar un código en Python debemos guardarlo en un fichero y
darle permisos de ejecución. Una vez hecho esto lo invocaremos como un
script clásico.

```
$ ./nombrefichero
```

## Variables


En Python una variable se crea en su primer uso. También podemos leer su
valor del teclado usando la función predefinida `raw_input()` de la
siguiente manera:

```
print 'Empezando ...'
a=raw_input()
```

De esta manera la variable 'a' obtendrá su valor del teclado y lo
almacenará como un literal o string. Si quieres que lo almacene como un
valor de otro tipo (entero, real, etc.) debes indicárselo explícitamente
al intérprete:

```
print 'Numero 1:'
a=int(raw_input())
print 'Numero 2:'
b=int(raw_input())
c=a+b
print c
```

## Tipos de datos


En Python usaremos los siguientes tipos de datos

-   Enteros (int)
-   Reales (float)
-   Cadenas (strings)
-   Lógicos o booleanos

## Listas

Las listas mantienen una colección ordenada de elementos. Para crear una
lista usaremos los corchetes. Para acceder una posición concreta de la
lista también usamos los corchetes seguida del ordinal de la posición.

```
lvacia=[]
lotra=[4,6,-1]
print lotra[0]
print lotra[0]+lotra[2]
```

## Instrucciones selectivas

La instrucciones selectiva que vamos a usar es la instrucción `if`. La
sintaxis del `if` en Python se puede ver en el siguiente ejemplo:

```
if (exp lógica):
    bloque de inst
else:
    bloque de inst
```

Tanto el `else` como su bloque de instrucciones son siempre optativos.


## Instrucciones iterativas {#inst.-iterativas .unnumbered}
Por un lado tenemos la instrucción `while`:

```
while (exp lógica):
    bloque de inst
```

También tenemos la instrucción `for`, que utiliza una lista para iterar
y pivotar el valor de una variable que sirve como controladora del
bucle:

```
for elem in lista:
    bloque de inst

```

En este caso, lista debe ser una variable de tipo lista en cualquier
caso.

## Funciones

Las funciones permiten agrupar código bajo un nombre común. Usaremos la
palabra reservada `def` para declarar una nueva función seguida de su
nombre y de sus parámetros de entrada. Las funciones pueden devolver un
valor directamente o a través de una variable usando el operador
`return`.

```
def mifunc (param1,param2):
     bloque de instrucciones
     return valor

```

## Uso de las librerías

Python cuenta con un gran número de librerías para manejar todo tipos de
datos (gráficos, strings, elementos de cifrado, etc.). Para utilizar una
librería primero hemos de informarnos de su nombre y de las funciones
que contiene. Lo ideal es usar la ayuda en línea que la comunidad de
Python ofrece a sus usuarios a través de su web en:
http://docs.python.org/library

Una vez ya conocemos el nombre de la librería que queremos usar hemos de
indicar al intérprete que vamos a usar sus funciones usando la
instrucción `import`. Esta declaración se hará al comienzo de nuestro
archivo, antes de cualquier otra declaración de función.

```
import strings
import sys
...

def func1():
     ...
def func2():
    ...
...
```

Una vez realizado el `import`, si queremos usar cualquier función de una
librería escribiremos el nombre de esta librería seguido del nombre de
la función y separado de esta por un '.'

```
import strings 
import sys 
...

def main(): 
    msg='frase de ejemplo' 
    msg2=string.upper(msg) 
    print msg2
```

## Manipulación de ficheros 


Los ficheros en Python se manipularán a través de la librería `file`.
Antes de manipular cualquier fichero hemos de abrirlo indicando el modo
de uso de este y la ruta en el sistema de ficheros. Tras abrirlo
podremos leerlo o escribirlo y por último siempre debemos cerrarlo.

En este ejemplo se ilustra como leer un fichero dejándolo en una
variable.

```
f=open('/ruta/f1','r')
cont=file.read(f)
file.close(f)
print 'El contenido es: '+cont
```

En este ejemplo vemos como escribir en un nuevo fichero:
```
f=open('/ruta/f2','w')
file.write(f,'blaaaa')
file.close(f)
```

# Librerías útiles

A continuación se listan algunos módulos que pueden resultaros útiles
para empezar a trabajar con Python. Podeis encontrar toda la información
sobre ellos en la web de Python.

-   string
-   math
-   random
-   os.path




---

Febrero 2009
