class Personaje:
    #Atributos de la clase
    __nombre = "Player"
    __fuerza = 0
    __inteligencia = 0
    __defensa = 0
    __vida = 0
    
    def __init__(self, __nombre, __fuerza, __inteligencia, __defensa, __vida):
        self.__nombre = __nombre
        self.__fuerza = __fuerza
        self.__inteligencia = __inteligencia
        self.__defensa = __defensa
        self.__vida = __vida
    
    def atributos(self):
        print(self.__nombre)
        print("- Fuerza: ",self.__fuerza)
        print("- Inteligencia: ",self.__inteligencia)
        print("- Defensa: ",self.__defensa)
        print("- Vida: ",self.__vida)
        
    def subir_nivel(self, __fuerza, __inteligencia, __defensa):
        self.__fuerza += __fuerza
        self.__inteligencia += __inteligencia
        self.__defensa += __defensa
        
    def esta_vivo(self):
        return self.__vida > 0
    
    def morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")
        
    def daño(self, enemigo):
        return self.__fuerza - enemigo.__defensa if self.__fuerza >= enemigo.__defensa else 0
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida -= daño
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        if not enemigo.esta_vivo():
            enemigo.morir()
        print("Vida de", enemigo.__nombre, "es", enemigo.__vida)
        
    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self, fuerza):
        self.__fuerza = fuerza if fuerza >= 0 else print("Error, hast puesto un numero negativo")
                    
        
#Variable de constructor de la clase
mi_personaje = Personaje("El Troyano", 20, 15, 12, 20) #__nombre, __fuerza, __inteligencia, __defensa, __vida
mi_enemigo = Personaje("Dario", 10, 15, 12, 20)

#Prueba I. Sin acceso al atributo
#print(mi_personaje.__fuerza)

#Prueba 7. Getters and setters
print(mi_personaje.get_fuerza())
mi_personaje.set_fuerza(-100)
print(mi_personaje.get_fuerza())


mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()

#mi_personaje.atributos()