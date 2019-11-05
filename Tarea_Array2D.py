
def caratula(tarea):
    print("Universidad Nacional Autónoma de México \nFacultad de Estudios Superiores Aragón")
    print("Materia: Estructura de datos \nProfesores:M. en C. Jesús Hernández Cabrera,Ing. Aaron Velascos Agustin")
    print("Alumno: Angel Andrés Hernández Hernández\nTarea: "+tarea+"\n")
class Array2D:
    def __init__(self,rows,cols):
        self.__data=[]
        self.__row=rows
        self.__col=cols
        for row in range(rows):
            tmp=[]
            for col in range(cols):
                tmp.append(None)
                self.__data.append(tmp)
    def to_string(self): #Imprime los valores dentro del Arrays.
        print(self.__data)
    def get_num_rows(self):#Regresa el numero de filas.
        return self.__row
    def get_num_cols(self):#Regresa el número de columnas.
        return self.__col
    def clearing(self, value):#Remplaza todos los valores de la cadena.
        for row in range(self.__row):
            for col in range(self.__col):
                self.__data[row][col]=value
    def set_item(self,r,c,valor):#Agrega o reemplaza un valor en la posición indicada.
        if (r>=0 and r<=self.__row) and (c>=0 and c<=self.__col):
            self.__data[r][c]=valor
def main ():
    caratula("Arrays 2D")
    arreglo=Array2D(3,3)
    arreglo.to_string()
    print(f"numero de renglones {arreglo.get_num_rows()}")
    print(f"numero de columnas {arreglo.get_num_cols()}")
    arreglo.clearing(1)
    arreglo.to_string()
main()
