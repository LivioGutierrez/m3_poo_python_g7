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
    #polimorfismo es el cambio de comportamiento del metodo segun como estava escrito en el padre
    def cambiar_color(self, color:str):
        self.color = color

class Hijo(Padre):
    dauda= 120
    
    def __init__(self, tamanio: int, saldo = 0):
        super().__init__(tamanio)#llamado al constructor padre
        self.__saldo = saldo
    
    @property
    def saldo(self):
        return self.__saldo

class Nieto(Hija):
    altura= 100


#instancia de la clase
hijita= Hija(100)
hijita.cambiar_color("")
print(f"El color de la clase hija es {hijita.color} y el tamaño es: {hijita.tamanio}")

regalon= Nieto(50)

super(type(hijita), hijita).cambiar_color("Gris")
print(f"El color de la clase hija es {hijita.color} y el tamaño es: {hijita.tamanio}")

hijito= Hijo(10, 1200)
print(hijito.tamanio, hijito.saldo, hijito.dauda)

#ISINSTANCE isinstance(objeto, clase_a_comparar)
print(f"princesa es instancia de Hija: {isinstance(hijita,Hija)}")
print(f"princesa es instancia de Padre: {isinstance(hijito,Padre)}")
print(f"princesa es instancia de Madre: {isinstance(regalon,Hija)}")