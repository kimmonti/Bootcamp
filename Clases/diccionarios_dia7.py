## Diccionarios
# Estructura de datos y un tipo de dato en Python que nos permite
# almacenar informacion con una clasificacion que nos permita ubicarla
# sin necesidad de saber su ubicación solo con una clave
## Estan compuestos por clave : (valor, variable o lista)
## La clave debe estar siempre entre ""

#Ejemplo estructura normal de una lista
lista_info = ["Kim", 24,"Ing. Ambiental", "ciclismo", "español, inglés y japones"]

diccionario_vacio = {}
#Estructura de un diccionario
nombre_diccionario = {"clave_diccionario":"valor de la clave"}
persona = {"nombre":"Kim","edad":24,"profesion":"Ing. Ambiental"}

hobbies = ["ciclismo", "bailar", "dibujar", "nadar", "escalar"]
idiomas = ["español", "ingles", "japonés"]

persona = {
    "nombre":"Kim",
    "edad":24,
    "profesion":"Ing. Ambiental",
    "hobbies":hobbies,
    "idiomas":idiomas
    }

print(persona)
#Para acceder a un valor ponemos el nombre del diccionario y entre[]
#la clave
print(persona["nombre"]) #Imprime solo el valor del nombre
print(persona["hobbies"][2]) #Imprime el valor 2 en la lista de la clave hobbie

# Para cambiar el valor ponemos el nombre del dic, entre[] la clave 
# y asignamos con =
persona[3] = "programadora" #Cambio el valor de la clave profesion
print(persona)