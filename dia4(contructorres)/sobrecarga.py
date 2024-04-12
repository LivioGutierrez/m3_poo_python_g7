class Auto():
    def __init__(self, color: str="blanco"):
        self.__color= color
    
    def __str__(self):
        return f"Metodo Sobre cargado {self.__color}"

nissan= Auto()
print(nissan)#<__main__.Auto object at 0x000002AA5D1E6330>

toyota= Auto("Negro")
print(toyota)