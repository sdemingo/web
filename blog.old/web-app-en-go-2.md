# Aplicación Web en Go (II)


Continuo con el [tema abierto hace unos días](../posts.html/web-app-en-go-1.md.html) sobre la programación de
aplicaciones web en Go. Hoy muestro un trozo de código que ilustra como he
manejado las sesiones de usuario de mi aplicación usando [el paquete de sesiones
de Gorilla](http://www.gorillatoolkit.org/pkg/sessions). El uso de estas no puede ser más sencillo. En primer lugar creamos
una variable de tipo `sessions.NewCookieStore` para el almacenamiento de las
sesiones en memoria. Tal y como se indica en [documentación de Gorilla](http://www.gorillatoolkit.org/pkg/sessions#NewCookieStore) de las
dos claves solo la primera es la obligatoria y aunque yo las he creado a mano es
recomendable el uso de la función `securecookie.GenerateRandomKey()` para
generarlas.

    // Authorization Key
    var authKey = []byte{
        0x70, 0x23, 0xbd, 0xcb, 0x3a, 0x15, 0x72, 0x48,
        0x46, 0x12, 0x16, 0xfc, 0x81, 0xF1, 0x38, 0xeb,
        0xfc, 0x81, 0xfb, 0xbb, 0x9b, 0xcf, 0x8e, 0x3e,
        0xa9, 0xf5, 0x43, 0x16, 0x54, 0x3d, 0xa1, 0x22,
    }
    
    // Encryption Key
    var encKey = []byte{
        0x31, 0x93, 0x3E, 0x1B, 0x00, 0x67, 0x62, 0x86,
        0xB1, 0x7B, 0x61, 0x01, 0xCA, 0xA8, 0x76, 0x44,
        0x0A, 0xEF, 0x65, 0x11, 0x21, 0x1B, 0x5A, 0x57,
        0x21, 0x72, 0xA1, 0x62, 0x5B, 0x8C, 0xE9, 0xA1,
    }
    
    var store = sessions.NewCookieStore(authKey, encKey)
    
    var sessionName = "appname"

También he implementado una serie de funciones simples para la gestión de las
sesiones: crear nueva, comprobar la validez y cerrar una sesión. Las sesiones
poseen un mapa de valores llamado `Values` indexado por nombres y una estructura
llamada `Options` donde podemos definir características internas de la sesión
como su tiempo de expiración, el ámbito de validez, etc.

    func createSession(w http.ResponseWriter, r *http.Request) 
              (*sessions.Session, bool) {
    
            session, err := store.Get(r, sessionName)
            if err!=nil {
                    log.Println("session error: ", err.Error())
                    return nil, false
            }
            session.Values["isAuthorized"] = true
            session.Options = &sessions.Options{
            Path: "/",      
            MaxAge:60*5}
            
            if err = session.Save(r, w); err != nil {
                    log.Println("session error: ", err.Error())
                    return nil,false
            }
            return session,true
    }
    
    
    func validateSession(w http.ResponseWriter, r *http.Request) 
                (*sessions.Session, bool) {
    
            if session, err := store.Get(r, sessionName); err == nil {
                    if v, ok := session.Values["isAuthorized"]; 
                          ok && v == true {
                            return session,true
                    } else {
                            return nil,false
                    }
            }
    
            return nil,false
    }
    
    
    func closeSession(w http.ResponseWriter, r *http.Request) 
               (*sessions.Session, bool) {
            if session, err := store.Get(r, sessionName); err == nil {
    
                    session.Values["isAuthorized"]=false
                    session.Options = &sessions.Options{
                    MaxAge: -1, 
                    Path: "/"}
                    
                    if err := session.Save(r, w); err != nil {
                            log.Println("saving error: ", err.Error())
                            return nil,false
                    }
    
                    http.SetCookie(w, &http.Cookie{
                    Name: sessionName,
                    MaxAge: -1,
                    Path: "/"})
    
                    return session,true
            }else{
                    log.Print(err)
            }
            return nil,false
    }

La idea es usar estas funciones en nuestros controladores. Las funciones
`createSession` y `closeSession` se pueden usar al implementar el controlador
que gestione los comandos de login y logout de nuestra aplicación. Una vez
implementado la funcionalidad de login, podemos incluir la validación de la
sesión en cada controlador tal y como se muestra en este ejemplo:

    func FooController(w http.ResponseWriter, r *http.Request) {
    
            f:=strings.Split(r.URL.Path,"/")
            cmd:=f[2]
            switch cmd{
            case "bar":
                    barHandler(w,r)
            default:
                    ErrorHandler(w,r,ErrResourceNotFound)
            }
    }
    
    
    func barHandler(w http.ResponseWriter, r *http.Request) {
    
            if _,ok := validateSession(w, r); ok {
                    fmt.Fprint(w,"Your session is ok, yeah!")
            }else{
                    http.Redirect(w, r, "/", http.StatusForbidden) 
            }
    }

Solo quedaría mapear la función principal de este controlador llamada
`FooController` tal y como se mostraba en el [artículo anterior](../posts.html/web-app-en-go-1.md.html) y comprobar su
funcionamiento realizando una petición a `http://localhost:6060/foo/bar`. Como
siempre con Go, fácil y claro. Los próximos artículos los dedicaré a la conexión
con la base de datos y la gestión de vistas usando la librería de plantillas de
Go.


---

Julio 2013
