def caratula(tarea):
    print("Universidad Nacional Autónoma de México \nFacultad de Estudios Superiores Aragón")
    print("Materia: Estructura de datos \nProfesores:M. en C. Jesús Hernández Cabrera,Ing. Aaron Velascos Agustin")
    print("Alumno: Angel Andrés Hernández Hernández\nTarea: "+tarea+"\n")

class Array:
         def __init__(self, n):
                  self.__data=[]
                  for i in range(n):
                           self.__data.append(None)
         def get_leght(self):#Tamaño del arreglo
                  return len(self.__data)
         def set_item(self, index, value):#Cambia valor en la posicion
                  if index >= 0 and index < len(self.__data):
                           self.__data[index]= value 
                  else:
                           print("Fuera de rango")
         def get_item(self, index):#Elem en posición de index
                  if index >= 0 and index < len(self.__data):
                           return self.__data[index] 
                  else:
                           print("Fuera de rango")
         def clearing(self, valor): #Asina el valor a todo el arreglo.
                  for index in range(len(self.__data)):
                           self.__data[index]=valor
         def to_string(self):#Imprime la cadena
                  print(self.__data)
def main():
    caratula("Arrays")
    arreglo = Array(10)
    print(f"El tamaño es de{arreglo.get_leght()}")
    arreglo.to_string()
    j=1
    for i in range(0,10,1):
        arreglo.set_item(i,j)
        j+=1
    arreglo.to_string()
    arreglo.set_item(12,10)
    print(f"El elemento 1 es {arreglo.get_item(1)}")
    arreglo.get_item(20)
    arreglo.clearing(5)
    arreglo.to_string()
main()
