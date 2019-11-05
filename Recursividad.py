def caratula(tarea):
    print("Universidad Nacional Autónoma de México \nFacultad de Estudios Superiores Aragón")
    print("Materia: Estructura de datos \nProfesores:M. en C. Jesús Hernández Cabrera,Ing. Aaron Velascos Agustin")
    print("Alumno: Angel Andrés Hernández Hernández\nTarea: "+tarea+"\n")
caratula("Recursividad")

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def suma(lista,a):
    if a==len(lista)-1:
        return 0
    else:
        a+=1
        return lista[a]+suma(lista,a)
n=int(input("Ingresa un número"))
print("El factorial de "+str(n)+" es:"+str(factorial(n)))
prueba=[3,5,2,1]
print("La suma de los elementos de la lista"+str(prueba)+" es:"+str(suma(prueba,-1)))
print("----FIN DEL PROGRAMA---")


