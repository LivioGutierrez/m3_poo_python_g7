""" 
TIPOS DE TIENDA
“Restaurante”, “Supermercado” y “Farmacia”.
"""
class Tienda():
    def __init__(self, nombre, delivery):
        #clases semi privadas
        self._nombre= nombre
        self._delivery= delivery
        self._productos= []
    
    def ingresar_producto(self, producto):
        for produc in self._productos:
            if produc.nombre == producto.nombre:
                produc.agregar_stock(producto.stock)#llama el metodo "agregar_stock" de la clase producto
        self._productos.append(producto)#agrega la final de la lista el producto pasado
        
    def listar_producto(self):
        for produc in self._productos:
            print(produc)
    
    def ralizar_ventas(self, nombre_producto, cantidad):
        for produc in self._productos:
            if produc == nombre_producto and produc.stock >= cantidad:
                produc.stock -= cantidad
                
                print(f"Venta Completada, Usted lleva una cantidad de {cantidad} del producto: {nombre_producto}")
            else:
                print("Venta no realizada, falta de Stock")


class Restaurante(Tienda):
    def ingresar_producto(self, producto):
        producto.stock= 0
        super().ingresar_producto(producto)
        
    def listar_producto(self):
        for produc in self._productos:
            print(f"Nombre: {produc.nombre}, Precio: {produc.valor}")
    
    def realizar_venta(self, nombre_producto, cantidad):
        super().ralizar_ventas(nombre_producto, cantidad)
    
class Supermercado(Tienda):
    def ingresar_producto(self, producto):
        super().ingresar_producto(producto)
        
    def listar_producto(self):
        for produc in self._productos:
            if produc.stock <= 10:
                print(f"¡ALERTA! queda poco stock de este producto: {produc.nombre}")
                

class Farmacia(Tienda):
    def ingresar_producto(self, producto):
        super().ingresar_producto(producto)
    
    def listar_producto(self):
        for produc in self._productos:
            if produc.stock <= 10:
                print(f"¡ALERTA! queda poco stock de este producto: {produc.nombre}")

    def realizar_venta(self, nombre_producto, cantidad):
        for produc in self._productos:
            if produc.valor >= 15000 and produc.stock >= cantidad:
                print("")
                print(f"Envío gratis al solicitar este producto: {produc.nombre}")
                print("")
            else:
                print("")
                print("No tenemos esa cantidad en el Stock")
                print("")
