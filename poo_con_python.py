class Personaje:
    #Atributos de la clase
    nombre = "Player"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0
    
#Variable de constructor vacío de la clase
mi_personaje = Personaje()
#Modificando los valores de los atributos
mi_personaje.nombre = "Damaris"
mi_personaje.fuerza = 1
mi_personaje.inteligencia = 5
mi_personaje.defensa = 10
mi_personaje.vida = 3
print("El nombre del personaje es",mi_personaje.nombre)
print("La fuerza del personaje es",mi_personaje.fuerza)
print("La inteligencia del personaje es",mi_personaje.inteligencia)
print("La defensa del personaje es",mi_personaje.defensa)
print("La vida del personaje es",mi_personaje.vida)
        