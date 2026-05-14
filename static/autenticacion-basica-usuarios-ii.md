# Autenticación básica de usuarios (II)


Hace unos días publiqué un post sobre [como realizar una conexión segura en un
servidor web en Go](../posts.html/autenticacion-basica-usuarios-i.md.html). La idea final es autenticar usuarios de forma segura tal y
como voy a terminar de explicar en este artículo.

Una vez tenemos un canal seguro hacia el servidor lo que tenemos que hacer ahora
es crear un sistema de sesiones para detectar que peticiones HTTP provienen de
un usuario que ya ha sido autenticado y cuales no. En la comunidad de Go existen
varios frameworks que tienen ya construidos sistemas de sesiones y es posible
que el más usado a día de hoy sea el que está contenido en [Gorilla](http://www.gorillatoolkit.org/), un *toolkit*
que implementa en varios paquetes la principal funcionalidad que necesita
cualquier aplicación web para empezar a funcionar de forma más o menos seria.
Por mi parte únicamente quiero construir un sistema sencillo que ni siquiera voy
a soportar sobre un almacenamiento persistente. La idea es sencilla y la [tenéis
desarrollada por completo en este gist](https://gist.github.com/sdemingo/79d5b6651b728badbe46). 

Inicialmente partimos de una estructura para la sesión de trabajo del usuario:

    type Session struct {
            Key       string
            User      *User
            LoginTime time.Time
            LastTime  time.Time
    }

En esta sesión se almacenan, además de la propia clave de sesión de la que ahora
hablaremos, el usuario al que pertenece y el momento en que la usó por última
vez. Este último valor nos es útil para poder ir [borrando en un *goroutine*
aparte las sesiones que consideramos caducadas](https://gist.github.com/sdemingo/79d5b6651b728badbe46#file-sessions-go-L30) porque el usuario no las cerró
correctamente.

Cuando un usuario se conecte por primera vez y se compruebe sus credenciales
(nombre de usuario y contraseña) en la base de datos, sistema de ficheros,
&#x2026; se generará una nueva sesión con una clave aleatoria. Usaremos esta clave
además para indexar esa nueva sesión en un mapa.

    func randKey() string {
            b := make([]byte, 8)
            rand.Read(b)
            return fmt.Sprintf("%x", b)
    }
    
    func NewSession(u *User) *Session {
            key := randKey()
            s := &Session{key, u, time.Now(), time.Now()}
            sessionTable[key] = s
            return s
    }

Este clave de sesión será [enviada al cliente en forma de cookie](https://gist.github.com/sdemingo/79d5b6651b728badbe46#file-server-go-L74) para que la
rebote en todas sus peticiones siguientes. Cada petición hacia el servidor que
contenga un token de sesión entre sus cookies será aceptada. Se comprobará que
este token conduce a una sesión válida o en caso contrario se reconducirá al
cliente al formulario de login.

    func welcome(w http.ResponseWriter, r *http.Request) {
            _, err := GetSession(r)
            if err != nil {
                    Exit(w, r)
                    return
            }
    
            tmpl := template.Must(template.ParseFiles("welcome.html"))
            if err := tmpl.Execute(w, nil); err != nil {
                    log.Printf("%v", err)
                    return
            }
    }

Al no tener soporte persistente para este mecanismo de sesiones, cualquier
reinicio del servicio eliminaría las sesiones, expulsando a cualquier usuario
que estuviera trabajando en ese momento en nuestra aplicación. 

Para terminar, una característica que podríamos implementar sería la posibilidad
de recuperar la clave de sesión bien de las cookies del navegador o quizás
usando la librería `localStorage` de almacenamiento local soportada por HTML5 y
evitar así que el usuario tuviera que abrir una nueva sesión cada vez que abra
el navegador e intente entrar en nuestra aplicación.


---

Marzo 2016
