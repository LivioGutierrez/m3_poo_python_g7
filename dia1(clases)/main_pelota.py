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