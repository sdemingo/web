

# Buscando ficheros con find

Find es un comando para buscar ficheros en Unix. Find busca y encuentra
ficheros según los valores asociados a una serie de reglas predefinidas
por el. Para tener un conocimiento de todas sus reglas y de los posibles
valores asociados a ellas se recomienda leer su página de manual.

En este breve tutorial se muestra el uso de dos reglas específicas:
-exec y -perm

## Ejecución de comandos a través de find

Permite ejecutar procesos por cada fichero o directorio coincidente con
los patrones de búsqueda indicados. En el primero de los ejemplos
siguientes se ejecutará un `ls -l` por cada fichero bajo el directorio en el que nos encontremos. En el segundo, se ejecutará un cat igualmente, con cada fichero bajo el
directorio en el que estemos situados. **Es importante respetar el espacio tras el comando y terminar el comando con la coletilla `\;`**

```
$ find . -type f -exec ls -l {} \;
$ find . -type f -exec cat {} \;
```

Podemos ejecutar varios comandos, simplemente repitiendo la regla `-exec` y
de esta forma concatenar diferentes ejecuciones por cada coincidencia.

```
$ find . -type f -exec cat {} \; -exec echo "----separador---" \;
```

En el caso de que necesitemos que los comandos ejecutados tras `-exec`
redireccionen sus entradas o salidas, lo mejor para no confundir
sintáxis con la del propio `find` es arrancar con `-exec` una shell sh y
pasarle a ella el comando que queramos ejecutar:

```
$ find . -type f -exec sh -c 'sed s/la/lo/ {} > {}.x' \;
```

## Búsqueda de archivos según sus permisos

Con `find` también podemos realizar búsquedas a partir de unos permisos
dados. Esta regla se denomina `-perm` y tiene una sintáxis propia que
debemos conocer. Tras `-perm` situaremos siempre la combinación de
permisos (en octal o de forma textual) pero estos pueden ir precedidos
de '-', '/' o nada.

-   `-perm mode`: Busca ficheros con esa combinación exacta de permisos.
    Aquí si podemos usar el modo octal sin problemas

-   `-perm -mode`: Busca ficheros que cumplan todas las combinaciones de
    permisos asignadas en mode de forma inclusiva (Y). Por ejemplo:

    -   `-perm -ug+w` : Todos los fichero que permitan 'w' al
        propietario Y al grupo
    -   `-perm -u+rw` : Todos los fichero que permitan al propietario
        'r' Y 'w'
    -   `-perm -+r` : Todos los ficheros que permitan 'r' al
        propietario, al grupo Y a los demás
    -   `-perm -u+r` : Todos los ficheros que permitan 'r' al
        propietario (aquí daría igual usar esta o la siguiente)

-   `-perm /mode`: Busca ficheros que cumplan todas las combinaciones de
    permisos asignadas en mode de forma exclusiva (O). Por ejemplo:

    -   `perm /ug+w`: Todos los fichero que permitan 'w' al propietario
        O al grupo
    -   `perm /u+rw`: Todos los fichero que permitan al propietario 'r'
        O 'w'
    -   `perm /+r`: Todos los ficheros que permitan 'r' al propietario,
        al grupo O a los demás

Nótese que en este último, al usar O, **no tienen porque cumplirse todas
las combinaciones, solo una de ellas.**

## Ejemplos de búsquedas a partir de permisos

A continuación se muestra un ejemplo de uso de find con la regla perm
partiendo de cuatro ficheros con diferentes permisos en un mismo
directorio.

```
$ ls -l
rw-rw-rw  ...  f1
r--rw-r-- ...  f2
---r--rw- ...  f3
r--r--r-- ...  f4

$ find . -perm -ug+w
f1

$ find . -perm -u+rw
f1

$ find . -perm -+r
f4
f1
f2

$ find . -perm -u+r
f4
f1
f2 

$ find . -perm /ug+w
f1
f2

$ find . -perm /u+rw
f4
f1
f2

$ find . -perm /+r
f4
f1
f3
f2
```

---

Octubre 2007
