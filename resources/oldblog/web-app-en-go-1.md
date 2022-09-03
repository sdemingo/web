% Aplicación Web en Go (I)

- [Inicio](../index.html)


Llevo unos días tirando código de una pequeña *webapp* para ir familiarizándome
con Go en este campo y me he dado cuenta de que realmente es en este entorno
donde se aprecia la potencia de este lenguaje en sencillez y claridad de
código. En un principio tras unas búsquedas por listas y foros me sorprendió la
ausencia de un framework potente aunque asumí que siendo Go un lenguaje aún en
fase de implantación, carecía de masa crítica para sostener algo de la dimensión
de Django, Rails o Grails. Encontré [Gorilla](http://www.gorillatoolkit.org/), que más que un framework MVC como
son los anteriores es un *toolkit* con varios paquetes que podemos incorporar a
nuestro proyecto. También descubrí [Revel](http://robfig.github.io/revel/), otro proyecto que si se asemeja más a
los mundialmente conocidos frameworks ya mencionados. Aún así, después de darle
algunas vueltas he llegado a pensar que puede que sea innecesario el uso de un
framework de este tipo. Por supuesto, no tengo entre mis manos una gran
aplicación en producción con la que poder opinar pero creo que Go aporta un
código de claridad y suficientemente compacto como para que sea fácilmente
mantenible sin necesidad de estas capas superiores. 

Para ir ubicándome en este campo empecé a organizar mi aplicación en
directorios, inspirado en el (simplemente genial) tutorial oficial de la gente
de Go para el [desarrollo de una pequeña wiki en Go](http://golang.org/doc/articles/wiki/). Mi idea ha sido desarrollar
tres directorios-paquetes: controladores, modelo y vistas. En el primero irían
los ficheros Go con los Handlers que tratarían las peticiones HTTP, descritas en
el paquete [net/http](http://golang.org/pkg/net/http). El directorio de vistas estaría formado por las templates
(ver la documentación del paquete [html/templates](http://golang.org/pkg/html/template/)) para generar el HTML de forma
cómoda y homogénea. Por último en el paquete del modelo están los ficheros con
las estructuras que dan lugar a cada entidad del modelo y sus métodos de acceso
a la base de datos.

    +-web_app/
     +-main.go
     +-controller/
      +-core.go
      +-users.go
      +- ...
    
     +-view/
      +-users/
       +-show.tmpl
       +-edit.tmpl
       +- ...
    
     +-model/
      +-user.go
      +- ...

<div class="center">
Organización del código fuente
</div>

Para el **mapeado de los controladores** usamos el propio fichero `main.go`
ubicado en la raíz del código fuente. Las dos primeras líneas de la función main
indican al servicio web que reenvíe todas las peticiones dirigidas a la raíz, a
la función `ctl.RootHandler` escrita en el fichero `controllers/core.go`. La
segunda línea hace lo propio pero reenviando toda petición realizada a `/core` o
a cualquier recurso bajo esta a la función `ctl.CoreController` también escrita
en este mismo fichero y que muestro un poco más abajo. Usaremos esta misma
fórmula para mapear cualquier otro controlador que necesite nuestra aplicación.

Es interesante tener un lugar donde servir recursos de forma estática (CSS,
imágenes, javascript, etc.). Para esto usamos la función `http.Handle` y
levantamos un servidor de ficheros sobre el directorio `/var/myapp/resources` y
lo enganchamos a un manejador al que redirigimos todas las peticiones bajo
`/resources`.

Por último, levantamos nuestro servicio HTTP en el puerto 6060. ¿Más fácil?
imposible ;-)

    func main(){
    
            http.HandleFunc("/", ctl.RootHandler)
            http.HandleFunc("/core/", ctl.CoreController)
            http.HandleFunc("/user/", ctl.UserController)
            //resto de controladores
    
            http.Handle("/resources/", 
                        http.StripPrefix("/resources/",
                        http.FileServer(http.Dir("/var/myapp/resources"))))
    
            http.ListenAndServe(":6060", nil)
    }

Para terminar os muestro como ejemplo la **función principal del controlador**
llamada `CoreController` implementada en el archivo `controller/core.go`. Cada
controlador tiene una función principal que recibe las peticiones y que es
mapeada en el archivo `main.go`, como ya he explicado antes. En esta función
simplemente corto la URL de la petición para detectar el siguiente elemento y
así lanzar una de las dos funcionalidades implementadas en este controlador:
login y logout. Las funciones que las implementan toman como parámetros el
`http.ResponseWriter` en el que escribiremos los bytes de la respuesta y la
`http.Request` en el que el servicio de Go nos ha dejado la petición del cliente
y de la que aún podemos extraer más información.

    func CoreController(w http.ResponseWriter, r *http.Request) {
            
            cmd:=r.URL.Path[6:]
            switch cmd{
            case "login":
                    loginHandler(w,r)
            case "logout":
                    logoutHandler(w,r)
            default:
                    ErrorHandler(w,r,ErrResourceNotFound)
            }
    }

Para no hacer esto más largo, dejo para próximos artículos el uso de sesiones
basado en la [librería de sesiones de Gorilla](http://www.gorillatoolkit.org/pkg/sessions), la implementación de los modelos y
la visualización de las templates. Siento no enlazar más código pero lo que
tengo ahora no esta en un estado como para presumir, así que prefiero seguir
dándole algunas vueltas más. Espero que al menos, os sirva para haceros una idea
de como organizar una pequeña aplicación web en Go.


--- 

Julio 2013
