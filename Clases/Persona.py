# Clase
# una receta para crear un objeto y darle carasteristicas o atributos
# Método
# una funcion dentro de la clase que configura el atributo

class persona:
    mi_edad = 0

    def __init__(self):
        print("Hello mom! I've finally born")

    def birthday(self):
        self.mi_edad = self.mi_edad + 1
        print("Happy birthday to me! Now i have", self.mi_edad, "year old")

    def name(self, un_nombre):
        self.mi_nombre= un_nombre
        print("Ok, thanks my existence will be called ", self.mi_nombre)
    
    def height(self, una_altura):
        self.mi_altura= una_altura
        if una_altura >= 160:
            print("Oh!", una_altura, "m, i'm tall, more than average")
        elif una_altura < 160 and una_altura >= 140:
            print ("So,", una_altura, " m, i'm average but not bad")
        elif una_altura < 140:
            print ("Oh oh,", una_altura, " m, i'm a hobbit, tell me i don't have furry feets")

    def genre(self, un_genero):
        self.mi_genero = un_genero
        if un_genero == "nena":
            print("Yeah giiiiirrl! i'm a", un_genero)
        elif un_genero == "nene":
            print ("Yeah boy!i'm a", un_genero)
        else:
            print ("Rrrr, I'm a misterious person! I could be anything or nothing at the time")

    def weight(self, un_peso):
        self.mi_peso= un_peso
        if p1.genre == "nena":
            if un_peso > 60 and p1.height >= 160:
                print("Oh!", un_peso, "Kg, i should sacrifice some chocolate")
            elif (un_peso < 60 and un_peso <40) and (p1.height <160 and p1.height >= 140):
                print ("So,", un_peso, " Kg, i'm goood bitch")
            elif un_peso < 40 and (p1.height <140):
                print ("Yeah!,", un_peso, "some chocolate comes in handy")
        elif p1.genre == "nene":
            if un_peso >= 90 and p1.height >= 170:
                print("Let's be honest!", un_peso, "Kg, leg day isn't so hard, right?")
            elif (un_peso < 90 and un_peso >= 75) and (p1.height <170 and p1.height >= 155):
                print ("So,", un_peso, " Kg, damn than + abs and i can start melting")
            elif un_peso < 75 and (p1.height < 155):
                print ("Yeah!,", un_peso, "some french fries with extra cheese, please")
        else:
            print ("Interesting,", un_peso, "Kg, no social construct matters to meeeeee")


p1 = persona()
p1.name("Syrionax")
p1.birthday()
p1.genre("")
p1.height(160)
p1.weight(56)