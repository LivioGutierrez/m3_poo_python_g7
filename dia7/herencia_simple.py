class Padre():
    #Atributos de clases
    color= "verde"
    #Contructor
    def __init__(self,tamanio:int):
        #atributos de instancias
        self.__tamanio= tamanio #atributo privado
        
    #Metodos staticos
    
    #Metodos de instancia
    def cambiar_color(self, color:str):
        if color != "":
            self.color = color
    #Sobre Escritura
    def __str__(self):
        return f"El color es {self.color}, y el tamanio {self.__tamanio}"
    
    #Getter - Setters
    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio: int):
        if tamanio > 0:
            self.__tamanio= tamanio
        else:
            self.__tamanio= 0

#HERENCIA
class Hija(Padre):
    peso= 100

class Hijo(Padre):
    dauda= 120

class Nieto(Hija):
    altura= 100


#instancia de la clase
hijita= Hija(100)
print(f"El color de la clase hija es {hijita.color} y el tamaño es: {hijita.tamanio}")

regalon= Nieto(50)



