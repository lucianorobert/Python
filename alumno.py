#PROGRAMACION SECUENCIAL
# nombre = input("Nombre: ")
# especialidad = input("Especialidad: ")
# print(f"Hola {nombre} de la especialidad de {especialidad}")



# #PROGRAMACION FUNCIONAL
# def main():
#     nombre = getNombre()
#     especialidad = getEspecialidad()
#     print(f"Hola {nombre} de la especialidad de {especialidad}")

# def getNombre():
#     return input("Nombre: ")

# def getEspecialidad():
#     return input("Especialidad: ")

# if __name__ == "__main__":
#     main()




# #PROGRAMACION FUNCIONAL USANDO TUPLAS
# def main():
#     nombre, especialidad = getAlumno() #TUPLAS
#     print(f"Hola {nombre} de la especialidad de {especialidad}")

# def getAlumno():
#     nombre = input("Nombre: ")
#     especialidad = input("Especialidad: ")
#     return nombre, especialidad #TUPLAS - INMUTABLE o puedo escribirlo (nombre, especialidad)

# if __name__ == "__main__":
#     main()

# Listas son Mutables




# #PROGRAMACION FUNCIONAL USANDO TUPLAS - Un mejor codigo
# def main():
#     alumno = getAlumno() #TUPLAS
#     print(f"Hola {alumno[0]} de la especialidad de {alumno[1]}")

# def getAlumno():
#     nombre = input("Nombre: ")
#     especialidad = input("Especialidad: ")
#     return (nombre, especialidad) #TUPLAS - INMUTABLE o puedo escribirlo (nombre, especialidad)

# if __name__ == "__main__":
#     main()



# #PROGRAMACION FUNCIONAL USANDO TUPLAS - Un mejor codigo - Probando inmutabilidad funcione
# def main():
#     alumno = getAlumno() #TUPLAS
#     if alumno[0] == "Maria":
#         alumno[1] = "Sistemas Computacionales"

#     print(f"Hola {alumno[0]} de la especialidad de {alumno[1]}")

# def getAlumno():
#     nombre = input("Nombre: ")
#     especialidad = input("Especialidad: ")
#     return (nombre, especialidad) #TUPLAS - INMUTABLE o puedo escribirlo (nombre, especialidad)

# if __name__ == "__main__":
#     main()





# #PROGRAMACION FUNCIONAL USANDO LIST - permite Mutar - cambiar el valor de las veriables
# def main():
#     alumno = getAlumno() 
#     if alumno[0] == "Maria":
#         alumno[1] = "Sistemas Computacionales"
        
#     print(f"Hola {alumno[0]} de la especialidad de {alumno[1]}")

# def getAlumno():
#     nombre = input("Nombre: ")
#     especialidad = input("Especialidad: ")
#     return [nombre, especialidad] #LIST - MUTABLE 

# if __name__ == "__main__":
#     main()


# DICCIONARIOS
# #Que pasa si tenemos mas de dos variables, se complica tener en mente el numero de indeces y a que 
# #variables corresponden. Un mejor diseno de codigo es utilizar DICCIONARIOS, donde es posible 
# # utilizar una llave o key asociado con un valor o value
# def main():
#     alumno = getAlumno() #TUPLAS
#     print(f"Hola {alumno['nombre']} de la especialidad de {alumno['especialidad']}")

# def getAlumno():
#     alumno = {}
#     alumno["nombre"] = input("Nombre: ")
#     alumno["especialidad"] = input("Especialidad: ")
#     return alumno

# if __name__ == "__main__":
#     main()



# #Que pasa si tenemos mas de dos variables, se complica tener en mente el numero de indeces y a que 
# #variables corresponden. Un mejor diseno de codigo es utilizar DICCIONARIOS (Mutables), donde es posible 
# # utilizar una llave o key asociado con un valor o value
# def main():
#     alumno = getAlumno() 
#     if (alumno['nombre'] == "Maria"):
#         alumno['especialidad'] = "Sistemas Computacionales"
#     print(f"Hola {alumno['nombre']} de la especialidad de {alumno['especialidad']}")

# def getAlumno():
#     # alumno = {}
#     # alumno["nombre"] = input("Nombre: ")
#     # alumno["especialidad"] = input("Especialidad: ")
#     nombre = input("Nombre: ")
#     especialidad = input("Especialidad: ")
#     return {"nombre" : nombre, "especialidad" : especialidad}

# if __name__ == "__main__":
#     main()



# class

# Hasta ahora hemos utilizado tipos de datos creados por los creadores de Python
# Los creadores de Python no pueden antiipar todos los tipos de datos que podemos utizar. Sin embargo,
# podemos crear nuestro propio tipo de datos mediante clases. Una clase es un prototipo, un plano, un molde 
# que nos permite crear objetos. Un objeto es una instancia de una clase.
 
# class Alumno:
#     ...

# def main():
#     alumno = getAlumno() 
   
#     print(f"Hola {alumno.nombre} de la especialidad de {alumno.especialidad}")

# def getAlumno():
#     alumno = Alumno()
#     alumno.nombre = input("Nombre: ")
#     alumno.especialidad = input("Especialidad: ")
#     return alumno

# if __name__ == "__main__":
#     main()

# Una vez que utilizamos la clase, creamos un objeto, acabamos de inventar un nuevo tipo de dato. Clase es un plano, plantilla o un molde. La definicion 
# de un nuevo tipo de dato. Objeto es una instancia de la clase: alumno = Alumno(). Atributos son las variables dependientes de la clase



# Para utilizar todo el poder de clases y objetos. Con clases podemos realizar software mas complejos, definir errores, asegurar que el codigo
# sea correcto
# class Alumno:
#     def __init__(self, nombre, especialidad):  #funcion que inicializa el contenido del objeto, es diferencte al constructor
#         self.nombre = nombre #self.n
#         self.especialidad = especialidad #self.e

# def main():
#     alumno = getAlumno() 
#     print(f"Hola {alumno.nombre} estas inscrito en la especialidad {alumno.especialidad}")

# def getAlumno():
#     nombre = input("Nombre: ")
#     especialidad = input("Especialidad: ")
#     # alumno = Alumno(nombre, especialidad) #Constructor
#     # return alumno
#     return Alumno(nombre, especialidad)

# if __name__ == "__main__":
#     main()



# VALIDACION DE ERRORES
# Que pasa si el usuario no introduce el nombre o escribe alguna especialidad desconocida
# Encapsulamiento: El objetivo de POO es que todo este contenido en la definicion de las clases, las operaciones bien podrian escribirse
# en otra funcion fuera de la clase. Sin embargo, la metodologia es que debe estan encapsulado en la definicion de la clase.

# class Alumno:
#     def __init__(self, nombre, especialidad):  #funcion que inicializa el contenido del objeto, es diferencte al constructor
#         if not nombre: # if nombre = "" print("Error ") //o sys.exit("Introduzca el nombre") # Termina el programa
#             raise ValueError("Introduzca el nombre")
#         if especialidad not in ['Sistemas', 'Quimica', 'Bioquimica', 'Mecatronica']:
#             raise ValueError("La especialidad no esta registrada en este centro de estudios")
#         self.nombre = nombre #self.n
#         self.especialidad = especialidad #self.e

# def main():
#     alumno = getAlumno() 
#     print(f"Hola {alumno.nombre} estas inscrito en la especialidad {alumno.especialidad}")

# def getAlumno():
#     nombre = input("Nombre: ")
#     especialidad = input("Especialidad: ")
#     return Alumno(nombre, especialidad)
#     # try
#         # return Alumno(nombre, especialidad)
#     # except Value:
#     #     ... Permite al programador manejar el error

# if __name__ == "__main__":
#     main()



# FUNCION STR TAMBIEN DEFINIDO DENTRO DE LA ClasE
class Alumno:
    def __init__(self, nombre, especialidad):  #funcion que inicializa el contenido del objeto, es diferencte al constructor
        if not nombre: # if nombre = "" print("Error ") //o sys.exit("Introduzca el nombre") # Termina el programa
            raise ValueError("Introduzca el nombre")
        if especialidad not in ['Sistemas', 'Quimica', 'Bioquimica', 'Mecatronica']:
            raise ValueError("La especialidad no esta registrada en este centro de estudios")
        self.nombre = nombre #self.n
        self.especialidad = especialidad #self.e

    # Imprime el objeto en texto(as string)
    def __str__(self):
        return f"{self.nombre} esta inscrito en {self.especialidad}"

def main():
    alumno = getAlumno() 
    print(alumno) # imprime la direccion del objeto alumno

def getAlumno():
    nombre = input("Nombre: ")
    especialidad = input("Especialidad: ")
    return Alumno(nombre, especialidad)
    # try
        # return Alumno(nombre, especialidad)
    # except Value:
    #     ... Permite al programador manejar el error

if __name__ == "__main__":
    main()