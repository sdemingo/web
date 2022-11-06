# Configurando el Tabbar Mode


La última receta para Emacs en la que he estado trabajado ha sido la
configuración de las pestañas superiores o *tabs*. A pesar de que algunos
usuarios señalan que entorpecen bastante el trabajo y es preferible utilizar los
buffers y la lista de buffers, me gustaba la idea de tener en la parte superior
un puntero a cada buffer archivo. Pero lo que realmente me atraía más era la
posibilidad que ofrece el modo `tabbar` para agrupar pestañas en base a
criterios personalizables. 

Una vez instalado el paquete, lo primero ha sido crear esta simple función de
agrupamiento basándome en la que se aporta por defecto. La modificación
principal que he realizo ha sido incluir una nueva agrupación para los bufferes
de tipo `org-mode`.

    (defun my-tabbar-buffer-groups ()
      (list (cond ((string-equal "*" (substring (buffer-name) 0 1)) "emacs")
                  ((eq major-mode 'dired-mode) "emacs")
                  ((eq major-mode 'org-mode) "org")
                  (t "user"))))
    
    (setq tabbar-buffer-groups-function 'my-tabbar-buffer-groups)

Configurado esto solo nos quedaría preparar un buen aspecto para las pestañas. A
continuación os muestro mi configuración de colore para las pestañas activas,
modificadas, etc.

    (setq tabbar-background-color "grey25") ;; the color of the tabbar background
    
    (custom-set-faces
     '(tabbar-default ((t (:inherit variable-pitch :background "grey25" :foreground "grey80" 
                                    :weight normal :height 1.5 ))))
     '(tabbar-button ((t (:inherit tabbar-default :foreground "grey25" ))))
     '(tabbar-button-highlight ((t (:inherit tabbar-default))))
     '(tabbar-highlight ((t (:underline t))))
     '(tabbar-selected ((t (:inherit tabbar-default :background "grey40" :weight normal))))
     '(tabbar-separator ((t (:inherit tabbar-default :background "grey25" ))))
     '(tabbar-unselected ((t (:inherit tabbar-default))))
     )

Para terminar algo que me costó sacar mientras buceaba en Google fue como
configurar el relleno interno o *padding* de cada pestaña, para que su texto no
ocupara la totalidad de la pestaña. Os muestro la variable a modificar para
conseguir este efecto:

    (custom-set-variables
     '(tabbar-separator (quote (2))))

Podéis consultar la configuración total del paquete en mi [github para Emacs](https://github.com/sdemingo/my-lisp/blob/master/tabbar-config.el).


---

Noviembre 2015
