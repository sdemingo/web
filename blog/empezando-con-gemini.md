%Empezando con Gemini

- [Inicio](../index.html)


Había oído hablar de este protocolo en algún artículo perdido de reddit hace
unos meses. Pero hasta ahora no me había puesto a indagar y a bucear en su
estructura. Me ha parecido brutal, simplemente. Obviamente recuerda mucho al
olvidado Gopher y en esencia simplifica hasta el extremo, haciendo lo mismo que
hacía HTTP/HTML hace veinte años. Mucho antes de que se convirtiera en el circo
en el que se ha convertido hoy en día la WWW.

Básicamente, Gemini son dos cosas. Por un lado tenemos el
[protocolo](https://gemini.circumlunar.space/docs/specification.gmi) y por otro
un sistema de marcado de documentos,
llamado [gemtext](https://gemini.circumlunar.space/docs/gemtext.gmi) 
que recuerda mucho a Markdown y que permite
documentar sin añadir carga extra a las páginas o documentos servidos por el
servidor.

A la hora de recuperar artículos antiguos escritos en markdown me he encontrado
algunas complicaciones para exportarlos a gemtext. La primera es recomendación
de no usar saltos de línea entre párrafos para partir líneas de forma artificial
y la segunda y mas incómoda es que gemtext no permite enlaces embebidos con el
texto, como HTML o Markdown, sino que estos han de estar situados en una línea
aparte para ellos solos.

Para solventar esto rápidamente os dejo un pequeño script de python que os
ayudará a recuperar todo esos contenidos que pudierais tener en markdown. Una
vez creado el contenido solo teneis que [crearos una cápsula
gemini](https://gemini.circumlunar.space/docs/gemtext.gmi) para servir todos
estos documentos.

Os dejo el sript y espero que os sirva de ayuda:

```
#!/usr/bin/env python

import sys
import re

link_regexp = '\[[^]]+\]\(\s*[^)]+\s*\)'
breaklines_regexp='([^\s]+)\n([^\s]+)'
link_list=[]
link_count=1

if (__name__=="__main__"):
    if (len(sys.argv)<2):
        print ("\tUso: md2gem   fichero.md")
        exit()

    with open(sys.argv[1],"r") as f:
        md=f.read()
        f.close()

    md = re.sub(breaklines_regexp,"\g<1> \g<2>",md)
    for link in re.findall(link_regexp,md):
       url=re.findall("\(\s*[^)]+\s*\)",link)[0].strip("()")
       name=re.findall("\[[^]]+\]",link)[0].strip("[]")
       link_list.append([name,url])

    link_count=1
    link_endlist=""
    for link in link_list:
        md = re.sub("\["+link[0]+"+\]\(\s*"+link[1]+"\s*\)",link[0]+"["+str(link_count)+"]",md)
        link_count+=1
        link_endlist +="=> "+link[1]+"\n"
   
    md += "\n\n"+ link_endlist
    print(md)
```


---

Diciembre 2021
