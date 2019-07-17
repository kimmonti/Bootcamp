# EJ 1. Hacer una clase que se llame vehiculo que tenga tres atributos
# uno que sea cantidad_ruedas, y un metodo que sea definir_tipo_vehiculo
# que me diga si es "Bicicleta, triciclo, auto" de acuerdo a la cantidad de ruedas.
""" 
class Vehiculo:
    
    def __init__(self):
        print ("Has creado un vehiculo")
    
    def cantidad_ruedas(self, num_ruedas):
        self.my_num_ruedas = num_ruedas
          print ("El movil tiene", self.my_num_ruedas, "ruedas"
    
    def motorized_vehicle(self, motor):
        self.have_motor = motor
        if self.have_motor == "si":
              print ("El movil tiene motor"
        elif self.have_motor == "no":
              print ("El movil no tiene motor"
    
    def capacity(self, cant_personas):
        self.my_capacity = cant_personas
          print ("El vehiculo puede llevar", self.my_capacity, "personas."

    def type_vehicle(self):
        if (self.my_capacity >= 14) and (self.have_motor == "si") and (self.my_num_ruedas == 4):
              print ("Es un bus"
        elif (self.my_capacity <14 and self.my_capacity >=7) and (self.have_motor == "si") and (self.my_num_ruedas == 4):
              print ("Es una van"
        elif (self.my_capacity <7 and self.my_capacity >=5) and (self.have_motor == "si") and (self.my_num_ruedas == 4):
              print ("Es una camioneta"
        elif (self.my_capacity <5 and self.my_capacity >=4) and (self.have_motor == "si") and (self.my_num_ruedas == 4):
              print ("Es un auto"
        elif (self.my_capacity <4 and self.my_capacity >=1) and (self.have_motor == "si") and (self.my_num_ruedas == 2):
              print ("Es una moto"
        elif (self.my_capacity <4 and self.my_capacity >=1) and (self.have_motor == "si") and (self.my_num_ruedas == 4):
              print ("Es una catriciclo"
        elif (self.my_capacity <4 and self.my_capacity >=1) and (self.have_motor == "no") and (self.my_num_ruedas == 3):
              print ("Es un triciclo"
        elif (self.my_capacity <4 and self.my_capacity >=1) and (self.have_motor == "no") and (self.my_num_ruedas == 2):
              print ("Es una bicicleta"
        elif (self.my_capacity <4 and self.my_capacity >=1) and (self.have_motor == "no") and (self.my_num_ruedas == 1):
              print ("Es un monociclo"
        else:
              print ("No es un vehiculo"

# Opcion mas corta

    def __init__(self,num_ruedas,motor,cant_personas):
        print ("Has creado un vehiculo")
        self.my_num_ruedas = num_ruedas
        self.my_capacity = cant_personas
        print("El movil tiene", self.my_num_ruedas, "ruedas y puede llevar a", self.my_capacity, "personas")
        self.have_motor = motor
        if self.have_motor == "si":
            print ("El movil tiene motor")
        elif self.have_motor == "no":
            print ("El movil no tiene motor")
        if (self.my_capacity >= 14) and (self.have_motor == "si") and (self.my_num_ruedas == 4):
            print ("Es un bus")
        elif (self.my_capacity <14 and self.my_capacity >=7) and (self.have_motor == "si") and (self.my_num_ruedas == 4):
            print ("Es una van")
        elif (self.my_capacity <7 and self.my_capacity >=5) and (self.have_motor == "si") and (self.my_num_ruedas == 4):
            print ("Es una camioneta")
        elif (self.my_capacity <5 and self.my_capacity >=4) and (self.have_motor == "si") and (self.my_num_ruedas == 4):
            print ("Es un auto")
        elif (self.my_capacity <4 and self.my_capacity >=1) and (self.have_motor == "si") and (self.my_num_ruedas == 2):
            print ("Es una moto")
        elif (self.my_capacity <4 and self.my_capacity >=1) and (self.have_motor == "si") and (self.my_num_ruedas == 4):
            print ("Es una catriciclo")
        elif (self.my_capacity <4 and self.my_capacity >=1) and (self.have_motor == "no") and (self.my_num_ruedas == 3):
            print ("Es un triciclo")
        elif (self.my_capacity <4 and self.my_capacity >=1) and (self.have_motor == "no") and (self.my_num_ruedas == 2):
            print ("Es una bicicleta")
        elif (self.my_capacity <4 and self.my_capacity >=1) and (self.have_motor == "no") and (self.my_num_ruedas == 1):
            print ("Es un monociclo")
        else:
            print ("No es un vehiculo")

movil = Vehiculo(2,"si",2) """
""" movil = Vehiculo()
print(movil.cantidad_ruedas(4))
print(movil.motorized_vehicle("si"))
print(movil.capacity(4))
print(movil.type_vehicle()) """

###### Otras formas de construir una clase #####

class Dino:
    #Cabeza = 1 Seria un atributo ya asignado pero invariable.
    def __init__(self, name_dino, genero, patas = 4, ojos = 2): #Atributo necesario, con = es modificable, si no se le asigna valor usa uno predeterminado
        self.its_name = name_dino
        self.its_paws = patas
        self.its_eyes = ojos
        self.its_genre = genero
        print ("Rwaaaar!!")
        print ("Ha nacido un dinosauro, se llamara", self.its_name)
    
    def skin(self, type_skin):
        self.its_skin = type_skin
    
    def height(self, meters):
        self.its_height = meters
    
    def characteristics(self):
        print (self.its_name, "es un dinosaurio con", self.its_paws, "patas,", self.its_eyes, "ojos,", self.its_skin,", con", self.its_height, "metros de alto, y es", self.its_genre)
    
    def cut_paws(self, cant_cortar_patas= 1): #Valor por defecto para un atributo necesario
        self.its_paws= self.its_paws - cant_cortar_patas #Si no se le da un valor resta siempre con 1.
   
dinosaurio = Dino("Pie pequeño", " un macho alfa pecho peludo")
dinosaurio.skin("plumoso")
dinosaurio.height(2)
dinosaurio.characteristics()
dinosaurio.cut_paws(2)
dinosaurio.characteristics()

dinosaurio2 = Dino("Tealha","una hembra, alfa, ovarios de acero, perra fria e inalcanzable",2)
dinosaurio2.skin("escamoso")
dinosaurio2.height(2)
dinosaurio2.characteristics()

#### Herencia ####
class TRex(Dino): #Permite que TRex comparta métodos y atributos similares a Dino.
    def __init__(self, nombre, genero, patas = 4, ojos = 2):
        self.its_name= nombre
        self.its_genre= genero
        self.its_paws= patas
        self.its_eyes= ojos
        print ("Hola, soy un TREX y me llamo", self.its_name)
    
robert = TRex("Roberto el TRex", "lo que se te antoje")
robert.height(4)
robert.skin("escamoso")
robert.characteristics()


