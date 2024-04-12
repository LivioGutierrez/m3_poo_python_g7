#Informacion de que tinee que hacer el personaje
"""
Completos
    ● Cada personaje tiene un nombre, el cual debe ser especificado al momento de crear
    un personaje. -> (COMPLETO)
    
    ● Cada personaje recién creado tiene nivel 1 y experiencia 0 (estos son los únicos
    valores posibles al momento de crear un personaje). -> (COMPLETO)
    
    ● Dar la bienvenida al jugador y solicitar el nombre para su personaje. -> (COMPLETO)
    
    ● Crear el personaje del jugador y mostrar su estado en panta. -> (COMPLETO)

● A cada personaje es posible consultarle o asignarle un estado. Al solicitar el estado
de un personaje, se debe mostrar en pantalla su nombre, su nivel y su experiencia. Al
asignar un valor al estado, este valor corresponderá a la experiencia recibida por el
personaje. Según la experiencia recibida, se debe modificar la experiencia actual del
personaje y su nivel de acuerdo a lo siguiente:
    ○ Los valores posibles de experiencia son entre 0 y 99 inclusive.
    ○ El nivel mínimo es 1 y no hay máximo.
    ○ Cada 100 puntos de experiencia recibidos, el personaje sube 1 nivel (su nivel
    aumenta en 1). Ejemplo: El personaje tiene actualmente nivel 1 y experiencia
    0. Si se asigna 250 a su estado, pasará a tener nivel 3 y experiencia 50.
    ○ Si la experiencia recibida es negativa, se debe restar a la experiencia actual
    del personaje. Cada vez que la experiencia sea menor a 0, el personaje baja
    de nivel (su nivel disminuye en 1). Ejemplo: El personaje tiene actualmente
    nivel 3 y experiencia 50. Si se asigna -150 a su estado, pasará a tener nivel 2 y
    experiencia 0. Si el personaje ya tiene nivel 1 y experiencia 0, no se altera su
    nivel ni su experiencia al recibir experiencia negativa. -> (PREGUNTAR A QUE SE REFIERE CON EL ESTADO)

● Informar por pantalla al jugador que ha aparecido un orco y la probabilidad que tiene
de ganarle. Informarle también que en caso de ganarle, recibirá 50 puntos de
experiencia y el orco perderá 30 y que, en caso de perder, perderá 30 puntos de
experiencia mientras que el orco ganará 50. Consultar finalmente al jugador si desea
atacar o huir. El jugador debe ingresar 1 para “Atacar” y 2 para “Huir”.

"""

#Tips:
"""
● Puede usar una variable temporal que corresponda a la suma entre la
experiencia actual del personaje y la asignada al estado. Luego, mediante
ciclos while puede ir actualizando este valor y el nivel del personaje y,
terminados los ciclos, se asigna a la experiencia actual el valor de suma
temporal actualizado. Otra posible solución es utilizando división redondeada
(//) y módulo (%).

● Un personaje se considera mayor a otro si tiene mayor nivel, y se considera menor a
otro si tiene menor nivel.

● Puedes agregar en la clase un método estático que reciba por parámetro
la probabilidad, muestre en pantalla todo lo requerido y retorne la opción de
juego del usuario.


"""

"""
Integrantes:

-> Najla Gatica
-> Edison Ahumada
-> Manuel Ruiz
-> Pablo Hernández
-> Livio Gutieerez
"""
from personaje import Personaje
import random

class Juego:
    def __init__(self, jugador: Personaje, orco: Personaje):
        self.jugador = jugador
        self.orco = orco

    def jugar(self):
        vidas = 4
        while vidas > 0:
            # Calcular la probabilidad de ganar del jugador contra el orco
            probabilidad_ganar = int(self.jugador.nivel * 50)
            print("")
            print("¡Ha aparecido un Orco!")
            print(f"Con el nivel actual, tienes una {probabilidad_ganar}% de probabilidad de ganarle al Orco.")

            # Enfrentamiento con el orco y elección del jugador
            opcion = None
            while opcion not in ["1", "2"]:
                opcion = input("¿Qué deseas hacer?\n1. Atacar\n2. Huir\n")

                if opcion == "1":
                    if random.random() < probabilidad_ganar / 100:
                        print("¡Le has ganado al orco, felicidades!")
                        self.jugador.aumentar_exp(50)
                        print("¡Recibirás 50 puntos de experiencia!")
                    else:
                        print("¡Oh no!, has sido derrotado por el orco.")
                        self.jugador.disminuir_exp(30)
                        vidas -=1
                        print(f"Perdiste 30 puntos de experiencia. Perdiste una vida. Vidas: {vidas}") 
                elif opcion == "2":
                    print("Has huido de la batalla.")
                    vidas= 0
                else:
                    print("Opción inválida.")
                
                #Estado de los jugadores
                print(self.jugador)
                print(self.orco)



if __name__ == "__main__":
    
    print("¡Bienvenido a Gran Fantasia!")
    nombre_personaje = input("Por favor, indica el nombre de tu personaje: > ")
    
    jugador = Personaje(nombre_personaje,1)
    print(jugador)

    orco = Personaje("Orco",1)
    print(orco)
    
    juego = Juego(jugador,orco)
    juego.jugar()