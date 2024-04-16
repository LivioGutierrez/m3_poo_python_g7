class Madre():
    def __init__(self, color: str, **kwargs):
        super().__init__(**kwargs)
        self.__color= color
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, color):
        self.__color= color

class Padre():
    def __init__(self, tamanio: int, **kwargs):
        super().__init__(**kwargs)
        self.__tamanio= tamanio
    
    @property
    def tamanio(self):
        return self.__tamanio
    
    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio= tamanio

#la clase que pones primero es la que te pedira primero3
class Hija(Madre,Padre):
    #Sobre escribiendo el contructor
    # def __init__(self, color: str, tamanio: int):
    #     Madre.__init__(self,color)
    #     Padre.__init__(self, tamanio)
    def __init__(self, deuda = 0, **kwargs):
        super().__init__(**kwargs)
        
        #atributo de instancia propio de Hija
        self.deuda= deuda

#princesa= Hija("Azul",80)
princesa = Hija(deuda=350, color="Azul", tamanio=80)
print(f"{princesa.tamanio},{princesa.color}")

#ISINSTANCE isinstance(objeto, clase_a_comparar)
print(f"princesa es instancia de Hija: {isinstance(princesa,Hija)}")
print(f"princesa es instancia de Padre: {isinstance(princesa,Padre)}")
print(f"princesa es instancia de Madre: {isinstance(princesa,Madre)}")