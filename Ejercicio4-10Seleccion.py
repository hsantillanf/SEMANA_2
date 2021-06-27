class eseleccion():
    def __init__():
        pass

    # Ejercicio4 Construir un algoritmo 
    def ejer4(self):
       nota=float(input("Ingrese su nota o calificación: "))
       if nota>=7:
            print(" Su calificacion es:{} APROBADO ".format(nota) ) 

    #Ejercicio5 Calificación de un alumno en su examen
    def ejer5(self):
        notaexa=float(input("Ingrese la nota de su examen: "))
        if notaexa>=7 :
	        print(" Su calificación es:{} APROBADO " .format(notaexa))
        else:
            print("sucalificación es:{} REPROBADO" .format(notaexa))

    # Ejercicio6 Sueldo de un empleado
    def ejer6(self):
        sueldo=float(input("Ingrese el sueldo: "))
        if sueldo <600:
            print("Usted recibira un aumento en el sueldo por lo tanto ganara:{} $".format((sueldo*0.10)+sueldo))
        else:
            print("Su sueldo total es:{}".format(sueldo))

    # Ejercicio7 Horas extras     
    def ejer7(self):
        htrabajads=int(input("Ingrese las horas trabajadas "))
        valorhora=float(input("Ingrese el valor por hora "))
        if htrabajads>40:
            hextras=htrabajads-40
            if hextras > 8:
                hextrast=hextras-8
                paghorasextra=(valorhora*2*8)+(valorhora*3*hextrast)
            else:
                paghorasextra=valorhora*2*hextras
            total=valorhora*40+paghorasextra
        else:
            total=valorhora*htrabajads
        print ("El pago total por las horas trabajadas es {}".format(total))

     # Ejercicio8 Leer 3 numeros enteros
    def ejer8(self):
        num1,num2,num3=0,0,0
        num1=int(input("Ingrese el numero1: "))
        num2=int(input("Ingrese el numero2: "))
        num3=int(input("Ingrese el numero3: "))
        if (num1>num2>num3):
            print(num1)
        elif (num2>num1>num3):
            print(num2)
        else:
            print(num3)

     # Ejercicio9 Diseñar un algoritmo (2variables tipo entero)
    def ejer9(self):
        numer, v = 0, 0
        numer = int(input("Ingrese un número como opción: "))
        v = float(input("Ingrese cualquier número que desee: "))

        if (numer == 1):
            resp = 100 * v
        elif (numer == 2):
            resp = 100 ** v
        elif (numer == 3):
            resp = 100 / v
        else:
            resp = 0
        print('Resultado:', resp)

    # Ejercicio10 Operador lógico AND
    def ejer10(self):
        nota1= int(input("Ingrese su primera calificación: "))
        nota2= int(input("Ingrese su segunda calificación: "))
        if  nota1>=80 and nota2>=80:
            print("La calificacion 1: {},la calificación 2:{} es ACEPTADO" .format(nota1,nota2))
        else:
            print("La calificacion 1: {},la calificación 2:{} es RECHAZADO" .format(nota1,nota2))

sel=eseleccion()
sel.ejer4()
sel.ejer5()
sel.ejer6()
sel.ejer7()
sel.ejer8()
sel.ejer9()
sel.ejer10()