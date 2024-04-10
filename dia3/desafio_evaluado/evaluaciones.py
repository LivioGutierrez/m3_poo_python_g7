from pizza import Pizza
pizza= Pizza()

#Requerimiento 4
pizza.pedido_a_realizar()
print("")
print("Requerimiento 4")
print(pizza.valida)
print(pizza.tipo_masa)
print(pizza.vegetal1)
print(pizza.vegetal2)
print(pizza.proteico)

print("")
print("Requerimiento 5-A")
#Requerimiento 5-A
print(pizza.valida)
print(pizza.tipo_masa)
print(pizza.vegetal1)
print(pizza.vegetal2)
print(pizza.proteico)

print("")
print("Requerimiento 5-B")
#Requerimiento 2 y 5-B
respuesta=pizza.validador("salsa detomate",["salsa detomate", "salsa bbq"])
print(respuesta)

print("")
print("Requerimiento 5-D")
#Requerimiento 5-D
print(F"El tipo de masa es: {pizza.tipo_masa}")
print(F"El vegetal 1 es: {pizza.vegetal1}")
print(F"El vegetal 2 es: {pizza.vegetal2}")
print(F"El Proteico es: {pizza.proteico}")

#Requerimiento 5-E
print("")
print("Requerimiento 5-E")
print(F"La pizza es: {'si' if pizza.valida else 'no'}")