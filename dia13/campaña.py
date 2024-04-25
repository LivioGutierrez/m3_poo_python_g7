
from largoexcedidoerror import LargoExcedidoError

class Camapaña(LargoExcedidoError):
    def __init__(self, fecha_inicio, fecha_termino, nombre=" "):
        self.__nombre=nombre
        self.__fecha_inicio=fecha_inicio
        self.__fecha_termino=fecha_termino
        # super().__init__(*args)
    
    def __str__(self) -> str:
        return f"Nombre: {camapaña.nombre}\nFecha de inicio: {camapaña.fecha_inicio}\nFecha de termino: {camapaña.fecha_termino}"
    
    #GETTER Y SETTER DE NOMBRE
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        
        if len(nombre) < 251 and len(nombre) > 0:
            self.__nombre=nombre
        else:
            print("Print de error")
    
    #GETTER Y SETTER DE FECHA DE INICIO
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self):
        pass
    
    #GETTER Y SETTER DE FECHA DE TERMINO
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self):
        pass
    
    

if __name__ == "__main__":
    camapaña=Camapaña(nombre="Campaña el Don Dimadon",fecha_inicio="2024/10/05",fecha_termino="2024/10/06")
    camapaña.nombre= ""
    print(camapaña)