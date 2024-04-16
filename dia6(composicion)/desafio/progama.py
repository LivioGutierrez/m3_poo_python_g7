from tienda import Restaurante,Supermercado,Farmacia
from producto import Producto


print(""" 
1: Restaurante
2: Supermercado
3: Farmacia
""")

op=int(input("Ingrese el restaurante a crear: "))

nombre_de_tienda= input("Ingrese el nombre de la tienda: ")
delivery= float(input("Ingrese el costo del delivery: "))

if op== 1:
    tienda= Restaurante(nombre_de_tienda, delivery)
elif op== 2:
    tienda= Supermercado(nombre_de_tienda, delivery)
elif op== 3:
    tienda= Farmacia(nombre_de_tienda, delivery)

print("")
while True:
        print("Seleccione una acción:")
        print(""" 
1: Agregar producto
2: Listar productos
3: Realizar una venta
4: Salir
""")

        opcion = input("Ingrese el número de la acción deseada: ")

        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            precio_producto = float(input("Ingrese el precio del producto: "))
            stock_producto = int(input("Ingrese el stock del producto: "))
            print("")
            producto = Producto(nombre_producto, precio_producto, stock_producto)
            tienda.ingresar_producto(producto)
            
        elif opcion == "2":
            print(":::::Listado de productos:::::")
            print("")
            print(tienda.listar_producto())
            print("")
            print(":::::::::::::::::::::::::::::")
            
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            tienda.realizar_venta(nombre_producto, cantidad)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")