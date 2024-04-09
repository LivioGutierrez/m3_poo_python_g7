from medicamento import Medicamento

#paso 1: crear una instancia
meidcamento_nuevo= Medicamento()

#paso 2: solicitud de ingreso de dato
precio= int(input("Ingrese le precio del medicamento > "))

#paso 3: pasar al metodo de instancia el valor capturado
meidcamento_nuevo.asigna_precio(precio)

print(f"el precio es de {meidcamento_nuevo.precio}")
print(f"el descuento es de {meidcamento_nuevo.descuento}")