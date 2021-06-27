class arreglos():
    def __init__(self):
        pass

    # Ejercicio18 
    def ejer18(self):
        notas = []
        for i in range(10):
            datonuev = int( input( "Escribe el dato  {}: ".format(i)))
            notas.append(datonuev)
        print("Las calificaciones son: {}".format(notas))

    # Ejercicio19 Leer un vector de 20 numeros enteros
    def ejer19(self):
        nuevo,a,b  = [],[],[]
        print ( nuevo )
        for  j  in  range ( 0 , 20 ):
            num  =  int ( input ( "Ingrese un número:" ))
            nuevo.append ( num )
        for  j  in  nuevo :
            if  j  >= 0:
                b.append ( j )
            else:
                a.append ( j )
        print ( "Los números positivos (+) son: {}" . formato ( b ))
        print ( "Los números negativos (-)son: {}" . formato ( a ))

    # Ejercicio20 Calificaciones de 6 examenes
    def ejer20(self):
        notas_list = []
        estudiantes_list = []
        estudiante = 30
        Casilleros_nt = 6
        promedio_examenes = []       
        for estudiante in range(1, 31):
            """30 alumnos"""
            estudiante_temporal = input("Nombre del estudiante {}: ".format(estudiante))
            estudiantes_list.append(estudiante_temporal)
        for nt in range(1, 7):
            print('Escriba la calificación del alumno "{}" en el exámen "{}"'.format(estudiante_temporal, nota))
            """Lectura de las 6 notas de los 30 alumnos"""
            notas_temporal = round(float(input('Nota #{}: '.format(nt))), 2)
            if nt == 1:
                notas_list.append([notas_temporal])
            else:
                notas_list[estudiante-1].append(notas_temporal)
            print("")
        
            """Promedio de calificaciones de c/u de los exámenes"""
            for numero_examen in range(6):
                sumas_notas = 0
                for nota in notas_list:
                    sumas_notas += nota[numero_examen]
                prom = round((sumas_notas/estudiante), 2)
                print('Promedio de exámen {}: {}'.format(numero_examen+1, prom))
        
            """Promedio de cada alumno."""
            print("")
            for numero, alumno in enumerate(estudiantes_list):
                sumas_notas = sum(notas_list[numero])
                prom = round((sumas_notas/Casilleros_nt), 2)
                print("{} su promedio es: {}".format(alumno, prom))
            
            """Tipo de exámen que tuvo mayor promedio de nota."""
            prom_may = 0
            for numero_examen in range(6):
                sumas_notas = 0
                for nota in notas_list:
                    sumas_notas += nota[numero_examen]
                prom = round((sumas_notas/estudiante), 2)
                if prom_may < prom:
                    prom_may = prom
                promedio_examenes.append(prom)
            print("")
            print("El exámen", promedio_examenes.index(prom_may)+1,"obtuvo el promedio mayor :", prom_may)


arr=arreglos()
arr.ejer18()
arr.ejer19()
arr.ejer20()