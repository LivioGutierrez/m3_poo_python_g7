class Ram():
    def __init__(self, velocidad, bite):
        self.velocidad= velocidad
        self.bite = bite

class DiscoDuro():
    def __init__(self, campasidad):
        self.capacidad= campasidad
        self.tipo="ssd"

class Teclado():
    def __init__(self, idioma:str, cant_tecla:int):
        self.idioma= idioma
        self.cantidad_tecla= cant_tecla

class Mause():
    def __init__(self, tipo:str, conectividad:str):
        self.tipo= tipo
        self.conectividad= conectividad

class Computador():
    def __init__(self, teclado:Teclado, mause:Mause):
        #El computador esta compuesto por la clase Ram
        
        self.ram = Ram(1500,32) # -> composicion
        self.disco_duro=DiscoDuro(1024) # -> composicion
        
        #revisa los parametro del contructor
        self.teclado= teclado # -> agregacion
        self.mouse= mause # -> agregacion

teclado= Teclado("Latino", 120)
mause= Mause("Gamer","Bluethoot")

computador_gamer= Computador(teclado, mause)

print(computador_gamer.ram.velocidad)
print(computador_gamer.teclado.cantidad_tecla)