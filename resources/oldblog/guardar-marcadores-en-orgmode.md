% Guardando marcadores en Orgmode

- [Inicio](../index.html)


Hace ya algunos años decidí abandonar los servicios de *bookmarks* en Internet
para usar únicamente un fichero en orgmode. Del.icio.us y otros servicios
similares dejaron de convencerme y me limité a guardar enlaces interesantes bien
etiquetados en Emacs.

Con una simple función de almacenado donde pedir interactivamente la url, el
título del enlace y una descripción bastaba. Más tarde la añadí otro campo más
para permitir etiquetar cada enlace y poder hacer búsquedas más rápidas. Dejé
enterrada esta función en mi directorio de configuración hasta que el otro día
decidí rescatarla y hacer que me mostrara una lista con las etiquetas usadas en
todo mi archivo de orgmode para así tener una referencia a la hora de etiquetar
mejor enlaces relacionados con otros que ya tenía guardados anteriormente. Esto
se me ocurrió tras descubrir que la información de todas las etiquetas está en
la variable `org-global-tags-completion-table`.

No me enrollo más y os dejo el código de la función completa por si a alguien
le vale. 

    (defun bookmark-save-orgmode()
      "Añade un enlace como favorito a un fichero en formato org-mode"
      (interactive)
      (setq prefix "http://")
      (setq iurl (read-string "Enlace: "))
      (if (string-prefix-p prefix iurl)
          (setq url iurl)
        (setq url (concat prefix iurl))
        )
    
      (setq tags-list (sort (mapcar 'car (org-global-tags-completion-table)) #'string<))
      (setq sort-tags-list (mapconcat 'identity tags-list "|"))
    
      (setq title (read-string "Título: "))
      (setq desc (read-string "Descripción: "))
      (setq tags (replace-regexp-in-string "[\|.,; ]+" ":" 
                                           (read-string 
                                            (format "Etiquetas \n%s: " sort-tags-list))))
      
      (setq stamp (format-time-string "%Y-%m-%d %a %H:%M"))
      (setq prop (format "<!--\n:CREATED: <%s>\n-->" stamp))
      (if (= (length tags) 0)
          (write-region (format "*** [[%s][%s]]\n%s\n%s\n" url title prop desc) 
                        nil bookmark-orgmode-file 'append)
        
        (write-region (format "*** [[%s][%s]] \t\t\t:%s:\n%s\n%s\n" url title tags prop desc) 
                      nil bookmark-orgmode-file 'append)
        )
      )


---

Marzo 2017
