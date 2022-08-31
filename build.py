#!/usr/bin/env python3

# Script para reconstruir tanto el blog como la sección de últimas lecturas
# y para actualizar los index tanto de gémini como de la versión web
# 
# Dependencias:
#  - md2gemini: https://pypi.org/project/md2gemini/  (pip3 install md2gemini)
#  - lxml
#  - beautifullsoup4


from string import Template
from datetime import datetime
import os
import sys
import re
from md2gemini import md2gemini
from string import Template
import requests
from bs4 import BeautifulSoup

HOME=os.getenv("HOME")


##
## Variables de ubicación del blog
##
GEM_ROOT=HOME+"/public_gemini"
HTML_ROOT=HOME+"/public_html"
INSTALL_BUILD=HOME+"/web"


##
## Otras variables
##
GEM_BLOG="/blog"
HTML_BLOG="/blog"

POSTS_ROOT=INSTALL_BUILD+"/blog"
POSTS_INDEX=POSTS_ROOT+"/INDEX"

HTML_FILE_BOOKS=HTML_ROOT+"/books.html"
HTML_TEMPLATE_BOOKS=INSTALL_BUILD+"/templates/books-template.html"

GEM_FILE_BOOKS=GEM_ROOT+"/books.gmi"
GEM_TEMPLATE_BOOKS=INSTALL_BUILD+"/templates/books-template.gmi"

GEM_INDEX_FILE=GEM_ROOT+"/index.gmi"
GEM_TEMPLATE_INDEX=INSTALL_BUILD+"/templates/index-template.gmi"

HTML_TEMPLATE_BLOG=INSTALL_BUILD+"/templates/blog-template.html"
GEM_TEMPLATE_BLOG=INSTALL_BUILD+"/templates/blog-template.gmi"



##
##
##  FUNCIONES PARA EL BLOG
##
##

files=[]

def md2gemtext(filename):
  internal_link = '=>(.+)\.md\.html(.+)\.md\.html'
  index_link = '=>.+index.html'
  index_upper_link = '\* Inicio\[\d+\]'
  title_head = '%(.+)'
  date_sign = '\-{3}\n+(\w+ \d{4})'
  month=""

  with open(filename, "r") as f:
    markdown=f.read()

    # Quito y extraigo la firma de la fecha del markdown original:
    matches = re.search(date_sign, markdown, re.MULTILINE)
    if matches!=None:
      month=matches.group(1)
    markdown = re.sub(date_sign,"",markdown, re.MULTILINE)

    gemini = md2gemini(markdown, links="at-end")

    # Saneo gemini para cambiar:
    # - Quito el % del primer título y lo convierto a #
    gemini = re.sub(title_head,"#\g<1>",gemini)

    # - Enlaces a otros artículos del propio blog
    gemini = re.sub(internal_link,"=>\g<1>.md.gmi \g<2>.md.gmi",gemini)

    # - Cambio los enlaces a index
    #gemini = re.sub(index_link,"=> ../index.gmi Inicio",gemini)
    gemini = re.sub(index_link,"",gemini)
    gemini = re.sub(index_upper_link,"",gemini)

    # - Añado al final de los enlaces la firma
    if month!="":
      gemini +="\n\n\n=> ../index.gmi Inicio\n"
      gemini +="\n---\n\n"
      gemini +=month+"\n\n"

  return gemini


def buildPost(post):
  mdfile=post[0]
  date=post[1]
    
  # First extract the title
  pathFile="{dir}/{file}".format(dir=POSTS_ROOT,file=mdfile)
  with open(pathFile) as f:
    lines=f.readlines()

  if (len(lines)==0):
    return
    
  title=lines[0].strip("%")
  if (len(title)==0):
    print ("El fichero "+mdfile+" no tiene título en la primera línea")
    return

  if fileChanged(pathFile,HTML_ROOT+HTML_BLOG+"/"+mdfile+".html"):
    # Build the HTML
    cmd="pandoc -s --css ../estilo.css {dir1}/{file} -o {dir2}/{file}.html".format(
      dir1=POSTS_ROOT,
      file=mdfile,
      dir2=HTML_ROOT+HTML_BLOG)
    print ("Build "+mdfile+".hml")
    os.system(cmd)
        
  if fileChanged(pathFile,GEM_ROOT+GEM_BLOG+"/"+mdfile+".gmi"):
    # Build the Gemtext file
    gem=md2gemtext(pathFile)
    
    with open(GEM_ROOT+GEM_BLOG+"/"+mdfile+".gmi","w") as fg:
      fg.write(gem)
      fg.close()
    print ("Build "+mdfile+".gmi")
    
  # Add to the files info
  files.append((mdfile,title,date))

    
def fileChanged(f1,f2):
  try:
    # Compare mtime
    sf1=os.stat(f1).st_mtime
    sf2=os.stat(f2).st_mtime
    if sf2<sf1:
      return True
    return False
  except:
    return True


def buildHTMLIndexBlog():
  files.reverse()
  postsList=""
  for fileInfo in files:
    dt=datetime.strptime(fileInfo[2],"%d/%m/%Y")
    post="<li><a href={url}.html>{text}</a><p class='date'>({date})</p></li>".format(
      url=fileInfo[0],
      text=fileInfo[1],
      date=localeDate(dt.strftime("%B %Y")))
    postsList+="\n"+post

  with open(HTML_TEMPLATE_BLOG) as t:
    strTmpl=t.read()
    tmpl=Template(strTmpl)
    html=tmpl.substitute(posts=postsList)
      
    with open(HTML_ROOT+HTML_BLOG+"/index.html","w") as o:
      o.write(html)
      o.close()
      print ("Build blog.html")
      

       
def buildGemIndexBlog():

  postsList=""
  for fileInfo in files:
    post="=>{url}.gmi {text}".format(
      url=fileInfo[0],
      text=fileInfo[1])
    postsList+="\n"+post

  with open(GEM_TEMPLATE_BLOG) as t:
    strTmpl=t.read()
    tmpl=Template(strTmpl)
    gmi=tmpl.substitute(posts=postsList)
    
    with open(GEM_ROOT+GEM_BLOG+"/index.html","w") as o:
      o.write(gmi)
      o.close()
      print ("Build blog.gmi")
     
  


        
def getPosts():
  posts=[]
  
  with open(POSTS_INDEX) as f:
    indexLines=f.readlines()

  for line in indexLines:
    fields=re.sub(r'\s+'," ",line).split(" ")
    filename=""
    date=""
    if len(fields)>0:
      date=fields[0].strip("\n")
      filename=fields[1].strip("\n")
    else:
      filename=fields[0].strip("\n")
    if len(filename)>0:
      posts.append([filename,date])
      
  return posts



def buildBlog():
  if not os.path.exists(HTML_ROOT+HTML_BLOG):
    os.makedirs(HTML_ROOT+HTML_BLOG)
        
  if not os.path.exists(GEM_ROOT+GEM_BLOG):
    os.makedirs(GEM_ROOT+GEM_BLOG)

  posts=getPosts()
  for post in posts:
    buildPost(post)

  buildHTMLIndexBlog()
  buildGemIndexBlog()








    
##
##
## FUNCIONES PARA LOS LIBROS
##
##

def getReads(url):
  reads=[]
  result = requests.get(url)
  if (result.status_code == 200):
    soup = BeautifulSoup(result.content,"xml")
    for item in soup.findAll("item"):
      title=item.title.text
      imglink=item.book_medium_image_url.text
      booklink=item.link.text
      author=item.author_name.text
      description=item.book_description.text
      read_at=item.user_read_at.text
      reads.append((title,author,imglink,booklink,description,read_at))
      # Fields:
      # 0:title
      # 1:author
      # 2:link to cover
      # 3:link to the book in goodreads
      # 4:description
      # 5:end reading date
  return reads


def buildTableHTML(reads):
  readsHTML=""
  for r in reads:
    html="""
    <tr>
    <td><img src='{img}'/></td>
    <td class='title'>{title} - <span class='author'>{author}</span></td>
    </tr>
    """.format(author=r[1],title=r[0],img=r[2],desc=r[4])
    readsHTML+=html
  return readsHTML
        

def buildListHTML(reads):
  readsHTML=""
  for r in reads:
    if r[5]!="":
      datef=r[5].split(" ")
      html="<li>{title} - <span class='author'>{author}</span> <span class='bookdate'>({date})</span></li>".format(
        author=r[1],title=r[0],date=" ".join(datef[2:4]))
      readsHTML+=html
  return readsHTML


def buildTableGemText(reads):
  readstext=""
  for r in reads:
    text="* {title} - {author}\n\n".format(author=r[1],title=r[0])
    readstext+=text
  return readstext


def buildListGemText(reads):
  readstext=""
  for r in reads:
    if r[5]!="":
      datef=r[5].split(" ")
      text="* {title} - {author} ({date})\n".format(
        author=r[1],title=r[0],date=" ".join(datef[2:4]))
      readstext+=text
  return readstext


def buildBooks():
  if (not (('currently' in globals()) and ('lasts' in globals()))):
    print ("No goodreads info. Ignore build")
    return
  
  todayDate=datetime.today().strftime("%d/%m/%Y")
  curReads=getReads(currently)
  lastReads=getReads(lasts)
  currTable=buildTableHTML(curReads)
  lastList=buildListHTML(lastReads[:20])
  
  with open(HTML_TEMPLATE_BOOKS) as t:
    strTmpl=t.read()
    tmpl=Template(strTmpl)
    html=tmpl.substitute(current=currTable,lasts=lastList,lastDate=todayDate)

    with open(HTML_FILE_BOOKS,"w") as o:
      o.write(html)
      print ("Build books.gmi")

  currTable=buildTableGemText(curReads)
  lastList=buildListGemText(lastReads[:20])

  with open(GEM_TEMPLATE_BOOKS) as t:
    strTmpl=t.read()
    tmpl=Template(strTmpl)
    html=tmpl.substitute(current=currTable,lasts=lastList,lastDate=todayDate)

    with open(GEM_FILE_BOOKS,"w") as o:
      o.write(html)
      print ("Build books.html")







##
##
## FUNCIONES GENERALES
##
##

months={"January":"Enero",
        "February":"Febrero",
        "March":"Marzo",
        "April":"Abril",
        "May":"Mayo",
        "June":"Junio",
        "July":"Julio",
        "August":"Agosto",
        "September":"Septiembre",
        "October":"Octubre",
        "November":"Noviembre",
        "December":"Diciembre"}
        
def localeDate(dstr):
  for i,j in months.items():
    dstr = dstr.replace(i,j)
  return dstr


def buildGemIndex():
  todayDate=datetime.today().strftime("%d %b %Y").replace("Jan","Ene").replace("Apr","Abr").replace("Dec","Dic")    
  with open(GEM_TEMPLATE_INDEX) as t:
    strTmpl=t.read()
    tmpl=Template(strTmpl)
    html=tmpl.substitute(last=todayDate)

    with open(GEM_INDEX_FILE,"w") as o:
      o.write(html)
      print ("Build index.gmi")

             
def buildHTMLIndex():
  cmd="cp {dir1}/index-template.html {dir2}/index.html".format(
            dir1=INSTALL_BUILD+"/templates",
            dir2=HTML_ROOT)
  print ("Build index.html")
  os.system(cmd)


def buildCSS():
  cmd="cp {dir1}/estilo.css {dir2}".format(
            dir1=INSTALL_BUILD+"/templates",
            dir2=HTML_ROOT)
  print ("Build estilo.css")
  os.system(cmd)
  
  

if __name__=='__main__':

  try:
    from goodreads import currently,lasts
  except Exception as err:
    print ("No goodreads.py module. Books cannot be build")
    
  if len(sys.argv)<2:
    print ("\t\t build.py [ --all | --blog | --books ]")
    sys.exit(0)

  if sys.argv[1]=="--books":
    buildBooks()
    sys.exit(0)

  if sys.argv[1]=="--blog":
    buildBlog()
    buildGemIndex()
    sys.exit(0)
            
  if sys.argv[1]=="--all":
    buildBlog()
    buildBooks()
    buildGemIndex()
    buildHTMLIndex()
    buildCSS()


