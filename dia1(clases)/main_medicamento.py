from medicamento import Medicamento

#Instanciar o crear un obejto
paracetamol= Medicamento()
aspirina= Medicamento()

print(paracetamol.descuento)#0.05
print(aspirina.descuento)#0.05

print("")
print("CAMBIANDO DATO DE PARACETAMOS")
#paracetamol.descuento= 0.06 MODIFICANDO EL DATO DEL ATRIBUTO EN ESTA INSTANCIA
print(paracetamol.descuento)

#Medicamento.descuento= 0.04

print("")
print("LLAMANDO A UN METODO ESTATICO")
precio= int(input("Ingrese el precio a validar > "))
es_valido= Medicamento.validad_mayor_a_cero(precio)

if es_valido:
    print("El precio ingresado es valido")
else:
    print("El precio ingresado no es valido")


if paracetamol.IVA == aspirina.IVA and paracetamol.descuento == aspirina.descuento:
    print("Todos las instancias(objetos), tienen los mismos valores de IVA y descuento")
    print(f"el valor del IVA es {Medicamento.IVA}")
    print(f"El valor de descuento es: {Medicamento.descuento}")


aspirina.modificar_atibuto()
print(aspirina.IVA)