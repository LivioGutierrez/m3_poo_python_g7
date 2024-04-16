class Madre():
    def __init__(self, color: str):
        self.__color= color
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color= color

class Padre():
    def __init__(self, tamanio: int):
        self.__tamanio= tamanio
    
    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio= tamanio

#la clase que pones primero es la que te pedira primero3
class Hija(Madre,Padre):
    pass

princesa= Hija("Azul")
princesa.tamanio= 80
print(f"{princesa.tamanio}")