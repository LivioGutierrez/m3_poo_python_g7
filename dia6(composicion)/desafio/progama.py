from tienda import Restaurante
from producto import Producto

nombre_de_tienda= input("Ingrese el nombre de la tienda: ")
delivery= float(input("Ingrese el costo del delivery: "))

op=1

if op == 1:
    tienda=Restaurante(nombre_de_tienda, delivery)

print("")
while True:
        print("\nSeleccione una acción:")
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
            producto = Producto(nombre_producto, precio_producto, stock_producto)
            tienda.ingresar_producto(producto)
            
        elif opcion == "2":
            print(":::::Listado de productos:::::")
            print("")
            print(tienda.listar_producto())
            print("")
            print(":::::Listado de productos:::::")
            
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            tienda.realizar_venta(nombre_producto, cantidad)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")