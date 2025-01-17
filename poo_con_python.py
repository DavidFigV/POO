class Personaje:
    #Atributos de la clase
    nombre = "Player"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
    
    def atributos(self):
        print(self.nombre)
        print("- Fuerza: ",self.fuerza)
        print("- Inteligencia: ",self.inteligencia)
        print("- Defensa: ",self.defensa)
        print("- Vida: ",self.vida)
        
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
        
    def esta_vivo(self):
        return self.vida > 0
    
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")
        
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa if self.fuerza >= enemigo.defensa else 0
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if not enemigo.esta_vivo():
            enemigo.morir()
        print("Vida de", enemigo.nombre, "es", enemigo.vida)
    
#Creando classe "Guerrero" que hereda de su clase padre "Personaje"
class Guerrero(Personaje):
    #Sobreescribir el constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        #LLamar a la clase padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
    
    #Pedirle al usuario escoger un arma
    def cambiar_arma(self):
        try:
            opcion = int(input("ARMAS DISPONIBLES\n(1) Espada de plata - Daño 10\n(2) Lanza - Daño 8\nElige un arma:"))
            if opcion == 1:            
                self.espada = 10
            elif opcion == 2:
                self.espada = 8
            else:
                print("valor incorrecto")
                self.cambiar_arma()
        except ValueError:
            print("valor incorrecto")
            self.cambiar_arma()
    
    #Sobreescribir método
    def atributos(self):
        super().atributos()
        print("- Espada ", self.espada)
        
    #Sobreescribir el cálculo de daño
    def daño(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa
    
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro
    
    def atributos(self):
       super().atributos()
       print("- Libro: ", self.libro)
       
    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

trakalosa = Personaje("La trakalosa de Monterrey", 20, 15, 10, 100)
hercules = Guerrero("Hercules", 20, 15, 10, 100, 5)
diosito = Mago("Diosito", 20, 15, 10, 100, 5)
#Imprimir atributos antes del ataque
trakalosa.atributos()
hercules.atributos()
diosito.atributos()
#Ataques
trakalosa.atacar(hercules)
hercules.atacar(diosito)
diosito.atacar(trakalosa)
#Imprimir atributos despues del ataque
trakalosa.atributos()
hercules.atributos()
diosito.atributos()

#Variable de constructor de la clase
#mi_personaje = Personaje("El Troyano", 20, 15, 12, 20) #nombre, fuerza, inteligencia, defensa, vida
#mi_enemigo = Personaje("Dario", 10, 15, 12, 20)
#mi_personaje.atributos()
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.atributos()