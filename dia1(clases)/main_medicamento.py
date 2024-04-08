from medicamento import Medicamento

#Instanciar o crear un obejto
paracetamol= Medicamento()
aspirina= Medicamento()

print(paracetamol.descuento)#0.05
print(aspirina.descuento)#0.05

print("")
print("CAMBIANDO DATO DE PARACETAMOS")
paracetamol.descuento= 0.06
print(paracetamol.descuento)