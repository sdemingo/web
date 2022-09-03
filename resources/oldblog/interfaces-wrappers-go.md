% Interfaces y wrappers en Go

- [Inicio](../index.html)



Este mes he seguido trasteando con Google App Engine y me gustaría enseñaros un pequeño
wrapper que he realizado para poder almacenar cualquier tipo de objeto sobre el
Datastore que ofrece la plataforma. 

El Datastore de GAE es una base de datos NoSQL orientada a pares de
clave-valor. Esto puede resultar un poco desconcertante para alguien
acostumbrado a un entorno relacional pero rápidamente se le pilla el
tranquillo. La [interfaz es muy sencilla y está muy bien documentada](https://cloud.google.com/appengine/docs/go/datastore/reference). Tenemos
métodos `Put` y `Get` que reciben estructuras e identificadores y realizan la
escritura o pueblan el puntero recibido con lo leído de la base de datos. Además
tenemos objetos `Query` para realizar consultas sobre datos de lo que no sabemos
su identificador y si otras propiedades. 

Incluir estos métodos dentro de los ficheros donde implementamos el modelo de
datos supone acoplar totalmente nuestros modelos con la capa de
persistencia. Obviamente esta es una práctica que debemos evitar, teniendo ambas
capas perfectamente desacopladas por si en un futuro queremos migrar nuestros
modelos a otro servicio de almacenamiento. 

En Go no tenemos tipos genéricos. Para conseguir que varios métodos tomen
diferentes tipos de objetos tenemos que homogeneizar todos estos a través de las
*interfaces*. Una interfaz no es mas que un conjunto de métodos que el objeto
que quiera implementarla debe a su vez declarar. Algo que me gusta de estas
interfaces de Go es que su uso no se declara de forma explícita en el objeto en
cuestión. Si una interfaz declara dos métodos llamados `A()` y `B()` cualquier
objeto que posea dos métodos con esa cabecera ya la implementa. Esto permite
adaptar interfaces propias a objetos definidos en paquetes de terceros sobre los
cuales no tenemos control. 

En mi caso he creado una primera interfaz llamada `DataItem` que permite
declarar métodos para retornar y actualizar un identificador numérico de un
item.

    type DataItem interface {
            ID() int64
            SetID(id int64)
    }

Ahora basta con implementar los métodos que envuelven al `Put` y al `Get` del
Datastore y que a su vez reciben objetos que implementan esta interfaz. El
método `Put` además actualiza el valor de la clave sobre el objeto recién escrito.

    func (op *DataConn) Put(obj DataItem) error {
    
            var key *datastore.Key
            c := op.Wreq.C
    
            if id := obj.ID(); id > 0 {
                    key = datastore.NewKey(c, op.Entity, "", obj.ID(), nil)
            } else {
                    key = datastore.NewIncompleteKey(c, op.Entity, nil)
            }
    
            key, err := datastore.Put(c, key, obj)
            obj.SetID(key.IntID())
    
            return err
    }
    
    
    func (op *DataConn) Get(item DataItem) error {
            c := op.Wreq.C
            key := datastore.NewKey(c, op.Entity, "", item.ID(), nil)
            err := datastore.Get(c, key, item)
            item.SetID(key.IntID())
            return err
    }

Otra operación que necesito *wrappear* es la consulta de varios registros en
base a filtros. Aquí se presenta otro problema: cuando Datastore recupera varios
registros a través de sus filtros, las claves de estos registros deben de
poblarse con posterioridad tal y como explican en este [hilo de
StackOverflow](http://stackoverflow.com/a/9960436). Una primera aproximación nos puede animar que nuestro método de
consulta reciba un array a interfaces de tipo `DataItem` y tras recuperarlas
poblemos sus identificadores. El problema es que el método `GetAll` recibe a su
vez un solo objeto y no un array de objetos. Esto lo he solucionado creado un
nuevo tipo de interfaz llamada `BufferItems` que se declarará sobre arrays
principalmente y que ofrece métodos para navegar por ella y actualizar sus
valores.

    type BufferItems interface {
            At(i int) DataItem
            Set(i int, d DataItem)
            Len() int
    }

Ahora solo falta implementar tipos concretos sobre arrays de objetos de nuestro
modelo que implementen esta interfaz. Para ubicaros mejor con todo lo explicado
recomiendo que estudiéis el [wrapper completo que tengo en GitHub](https://github.com/sdemingo/chex/blob/master/appengine/data/data.go). Antes de
terminar indicaros que he intentado evitar a toda costa la reflexión de tipos
implementada en el [paquete reflect](https://golang.org/pkg/reflect/) de Go. Utilizar *type assertions* en el
wrapper o un switch de tipos tampoco me parecía útil porque implicaba conocer de
antemano los tipos usados en la capa de modelo y quería aislar lo más posible el
almacenamiento de la capa superior. Es posible que haya mejores soluciones no se
me han ocurrido &#x2026; aún ;-)


---

Diciembre 2015
