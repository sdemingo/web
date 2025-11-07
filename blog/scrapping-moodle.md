# Extrayendo información de Moodle 

Por razones que no vienen al caso, este curso he necesitado recabar información
sobre la estructura interna de un CMS Moodle. Este gestor de contenidos, para quien no lo conozca es muy usado en docencia para la gestión de curso online, aulas virtuales, gestión de calificaciones, etc.  En concreto he necesitado cargar una base de datos con los cursos creados de los profesores de mi centro, los participantes de estos y sus últimos accesos. Esta información es sencilla de obtener si tienes permisos de administración pero no era esta mi situación. Este Moodle no está administrado directamente por mi sino que es gestionado por mi administración autonómica por lo que todo quedaba reducido a solicitar esta información a los administradores o bien obtenerla yo mismo a través de la extracción de los datos usando HTTP. Lo que viene siendo *web scrapping* de toda la vida. 

Hoy en día extraer información usando *scripts* automatizados no es muy difícil siempre y cuando la web en cuestión no ponga obstáculos serios. En mi caso ha sido fácil. Únicamente he necesitado la librería `request` para iniciar y gestionar una sesión autenticada sobre la que ir solicitando recursos HTTP y la librería `BeautifulSoup` para procesar el fichero HTML recibido y extraer de el fácilmente la información que me interesa. Algo a tener en cuenta es la necesidad de no incordiar demasiado al servicio contra el que estás conectado. Levantar gran número de hilos o peticiones simultáneas puede ser fácilmente detectado y terminará con tu dirección IP o tu credencial de usuario bloqueada. 

Como la información no era algo que necesitara tener de forma apremiante, construí mi script para incluir latencias aleatorias de varios segundos entre peticiones y así evitar llamar mucho la atención. También evité tener que ejecutar toda la extracción de una vez y elaboré un mecanismo para poder ir lanzándola a ratos y que esta fuera descargándose en periodos separados durante varios días.

Os dejo una pequeña muestra sobre como crear y manejar una sesión autenticada con la que solicitar las páginas situadas tras el formulario de inicio de sesión.



```
import requests
from bs4 import BeautifulSoup


BASE_URL = "https://url-base-de-tu-servicio-mooodle.org"

CREDENTIALS = {
    "username": "tunombredeusuario",
    "password": "LaContraseña"
}

##
## Autentifico la sesión y obtengo un token
##

session = requests.Session()
login_page = session.get(f"{BASE_URL}/login/index.php")
soup = BeautifulSoup(login_page.text, "html.parser")
token = soup.find("input", {"name": "logintoken"})["value"]

CREDENTIALS["logintoken"]=token

##
## Uso el token para comprobar que estoy autenticado correctamente
##
resp = session.post(f"{BASE_URL}/login/index.php", data=CREDENTIALS)
if not any("MoodleSession" in cookie.name for cookie in session.cookies):
    print("⚠️ No hay cookie de sesión; el login falló.")
    sys.exit()

##
## Pedimos cualquier página de la zona tras el login
##
page = sesion.get(f"{BASE_URL}/course/index.php")
soup = BeautifulSoup(page.text, "html.parser")

select = soup.find("select")
# ...
```


---

Noviembre 2025
