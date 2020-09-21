import math

print ("***Menú***")
print ("Calculadora")
print ("Elige una opción")
print ("1-Suma")
print ("2-Resta")
print ("3-División")
print ("4-Multiplicación")
print ("5-Raiz")
print ("6-Elevar un numero")
entrada= input("Qué operación quieres realizar, selecciona un numero: ")
operacion= float(entrada)

if (operacion==1):
    primer_numero=input("Primer numero a sumar\n")
    segundo_numero=input("Segundo numero a sumar\n")
    primer_numero_recibido=float(primer_numero)
    segundo_numero_recibido=float(segundo_numero)
    resultado_suma= primer_numero_recibido+segundo_numero_recibido
    print("La suma es: ", resultado_suma)
if (operacion==2):
    primer_numero=input("Primer numero a restar\n")
    segundo_numero=input("Segundo numero a restar\n")
    primer_numero_recibido=float(primer_numero)
    segundo_numero_recibido=float(segundo_numero)
    resultado_resta= primer_numero_recibido-segundo_numero_recibido
    print("La resta es: ", resultado_resta)
if (operacion==3):
    primer_numero=input("Dividendo\n")
    segundo_numero=input("Divisor\n")
    primer_numero_recibido=float(primer_numero)
    segundo_numero_recibido=float(segundo_numero)
    resultado_division= primer_numero_recibido/segundo_numero_recibido
    print("El resultado es: ", resultado_division)
if (operacion==4):
    primer_numero=input("Primer numero a multiplicar\n")
    segundo_numero=input("Segundo numero a multiplicar\n")
    primer_numero_recibido=float(primer_numero)
    segundo_numero_recibido=float(segundo_numero)
    resultado_multiplicacion= primer_numero_recibido*segundo_numero_recibido
    print("La multiplicación es: ", resultado_multiplicacion)
if (operacion==5):
    primer_numero=input("Ingrese el numero al cual desea calcular la raiz cuadrada\n")
    numero_raiz_recibido=float(primer_numero)
    resultado_raiz= math.sqrt(numero_raiz_recibido)
    print("La raiz es: ", resultado_raiz)
if (operacion==6):
    primer_numero=input("Numero a Elevar\n")
    segundo_numero=input("Exponente\n")
    primer_numero_recibido=float(primer_numero)
    segundo_numero_recibido=float(segundo_numero)
    resultado_numero_levado= primer_numero_recibido**segundo_numero_recibido
    print("El resultado es: ", resultado_numero_levado)
else:
    print("El numero que ingresó es invalido")