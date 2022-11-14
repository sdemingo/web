
# Instalación de Minix


## 1. Introducción


Este documento describe el proceso de instalación del sistema operativo
minix 2.0 en una partición dedicada. La maquina sobre la que se realizo
la instalación fue un viejo 486 SX 33Mhz con 170 Mgbytes de HD. Como
veis una bonita forma de reciclar el ordenador del abuelo.Vamos además a
tener un DOS instalado en otra partición, porque nunca se sabe cuando se
va a necesitar.

## 2. Primeros Pasos


Lo primero que necesitamos son 9 disquetes en blanco. En ellos
grabaremos las imágenes de los archivos necesarios para arrancar la
instalación. Usaremos *fdvol* incluido en el CD de Minix.

```
fdvol 1440 A: Boot\ROOT Boot\USR 
```

y lo mismo para los otros 8 disquetes. El programa te ira pidiendo los
sucesivos disquetes a medida que los va llenando.

```
fdvol 1440 A: Base\USR.TAZ fdvol 1440 A: Source\SYS.TAZ fdvol 1440 A: Source\CMD.TAZ 
```

`USR.TAZ` contiene algunos comandos básicos (3 discos), `SYS.TAZ` los
fuentes del sistema (2 discos) y `CMD.TAZ` los fuentes de esos comandos
básicos (3 discos).

A continuación debemos preparar las particiones para alojar los dos
sistemas. En mi caso comencé la desde cero con mi HD. Usando un
disco de arranque de DOS y el *fdisk* de DOS destruí la única partición
que había en el disco duro, donde se alojaba el DOS. Tras eso hemos
reinstalado DOS en una partición de 20 MB, situada al comienzo del
disco, seguida de dos particiones, una de 100 MB y otra que ocupa el
disco restante. De esta forma tengo una primera partición de 20 MB con
DOS y en los 100 MB siguientes instalare MINIX. La configuración última
de las particiones en tu disco es algo muy personal y no afecta al
funcionamiento de minix.

**Nota:** El uso de fdisk no es complicado y a pesar de estar en formato
ascii sus menús resultan muy intuitivos, para mas ayuda en el manejo de
fdisk visitar <http://www.vtr.net/~lfuenza/FDISK.htm>.

## 3. Instalación


Usaremos el disquete de booteo anteriormente generado. Tras rearrancar
el ordenador con este disco en la disquetera, presenciaremos el proceso
de carga de minix. Pulsamos el signo `=` en el monitor para comenzar
con dicho proceso. Se generara un disco virtual en el disquete para
contener el sistema de ficheros raíz. Ahora debemos indicar donde se
encuentra el sistema de ficheros con los comandos. Esta situado en el
disco de booteo aunque debemos indicarle el slice correspondiente,
`/dev/fd0c`. Tras esta operación deberíamos tener algo parecido esto en
nuestro monitor.

```
Minix 2.0.0  Copyright 1997 Prentice-Hall, Inc.

Executing in 32-bit protected mode Memory size = 8010K MINIX = 295K RAM disk = 480K Available = 7236K

RAM disk loaded.

Tue Oct  1 16:21:37 MET 1996 
Finish the name of device to mount as /usr: /dev/fd0c 
/dev/fd0c is read-write mounted on /usr 
Starting standard daemons: update. 
Login as root and run 'setup' to install Minix.

Minix Release 2.0 Version 0
noname login:
```

Una vez se ha montado el sistema de ficheros `/usr` y se han levantado los daemons, aparecera el indicador de login.
Ingresaremos como root para comenzar con la instalación.

```
noname login: root 
# setup

This is the Minix installation script.

Note 1: If the screen blanks suddenly then hit F3 to select "software
scrolling". 
..... 
..... 
Note 5: If you see a colon (:) then you should hit RETURN to continue. :
```

Hay dos caminos para la satisfactoria instalación de minix, la instalación
manual mas larga y compleja y la automatica, que recomendamos a los iniciados en
minix y de la que trata este documento. Para iniciar la instalación automática
debemos de teclear el comando `setup` en el prompt que nos ha aparecido tras
ingresar como root en el sistema.  (ilustrado en la captura anterior).


### Configuracion del teclado

El primer paso de la instalación sera seleccionar el tipo de teclado que
queremos tener, por defecto tenemos seleccionado el `US standard`.

```
What type of keyboard do you have?  You can choose one of:

french  italian   latin-am  scandinavn  uk      us-swap
german  japanese  olivetti  spanish     us-std

Keyboard type? [us-std]
```


### Creación de particiones

El siguiente paso es el más critico de la instalación. Usaremos el editor de
tabla de particiones que incorpora minix, **part**. Con las teclas `+` y `-`
elegimos el dispositivo que queremos particionar. En mi caso solo tengo un disco
duro así que selecciono /dev/hd0. Ahora veras que el dispositivo ha sido
seleccionado pero no aparece información sobre el, tan solo un montón de
interrogaciones. Esto es porque debemos leer la tabla de particiones de dicho
dispositivo, lo haremos pulsando `r`. Part debería mostrar la información de tu
disco de una manera similar a la de la imagen.


```
Select device       ----first----  --geom/last--  ------sectors-----
    Device             Cyl Head Sec   Cyl Head Sec      Base      Size       Kb
    /dev/hd0                          485   16  63
                         0    0   0   488   15  62         0    492912   174080
Num Sort   Type
 1  hd1  12              0    1   0     4   15  62        63      4977    20488
 2  hd2  00 None         0    0   0     0    0  -1         0         0        0
 3  hd3  00 None         0    0   0     0    0  -1         0         0        0

at-hd0: Conner Peripherals 170MB - CP2251
```

La nueva partición donde ira alojado minix se deberá crear en el espacio
denominado NONE (ya que en el otro tenemos instalado DOS). Es recomendable que
la partición de minix no supere los 128 MB (las versiones mas modernas soportan
particiones de hasta 1 GB) y no sea menor de 30 MB. Para crear la partición de
minix nos situamos en la zona no asignada que nos interese (en mi caso *hd2*) y
la cambiamos el tipo a MINIX. Hecho esto solo nos queda salir y salvar los
cambios, pulsamos `q` confirmamos la reescritura de la tabla de particiones del
disco.

Ahora el instalador nos preguntara el nombre de la partición creada (en mi caso
`/dev/hd2`). Tras esto se crean en dicha partición dos subparticiones, una de
1440 KB para el sistema de fichero raíz y el resto para el `/usr`.


``` 
Size in sectors     ----first----  --geom/last--  ------sectors-----
    Device             Cyl Head Sec   Cyl Head Sec      Base      Size       Kb
    /dev/hd0                          485   16  63
                         0    0   0   488   15  62         0    492912   174080
Num Sort   Type
 1  hd1  12              0    1   0     4   15  62        63      4977    20488
 2* hd2  81 MINIX        5    0   0   426   14  52      5040    425303   102400
 3  hd3  00 None         0    0   0     0    0  -1         0         0        0

Save partition table? (y/n) y

Please finish the name of the primary partition you have created:
(Just type RETURN if you want to rerun "part")                   /dev/hd2

You have created a partition named:     /dev/hd2
The following subpartitions are about to be created on /dev/hd2:

        Root subpartition:      /dev/hd2a       1440 kb
        /usr subpartition:      /dev/hd2c       rest of hd2

Hit return if everything looks fine, or hit DEL to bail out if you want to
think it over.  The next step will destroy /dev/hd2.
```

Con el disco ya preparado solo queda llenar los filesystems con los contenidos
de los discos de booteo generados al comienzo de la instalación. Y con esto
llegamos a la ultima cuestión de la instalación, la asignación de cache, para
maquinas con mas de 4 MB de de RAM bastara con pulsar intro (en caso de memoria
inferior hay que indicárselo al instalador).  Insertamos el disco etiquetado
como ROOT y salimos del sistema con el comando `halt`.

## 4. Configuración


Ya hemos instalado minix, ahora debemos instalar tambien los comandos y las
fuentes del sistema. Rearrancamos la maquina con el disco `ROOT` en la
disquetera, booteamos la particion de minix (hd2) e ingresamos como
root. Tecleamos `setup /usr` para instalar lo anterior. Usaremos primero los
discos de `USR.TAZ`, luego `SYS.TAZ` y por ultimo los `CMD.TAZ`, para cada grupo
de discos usaremos el anterior comando.

```
fd0>boot hd3

Minix 2.0.0  Copyright 1997 Prentice-Hall, Inc.

Executing in 32-bit protected mode
.....
.....
Minix  Release 2.0 Version 0

noname login: root
# setup /usr

What is the size of the images on the diskettes? [all]
What floppy drive to use? [0]
Please insert input volume 1 and hit return

created directory: local/lib
created directory: local/man
created directory: local/src
......
......
```

Nuestro sistema minix ya esta instalado y es plenamente funcional, tan
solo nos queda darle un nombre a nuestra maquina usando el comando
`echo` Donde *nombre* es el nombre de nuestra maquina.


```
# echo nombre >/etc/hostname.file
```

Para bootear automaticamente minix pasados unos segundos del arranque de
la maquina basta con escribir en el monitor:
`main(){ trap 5000 minix;menu}`, sin olvidar que la partición de minix
debe de estar marcada como partición activa. Igualmente para añadir
opciones al menu del monitor, como por ejemplo el booteo de la particion
de DOS al inicio se debe introducir la siguiente secuencia de comandos
en el monitor.

```
name(d,Boot DOS){ boot hd1}
save
```

Minix es un sistema con escasa utilidad practica pero con el que sin
duda puedes aprender infinidad de cosas. Es la mejor herramienta con la
que empezar a introducirte en los sistemas UNIX de una forma fácil y
simple. Espero que este documento te haya servido para aclararte esas
primeras dudas sobre minix y su instalación. Buena suerte.

## 5. Enlaces

Pagina oficial, del A.S.Tanembaum autor de minix:<http://www.cs.vu.nl/~ast/minix.html>



---

Noviembre 2001
