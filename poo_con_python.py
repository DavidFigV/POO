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
        return self.fuerza - enemigo.defensa
    
    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida -= daño
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if not enemigo.esta_vivo():
            enemigo.morir()
        print("Vida de", enemigo.nombre, "es", enemigo.vida)
        
#Variable de constructor de la clase
mi_personaje = Personaje("El Troyano", 200, 15, 12, 20)
mi_enemigo = Personaje("Dario", 10, 15, 12, 20)
mi_personaje.atributos()
mi_personaje.atacar(mi_enemigo)
mi_enemigo.atributos()