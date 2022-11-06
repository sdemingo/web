# Emacs como lector de feeds



Mi relación con el editor Emacs ha sido larga. Y, tal vez por eso, ha pasado por
varias fases. Conocí Emacs a través de su fork XEmacs hace más de veinte años y
aunque mi primera impresión fue de indiferencia, le dí una oportunidad al Emacs
original algún tiempo más tarde, año 2002 o así. Poco a poco vas aprendiendo a
configurar el sistema y algo de elisp y acabas entrando en una espiral en la que
no sales de Emacs para nada: correo, navegación, ssh, programación, etc. Y
terminé bastante quemado, la verdad. Sobre el año 2014. Tenía unos ficheros de
configuración monstruosos con decenas de módulos de terceros que actualizaba
manualmente porque en ese momento no usaba sistemas de gestión de paquetes. Ni
siquiera se si existían o no por aquel entonces.

Fuí dejando a Emacs de lado y probando otras alternativas hasta que terminé
usando el *archi*-conocido Visual Studio Code durante un tiempo. Hace unos tres
años aproximadamente comencé a utilizar servidores remotos y a trabajar en
entorno de consola durante mucho tiempo y fue entonces cuando desempolvé al
viejo Emacs. Afinando mucho la configuración e instalando módulos con cabeza,
ayudándome del sistema de paquetería, ahora he conseguido un *setting* mucho más
amigable y robusto del sistema. Tengo un editor potentísimo que uso en cualquier
sistema, sobre bash o ksh de igual manera.

Uno de los usos a los que ahora dedico mi Emacs, además de para editar o
pogramar es la lectura de blogs a través de ficheros RSS. Gracias al módulo
[elfeed](https://github.com/skeeto/elfeed) puedo tener instalado configurado un
Emacs en mi servidor principal, mi feed de blogs y conectarme a el desde
cualquier lugar (incluido mi móvil Android). Os dejo por aquí los principales
aspectos de la configuración de elfeed.

Lo primero es configurar tu lista de feeds:

```
(setq elfeed-feeds
    '(
     ("http://blogdeprueba.com/feed/" etiqueta1)
     ("http://blogdeprueba2.com/feed/" etiqueta1)
     ; ...
     ))
```

Para la lectura cómoda tanto en un monitor grande como en una pequeña pantalla
de móvil lo más importante para mi ha sido poder modificar cómodamente el
autowrapeo de las líneas. En pantallas grandes quiero que estas se trunquen a 80
columnas para evitar largas líneas, pero en pantallas pequeñas justo al
revés. Quiero que estas se corten cuando toque. Esto lo que conseguido con la
siguiente función:

```
(defun eww-toogle-fill-line()
  (interactive)
  (if shr-width                                    
      (progn
        (setq shr-width nil)
        (message "fill lines activated")
        )
    (progn
      (setq shr-width 80)
      (message "fill lines disabled. Truncated at 80 cars"))))

```

Ahora solo enlazo esta función con la tecla `.` para cambiar entre ambos
modos. Así que pulsando `.`  luego la tecla `g` para refrescar, el contenido se
adapta perfectamente a las dimensiones de la pantalla.

```
(with-eval-after-load "elfeed-show"
  (define-key elfeed-show-mode-map "." 'eww-toogle-fill-line))

(with-eval-after-load "eww"
  (define-key eww-mode-map "." 'eww-toogle-fill-line))
```

Para terminar configuro algo de margen izquierdo al contenido y así evitar que se
me pegue al borde de la pantalla. En monitores grandes esto es indiferente pero
en la pantalla del móvil este efecto me generaba muchas molestias.

```
(add-hook 'eww-after-render-hook
          (lambda ()
            (set-window-margins nil 2)))
```

Con estos pequeños ajustes puedo leer mis feeds en mi Emacs cómodamente en
cualquier lugar.  Espero que os haya sido de ayuda.




---

Noviembre 2022
