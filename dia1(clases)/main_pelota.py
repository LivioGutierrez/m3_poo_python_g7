# Primea forma
#import pelota

#Instanciar o crear un obejto
#pelota_de_andy= pelota.Pelota()

# Segunda forma(Es la que mas se usa al trabajar con un objeto)
#Instanciar o crear un obejto
from pelota import Pelota
pelota_de_andy= Pelota()

print("")
print("DATOS")
print(pelota_de_andy)#<pelota.Pelota object at 0x0000020ADCB25E80>
print(type(pelota_de_andy))#<class 'pelota.Pelota'>
print(pelota_de_andy.forma)#redondeada
print(pelota_de_andy.material)#no manda nada por que esta vacio el atributo

print("")
print("ASIGNANDO DATOS")
pelota_de_andy.material= "Plastico"
print(pelota_de_andy.material)

print("")
print("CREANDO UNA PELOTA NUEVA")
pelota_tenis= Pelota()
print(pelota_tenis.material)
print(pelota_tenis.posicion)

print("")
print("METODOS ESTATICOS")

#Metodos estaticos, Los metodos estaticos no requieren de un objeto para invocar al metodo
print(Pelota.crear_rebote) #<function Pelota.crear_rebote at 0x00000262E9ACD9E0>
print(Pelota.crear_rebote()) #[5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

print("")
Pelota.posicion= [2,4,6]#modificando el valor del atributo posicion
Pelota.imprimir_posicion()# [3, 0, 2, 1, 0]
print(Pelota.posicion)

pelota_futbol= Pelota()
print(pelota_futbol.posicion)

#Metodos no estaticos
print("")
print("METODOS NO ESTATICOS")
pelota_futbol.rebotar() #cambia la posicion
print(pelota_futbol.posicion) # [5, 0, 4, 0, 3, 0, 2, 0, 1, 0]

pelota_basquet= Pelota()
print(pelota_basquet.posicion)


#los metodos no estaticos permiten crear atributos de tipo "atributos de instantes"
pelota_basquet.nuevo_atributo() #si no invocamos antes el metodo
print(pelota_basquet.color) #blanco

#print(pelota_futbol.color) #AttributeError: 'Pelota' object has no attribute 'color'