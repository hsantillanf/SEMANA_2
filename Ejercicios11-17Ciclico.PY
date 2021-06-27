class eciclico():
    def __init__(self):
        pass

    # Ejercicio11 Suma de los cuadrados
    def ejer11(self):
        i=1
        sum=0
        for i in range(100):
	        sum= sum + i*i
        print("El total de la suma es:{}".format(sum))

    # Ejercicio12 Escribir los números del 1 al 100
    def ejer12(self):
        i=0
        while i <= 100:
            i+=1
            print("Presentación de los números:{}".format(i))

    # Ejercicio13 Suma y productos de N numeros enteros(usuarios)
    def ejer13(self):
        n="si"
        sum=0
        pro=1
        while n!="no":
	        num=int(input("ingrese un numero: "))
	        sum+=num
	        pro=pro*num
	        n=input("desea continuar si/no: ")
	        n=n.lower()
        print("La suma es:{} y el producto es:{}".format(sum,pro))

    # Ejercicio14 suma y productos de N numeros entreros (centinela)
    def ejer14(self):
        sum = 0
        product = 1
        numer = 0
        numer = int(input("Ingrese un número: "))
        while (numer != -1):
            sum = sum + numer
            product = product * numer
            numer = int(input("Ingresa un número: "))
        print("Total de la suma es:{}, Total del producto es:{}" .format(sum,product))

    # Ejercicio15 Determinar si el numero es primo
    def ejer15(self):
        primo =  True
        divisor = 2
        numero =  int ( input ( "Ingrese un número:" ))
        while  divisor < numero  &  primo == True :
            res =  numero % divisor
            if  res == 0 :
                primo =  False
            divisor += 1
        if  primo ==  True :
            print ( "El número {} es primo" . formato ( numero ))
        else:
            print ( "El número {} no es primo" . formato ( numero ))

    # Ejercicio16 Leer un N° entero  y calcular la serie
    def ejer16(self):
        i = 1
        serie = 0
        num =  int ( input ( "Ingrese un número:" ))
        band = True
        while  band:
            if  band  == True:
                serie =  serie + ( 1 / i )
                band =  False
            else:
                serie =  serie - ( 1 / i )
                band =  True
            i += 1
            if i > num :
                break
            print ( "El resultado de la serie es: {}" . formato ( serie ))

    # Ejercicio17 Calcular el factorial
    def ejer17(self):                          
        num =  int ( input ( "Ingrese un número:" ))
        fact = 1
        for  i  in  range ( 1 , num + 1 ):
            fact *= i
        print ( "El factorial del número {} es: {}" . formato ( num , fact ))
    
cic= eciclico()
cic.ejer11()
cic.ejer12()
cic.ejer13()
cic.ejer14()
cic.ejer15()
cic.ejer16()
cic.ejer17()
