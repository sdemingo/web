% Autenticación básica de usuarios (I)

- [Inicio](../index.html)

La autenticación de usuarios es un paso básico y primordial en toda aplicación
web y si estamos trabajando fuera del Google App Engine tendremos que montarnos
nosotros mismos el mecanismo. 

Actualmente existen varias librerías en Go que ya permiten solucionar el
problema y que recomiendo si se quiere algo robusto para producción. Si lo que
queremos es aprender algo sobre el tema nada mejor que abordar el asunto desde
un punto de vista artesanal. Para ello me he inspirado (como no) en un [post de
StackOverflow](http://stackoverflow.com/questions/25218903/how-are-people-managing-authentication-in-go/27470944#27470944) donde se trata el tema y se propone un pequeño flujo para
controlar el formulario de entrada y la gestión de la sesión del
usuario. Resumiendo el asunto queda de la siguiente manera:

-   El usuario manda sus credenciales desde un formulario via POST sobre TLS
-   El servidor crea una nueva sesión y la asigna una clave aleatoria que se envía
    al usuario como una cookie. Además esta sesión se añade a una tabla de sesiones abiertas
-   Cada manejador que requiera autenticar al usuario comprueba la cookie en cada petición y recupera la sesión almacenada de la tabla

Hablaré del mecanismo de sesiones sobre cookies en el próximo post. En este voy
a centrarme en conseguir una conexión segura sobre TLS a nuestro servidor
web. Para ello lo primero que necesitamos es un [certificado X.509](https://es.wikipedia.org/wiki/X.509) necesario para
negociar con el cliente los parámetros del cifrado de TLS. Esto lo podemos hacer
fácilmente con el comando `openssl`.

    openssl genrsa -out private_key 2048
    openssl req -new -x509 -key private_key -out public_key -days 365

Una vez hecho esto solo tenemos que sustituir la llamada clásica al método
`http.ListenAndServe` por `http.ListenAndServeTLS` pasándole el puerto donde
escuchamos y las rutas de los ficheros de nuestro certificado. Antes de terminar
he añadido una *goroutine* para redireccionar todo el tráfico que pueda seguir
teniendo sobre el puerto inseguro de HTTP hacia el puerto seguro que escucha en
TLS.

    package main
    
    import (
            "log"
            "net/http"
    )
    
    const (
            TLSPORT    = ":8443"
            PORT       = ":8080"
            PRIV_KEY   = "./private_key"
            PUBLIC_KEY = "./public_key"
            DOMAIN     = "localhost"
    )
    
    func main() {
    
            http.HandleFunc("/", rootHandler)
    
            // Redirect all requests to TLS socket
            go func() {
                    err := http.ListenAndServe(PORT, http.RedirectHandler("https://"+DOMAIN+TLSPORT, http.StatusFound))
                    if err != nil {
                            panic("Error: " + err.Error())
                    }
            }()
    
            // Listen on secure port
            err := http.ListenAndServeTLS(TLSPORT, PUBLIC_KEY, PRIV_KEY, nil)
            if err != nil {
                    panic("Error: " + err.Error())
            }
    }
    
    
    func rootHandler(w http.ResponseWriter, r *http.Request) {
      // do something ...
    }

En el próximo post dentro de unos días hablaré de como implementar el mecanismo
de autenticación de usuarios y la gestión de la sesión de trabajo en el
servidor.


----

Febrero 2016
