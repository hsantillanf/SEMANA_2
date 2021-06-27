class esecuenciales:
    def __init__(self):
        pass

    def  ejer2(self):                    
        totalC =  float ( input ( "Ingrese el total de la compra:" ))
        Dscto =  totalC * 0.15
        ValorP =  totalC - Dscto
        print ( "El total de la compra es {}, su valor a pagar es {}" . formato ( totalC , ValorP ))

    def ejer3(self):
        sueldob=float(input("Ingresar el valor del sueldo:  "))
        venta1=float(input("Ingresar el valor de la primera venta: "))
        venta2=float(input("Ingresar el valor de la segunda venta: "))
        venta3=float(input("Ingresar el valor de la tercera venta: "))
        totalv=(venta1+venta2+venta3)
        comision=totalv*0.1
        Total=sueldob+comision
        print("Su sueldo final es de:${}, total de sueldo recibido:${} ".format(sueldob,Total))

secuen= esecuenciales()
secuen.ejer2()
secuen.ejer3()        
