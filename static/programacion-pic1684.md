
# Programación de un PIC16F84

Años antes de que el primer Arduino viera la luz del día ya había gente trasteando con pequeños microcontroladores. Os dejo por aquí un pequeño código que he encontrado rebuscando en el baúl donde se programa un dado electrónico usando un pequeño microcontrolador [PIC16F84](https://es.wikipedia.org/wiki/PIC16F84). 

Mientras conectamos un display de 7 segmentos al `PORTB` y lo usamos como salida, conectamos a `PORTA` un botón físico que será el que detenga el dado. Como los microcontroladores son deterministas, generar un número puramente aleatorio es difícil. El programa utiliza el tiempo humano para esta labor. Mientras mantienes pulsado el botón, el registro `AUX2` incrementa a una velocidad de microsegundos del 1 al 6. Como es imposible que un humano suelte el botón exactamente en el mismo microsegundo cada vez, el número que queda en `AUX2` cuando sueltas el botón parece totalmente aleatorio.

Aquí tenéis el código completo aunque hace tanto tiempo que no toco uno de estos que no sería capaz de encontrar ningún error en caso de haberlo.


```
        LIST    P=16F84
        RADIX   HEX
; definicion de las constantes a usar en el programa
W       EQU     0
F       EQU     1
UNO     EQU     06
DOS     EQU     5B
TRES    EQU     4F
CUATRO  EQU     66
CINCO   EQU     6D
SEIS    EQU     7D

; declaracion de los registros
TMROPT  EQU     0x01
; ###### de generacion del numero aleatorio ######
PC      EQU     0x02
Z       EQU     0x02
ESTADO  EQU     0x03
PUERTAA EQU     0x05
PUERTAB EQU     0x06
INTCON  EQU     0x0B
VECES   EQU     0x10
AUX     EQU     0x0E


; ###### de generacion del numero aleatorio ######
AUX2    EQU     0x15
DISP    EQU     0x12
        ORG     0
        goto    inicio
        ORG     4
        goto    inter
        ORG     5

; para empezar inicializamos los 'registros'con los valores correspondientes
inicio  bsf     ESTADO,5
        clrf    PUERTAB
        movlw   b'00000001'     
        movwf   PUERTAA
        movlw   b'00000110'
        movwf   TMROPT
	    bcf	    ESTADO,5
     	movlw	b'10100000'
    	movwf	INTCON                       
; ###### de generacion del numero aleatorio ######
        MOVLW   0x01
        MOVWF   AUX2
        movlw   0X64
        movwf   VECES
        movlw   0xB2
        movwf   TMROPT
; ###### de generacion del numero aleatorio ######
bucle   btfsc   PUERTAA,0
        goto    bucle

; ###### de generacion del numero aleatorio ######
        call    RANDOM
        call    DISPLAY
        movwf   PUERTAB
        movlw   b'10100000'     
        movwf   INTCON
        goto    bucle
; codigo de la interrupcion
inter   btfsc   PUERTAA,0
        goto    inter_
        movlw   b'10100000'
        movwf   INTCON
        movlw   0xB2
        movwf   TMROPT
        retfie
inter_  decfsz  VECES,1
        goto    salir
reinic  movlw   0x64
        movwf   VECES
; en este momento ha pasado un segundo asi que empezamos a
; mostrsr los numero del uno al seis por el display con un
; peque¤o retardo (dos bucles anidados de ff instrucciones)
nums    movlw   0x01
        movwf   AUX
; ********* mostramos el valor 1 **********
        movf    AUX,W
        call    Display1
        movwf   PUERTAB
        movlw   0xff
        movwf   DISP


bucle1  btfsc   PUERTAA,0
        goto    b_1
        movlw   b'10100000'
        movwf   INTCON
        movlw   0xB2
        movwf   TMROPT
        retfie
b_1     decfsz  DISP,1
        goto    bucle1
; metemos un segundo bucle para mostrar el valor un mayor tiempo
        movlw   0xff
        movwf   DISP            
bucle1_ btfsc   PUERTAA,0
        goto    b__1
        movlw   b'10100000'
        movwf   INTCON
        movlw   0xB2
        movwf   TMROPT
        retfie
b__1    decfsz  DISP,1
        goto    bucle1_
; ********* mostramos el valor 2 **********
        incf    AUX,F
        movf    AUX,W
        call    Display2
        movwf   PUERTAB
        movlw   0xff
        movwf   DISP
bucle2  btfsc   PUERTAA,0
        goto    b_2
        movlw   b'10100000'
        movwf   INTCON
        movlw   0xB2
        movwf   TMROPT
        retfie
b_2     decfsz  DISP,1
        goto    bucle2
; metemos un segundo bucle para mostrar el valor un mayor tiempo
        movlw   0xff
        movwf   DISP            
bucle2_ btfsc   PUERTAA,0
        goto    b__2
        movlw   b'10100000'
        movwf   INTCON
        movlw   0xB2
        movwf   TMROPT
        retfie
b__2    decfsz  DISP,1
        goto    bucle2_
; ********* mostramos el valor 3 **********
        incf    AUX,F
        movf    AUX,W
        call    Display3
        movwf   PUERTAB
        movlw   0xff
        movwf   DISP
bucle3  btfsc   PUERTAA,0
        goto    b_3
        movlw   b'10100000'
        movwf   INTCON
        movlw   0xB2
        movwf   TMROPT
        retfie
b_3     decfsz  DISP,1
        goto    bucle3
; metemos un segundo bucle para mostrar el valor un mayor tiempo
        movlw   0xff
        movwf   DISP            
bucle3_ btfsc   PUERTAA,0
        goto    b__3
        movlw   b'10100000'
        movwf   INTCON
        movlw   0xB2
        movwf   TMROPT
        retfie
b__3    decfsz  DISP,1
        goto    bucle3_
; ********* mostramos el valor 4 **********
        incf    AUX,F
        movf    AUX,W
        call    Display4
        movwf   PUERTAB
        movlw   0xff
        movwf   DISP
bucle4  btfsc   PUERTAA,0
        goto    b_4
        movlw   b'10100000'
        movwf   INTCON
        movlw   0xB2
        movwf   TMROPT
        retfie
b_4     decfsz  DISP,1
        goto    bucle4
; metemos un segundo bucle para mostrar el valor un mayor tiempo
        movlw   0xff
        movwf   DISP            
bucle4_ btfsc   PUERTAA,0
        goto    b__4
        movlw   b'10100000'
        movwf   INTCON
        movlw   0xB2
        movwf   TMROPT
        retfie

b__4    decfsz  DISP,1
        goto    bucle4_
; ********* mostramos el valor 5 **********
        incf    AUX,F
        movf    AUX,W
        call    Display5
        movwf   PUERTAB
        movlw   0xff
        movwf   DISP
bucle5  btfsc   PUERTAA,0
        goto    b_5
        movlw   b'10100000'
        movwf   INTCON
        movlw   0xB2
        movwf   TMROPT
        retfie
b_5     decfsz  DISP,1
        goto    bucle5
; metemos un segundo bucle para mostrar el valor un mayor tiempo
        movlw   0xff
        movwf   DISP            
bucle5_ btfsc   PUERTAA,0
        goto    b__5
        movlw   b'10100000'
        movwf   INTCON
        movlw   0xB2
        movwf   TMROPT
        retfie
b__5    decfsz  DISP,1
        goto    bucle5_
; ********* mostramos el valor 6 **********
        incf    AUX,F
        movf    AUX,W
        call    Display6
        movwf   PUERTAB
        movlw   0xff
        movwf   DISP
bucle6  btfsc   PUERTAA,0
        goto    b_6
        movlw   b'10100000'
        movwf   INTCON
        movlw   0xB2
        movwf   TMROPT
        retfie
b_6     decfsz  DISP,1
        goto    bucle6
; metemos un segundo bucle para mostrar el valor un mayor tiempo
        movlw   0xff
        movwf   DISP            
bucle6_ btfsc   PUERTAA,0
        goto    b__6
        movlw   b'10100000'
        movwf   INTCON
        movlw   0xB2
        movwf   TMROPT
        retfie
b__6    decfsz  DISP,1
        goto    bucle6_
; una vez mostrados todos los numero del 1 al 6 repetimos la operacion
        goto    nums
salir   movlw   b'10100000'

  	    movwf	INTCON
        movlw   0xB2
        movwf   TMROPT
	    retfie

; rutinas que nos dan el valor de los numeros en su "modo" display
Display1  retlw   UNO
Display2  retlw   DOS
Display3  retlw   TRES
Display4  retlw   CUATRO
Display5  retlw   CINCO
Display6  retlw   SEIS

; ###### de generacion del numero aleatorio ######
; rutina para generar el numero "aleatorio" (realmente es pseudoaleatorio)
; pues en el caso de que pulsaramos 2 veces el boton al mismo tiempo
; durante exactamente el mismo tiempo nos daria el mismo numero
; cuando en un algoritmo real de generacion de numero aleatorios esto
; seria realmente complicado
RANDOM  movlw   b'00000000'
        movwf   INTCON
RANDOM2 btfsc   PUERTAA,0
        goto    salirR
        movlw   b'00000110'
        subwf   AUX2,W
        btfsc   ESTADO,Z
        clrf    AUX2
        incf    AUX2,F
        goto    RANDOM2
salirR  movf    AUX2,W
        return

; ###### de generacion del numero aleatorio ######
; rutina que nos da el valor del "codigo" 7 segmentos para cada valor
; del dado
DISPLAY addwf   PC,F
        nop
        retlw   UNO
        retlw   DOS
        retlw   TRES
        retlw   CUATRO
        retlw   CINCO
        retlw   SEIS
        end

```

---

Abril 2003
