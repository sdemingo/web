% Macros para LaTeX en Emacs

- [Inicio](../index.html)


Este verano he estado experimentando y trabajando con los bufferes en Emacs con
Elisp: borrando y escribiendo texto, moviendo el cursor, seleccionado, etc. Y a
modo de pequeñas prácticas he estado completando algunas funciones útiles para
usar con LaTeX. Realmente no son nada del otro mundo o que no esté hecho ya en
otros famosos modos como [AUCTeX](http://www.gnu.org/software/auctex/), pero la idea era simplemente practicar lo
aprendido. Os dejo aquí algo de todo ese código: dos sencillas funciones para
crear un entorno cualquiera y otra para crear el código a la inserción de una
imagen en un entorno *figure*, estructura que suelo repetir bastante.

    (defun latex-write-environment ()
      (interactive)
      (setq env (read-string "Name of the environment: "))
      (insert (format "\\begin{%s}\n\n\n\\end{%s}\n" env env))
      (search-backward "\n\n"))
    
    
    (defun latex-write-image ()
      (interactive)
      (setq path (read-string "Image path: "))
      (insert "\\begin{figure}\n")
      (insert (format "\\includegraphics[scale=0.5]{%s}\n" path))
      (insert "\\end{figure}\n"))

Repitiendo estas formulas he creado macros para otras estructuras que suelo
utilizar, sobre todo cuando trabajo con *slides* de Beamer para preparar el
material de clase. 

Otra función que escribí esa semana fue relacionada con el borrado de los
ficheros temporales que crea Emacs. De esa manera, no necesito tener siempre un
archivo `makefile` o similar para crear reglas de borrado, simplemente tiro de
la función y listo.

    (setq latex-tmp-files-list
            (list
             ".aux"
             ".log"
             ".bbl"
             ".bbg"
    
    (defun latex-remove-tmp-files()
      (interactive)
      (let ((list latex-tmp-files-list))
        (while list
          (setq ext (car list))
          (dired-delete-file (concat 
                              (file-name-sans-extension 
                               buffer-file-name)
                              ext))
          (setq list (cdr list)))))


---

Septiembre 2013
