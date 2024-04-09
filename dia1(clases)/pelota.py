""" 

Los scripts van en minuscula y en singular
Las clases van con Mayuscula la primera letra en el nombre 
"""

class Pelota():
    forma= "redondeada" #atributo estatico o atributo de clase
    material= ""
    posicion= [3,0,2,1,0]
    
    
    @staticmethod #decorador
    def crear_rebote(): #metodo estatico
        return[5,0,4,0,3,0,2,0,1,0]
    
    @staticmethod
    def imprimir_posicion():
        Pelota.crear_rebote() # llamando a un metodo
        print(Pelota.posicion) # imporimiendo el valor de un atributo
    
    #metono no estatico o de instancia, siempre van con self
    #modificacion del estado de un objeto
    def rebotar(self):
        self.posicion= self.crear_rebote()
    
    def nuevo_atributo(self):
        self.color= "blanco"