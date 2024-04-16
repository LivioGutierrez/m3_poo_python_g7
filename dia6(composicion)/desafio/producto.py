""" 
TIPOS DE TIENDA
“Restaurante”, “Supermercado” y “Farmacia”.
"""
class Producto():
    def __init__(self, nombre,valor, stock=0):
        self.__nombre= nombre
        self.__valor= valor
        self.__stock= max (stock,0)
    
    def __str__(self):
        return f"Nombre: {self.__nombre}, Valor: {self.__valor}, Stock: {self.__stock}"
    
    def agregar_stock(self, cantidad):
        self.__stock+=cantidad
    
    #getters
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def valor(self):
        return self.__valor
    @property
    def stock(self):
        return self.__stock
    
    #Setters
    @stock.setter
    def stock(self, cantidad):
        self.__stock = max(cantidad,0)