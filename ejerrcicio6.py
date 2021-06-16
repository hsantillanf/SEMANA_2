
class ciclofor:
    def __init__(self):
        pass
    
    def usofor(self):
        datos=["carlos",25,True]
        numeros=(2,5.6,4,2)
        docente={"nombre":"TONNY","edad":50,"fac":"faci"}
        listnotas=[(20,20),(40,30),(50,20)]
        listalunmos=[{"nombre":'erick',"final":90},{"nombre":'juan',"final":20},{"nombre":'ronny',"final":30}]

        for i in range(5):
            print("i={}".format(i))
        for i in range(2,10):
            print("i={}".format(i))
        for i in range(4,10,2):
            print("i={}".format(i),end="   ") 
        
        longitud=len(datos)
        for i in range(longitud):
            print("for",datos[i],end=' ')
        
        l=0
        while l<longitud:
            print("while",datos[l])
            l=l+1
        
        for i in range(longitud-1,0,-1):
            print("for",datos[i])

        for i,info in enumerate(datos):
            print("for",i,info)
        for info in numeros:
            print(info)
        for info in ['t','o','m','g','f','p','a']:
            print(info)
        
        print("\ndiccionario de notas")
        
        for clave,valor in docente.items():
            print(clave,":",valor,docente)
        
        for alumnos in listalunmos:
            for clave,valor in docente.items():
              print(clave,":",valor,end="  ")



objeto=ciclofor()
objeto.usofor()

