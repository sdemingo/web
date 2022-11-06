# Emacs como editor para Python


Siempre que he programado Python he usado Emacs como entorno de desarrollo pero
esta es la primera vez que he configurado el autocompletado para programar "como
Dios manda" (según algunos). Una vez configurado y listo le sigo sin ver tanta
utilidad a esta característica, aunque seguro que es problema mio. El caso es
que, si queremos un autocompletado "inteligente" y no simplemente el basado en
diccionarios propio del modo [autocomplete](http://www.emacswiki.org/emacs/AutoComplete) necesitamos algo como [Jedi](https://github.com/davidhalter/jedi). Para
configurar este modo utilicé la documentación del propio sitio junto con [este
otro blog](http://www.alandmoore.com/blog/2013/07/31/python-code-completion-in-emacs-at-last/). 

Este modo tiene varias dependencias incluidas varias librerías de Python por lo
que su instalación no es tan limpia como otros, más autocontenidos. Intentaré
resumir aquí los pasos necesarios. Partimos de los siguientes prerrequisitos:

-   Emacs 24.3 (aunque yo lo tengo funcionando en la versión 23.4).
-   Repositorio [Marmalade](http://marmalade-repo.org/) de paquetes Emacs configurado y funcionando.
-   Tener instalado virtualenv para Python.

## Paso 1: Instalamos Jedi

Instala emacs-jedi con todas sus dependencias usando Marmalade. Visualizamos la
lista de paquetes con `M-x package-list-packages` lo buscamos y lo marcamos para
instalar.

Realmente hemos instalado el modulo de Emacs que usa Jedi pero no tenemos el
propio Jedi, pues este es una librería de Python general y usada por muchos
editores. Esto debemos hacerlo manualmente. Antes hemos de asegurarnos que
nuestro sistema cuenta con la librería `virtualenv` de Python. Para terminar de
instalar a mano estas dependencias debemos ir al directorio donde hayamos
instalado emacs-jedi, normalmente bajo el directorio `~/.emacs.d/elpa/jedi-X.X.X` y
ejecutar allí:

    $ make requirements
    $ pip install -r requirements.txt

## Paso 2: Configurar ficheros de emacs

Con todo lo anterior terminado, debemos primeramente asegurarnos que tanto Jedi
como todos sus dependencias se encuentran en nuestro `load-path`. Os pego la
configuración que yo incluí en mi Emacs para terminar de rematar la faena:

    (autoload 'jedi:setup "jedi" nil t) 
    
    (require 'jedi)
    (add-hook 'python-mode-hook 'jedi:setup)
    (setq jedi:server-command (list "python3" jedi:server-script))
    (jedi-mode 1)
    (setq jedi:complete-on-dot t)

Con todo esto terminado solo falta abrir un fichero Python vacío probar con algo
sencillo. Importad un módulo y luego usarlo para comprobar que se os abre el
popup con la información de métodos disponibles.

## Importante

Algo que a mi se me olvidó y me hizo perder un buen rato de trasteo fue la
configuración de la variable PYTHONPATH correctamente. Esta variable ha de estar
definida "dentro de Emacs", así que o bien la capturamos de alguna manera de
nuestro sistema o bien usamos `setenv`. De cualquier manera debe contener,
además del resto de rutas, la ruta donde hayamos instalado el módulo de jedi
para Emacs, en mi caso: `~/.emacs.d/elpa/jedi-X.X.X`


---

Diciembre 2013
