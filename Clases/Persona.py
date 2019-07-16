# Clase
# una receta para crear un objeto y darle caracteristicas o atributos
# Método
# una funcion dentro de la clase que configura el atributo

class Persona: #Clase debe ir con mayuscula
    mi_edad = 0

    def __init__(self): #Metodo constructor
        print("Hello mom! I've finally born")
#Metodo de hacerle cumplir años a tu persona.
    def birthday(self):
        self.mi_edad = self.mi_edad + 1
        print("Happy birthday to me! Now i have", self.mi_edad, "year old")
#Metodo de designar edad y obtener una respuesta de su persona.
    def age(self, an_age, person):
        self.mi_edad = an_age
        if an_age <= 5:
            print("I'm", self.mi_edad, "year old now, such a cute baby")
        elif an_age > 5 and an_age <= 10:
            print("I'm", self.mi_edad, "year old now, just a pricky", person.genre)
        elif an_age > 10 and an_age <= 15:
            print("I'm", self.mi_edad, "year old now, you happy mom..?")
        elif an_age > 15 and an_age <= 18:
            print("I'm", self.mi_edad, "year old now, don't ask i don't know what to do with the rest of my life")
        elif an_age > 18 and an_age <= 25:
            print("I'm", self.mi_edad, "year old now, why do you want to make me suffer already? D:")
        elif an_age > 25 and an_age <= 30:
            print("I'm", self.mi_edad, "year old now, tell me at least i'll be able to travel trought the cloud :(")
        elif an_age > 30 and an_age <= 50:
            print("I'm", self.mi_edad, "year old now, not having childs just telling..")
        elif an_age > 50 and an_age <= 80:
            print("I'm", self.mi_edad, "year old now, feelin' little grumpy")
        else:
            print("I'm", self.mi_edad, "year old now, yup, my momma likes gods and vampires")
#Metodo de designar nombre y obtener una respuesta de su persona.
    def name(self, un_nombre):
        self.mi_nombre= un_nombre
        print("Ok, thanks my existence will be called ", self.mi_nombre)
#Metodo de designar altura y obtener una respuesta de tu persona segun su altura relacionada al estandar paraguayo.
    def height(self, una_altura):
        self.mi_altura= una_altura
        if una_altura >= 160:
            print("Oh!", una_altura, "m, i'm tall, more than average")
        elif una_altura < 160 and una_altura >= 140:
            print ("So,", una_altura, " m, i'm average but not bad")
        elif una_altura < 140:
            print ("Oh oh,", una_altura, " m, i'm a hobbit, tell me i don't have furry feets")
#Metodo de designar genero y obtener una respuesta de tu persona segun su genero o no genero.
    def genre(self, un_genero):
        self.mi_genero = un_genero
        if un_genero == "girl":
            print("Yeah giiiiirrl! i'm a", un_genero)
        elif un_genero == "boy":
            print ("Yeah boy!i'm a", un_genero)
        else:
            print ("Rrrr, I'm a misterious person! I could be anything or nothing at the time")
#Metodo de designar peso y obtener una respuesta de su persona segun la relacion con tu altura y genero.
    def weight(self, un_peso, person):
        self.mi_peso= un_peso
        if person.genre == "girl":
            if un_peso > 60 and person.height >= 160:
                print("Oh!", un_peso, "Kg, i should sacrifice some chocolate")
            elif (un_peso < 60 and un_peso <40) and (person.height <160 and person.height >= 140):
                print ("So,", un_peso, " Kg, i'm goood bitch")
            elif un_peso < 40 and (person.height <140):
                print ("Yeah!,", un_peso, "some chocolate comes in handy")
        elif person.genre == "boy":
            if un_peso >= 90 and person.height >= 170:
                print("Let's be honest!", un_peso, "Kg, leg day isn't so hard, right?")
            elif (un_peso < 90 and un_peso >= 75) and (person.height <170 and person.height >= 155):
                print ("So,", un_peso, " Kg, damn than + abs and i can start melting")
            elif un_peso < 75 and (person.height < 155):
                print ("Yeah!,", un_peso, "some french fries with extra cheese, please")
        else:
            print ("Interesting,", un_peso, "Kg, no social construct matters to meeeeee")

    def nation(self, an_nationality):
        self.my_nationality= an_nationality

    def say_nation(self):
        print("Proudly from", self.my_nationality) #Una variable que puedo llamar en otros metodos diferente a las variables de funcion


p1 = Persona()
p1.name("Syrionax")
p1.birthday()
p1.genre("")
p1.height(160)
p1.weight(56, p1) #Le designo con los datos de que persona debe comparar para darme una respuesta
p1.age(300,p1) #Igual a arriba
p1.nation("Paraguay") #Si es string hay que trabajar con la variable no con el metodo
p1.say_nation()

p2 = Persona()
p2.name("Britz")
p2.nation("Suiza")
p2.say_nation()