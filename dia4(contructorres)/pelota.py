class Pelota():
    #Atributos de clases
    marca="adidas"
    
    #Contructor
    def __init__(self, color: str, tamanio= 20, material="plastico"):#es una funcion, es un metodo no estatico
        print("Metodo contructor al crear el objeto")
        self.tamanio= tamanio
        self.material= material
        self.rebotes= 0
        self.__color = color #ocultando el atributo
        self.marca="Adidas"
        self.__password="as"
        
    #Metodo oculto
    def __getColor(self):
        return self.__color
    
    def setColor(self, color):#Se ocupa como metodo en el main
        self.__color= color
        
    def setPassword(self, password):
        self.__password= password
    
    #Getter-> da acceso al atributos ocultos y no deja cambiar
    @property
    def color(self):
        return self.__color
    
    @color.setter#Se ocupa como atributo en el main
    def color(self, color:str):
        self.__color= color if color !="" else 'verde'
    
    #deleter
    @color.deleter
    def color(self):
        del self.__color

print("")
print("PElOTA DE FUTBOL")
pelota_futbol= Pelota("Amarillo",16,"Plastico")#Se tiene que si o si pasar los argunmentos si en el contructor estan, si se le quita un argumento por ejemplo 16 "Plastico" se pasara a tamaño
print(pelota_futbol.color, pelota_futbol.tamanio, pelota_futbol.material)
#print(pelota_futbol.__color) da error
# print(pelota_futbol.getColor())
#print("getercolor()",pelota_futbol.getColor())
print("Metodo getter", pelota_futbol.color)#Sin parentesis

print("")
print("PElOTA 3")
pelota3= Pelota("Rojo")
pelota3.rebotes=100 #esto no es seguro
print(pelota3.color, pelota3.tamanio, pelota3.material, pelota3.rebotes)
