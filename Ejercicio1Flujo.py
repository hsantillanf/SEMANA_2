class circulo:
    def __init__(self):
        pass

    def superficie_circulo(self):
        radio= float(input("Ingresar el radio del círculo: "))
        superficie= 3.1416*(radio**2)
        print("La superficie del círculo es {}" .format(superficie))

cir=circulo()
cir.superficie_circulo()