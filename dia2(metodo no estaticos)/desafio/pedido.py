from te import Te

te= Te()

clase_te= int(input("""
Ingrese el Té que desea comprar

1 > Te Negro
2 > Te Verde
3 > Agua de Hierba

respuesta > """))

sabor=input("""
Ingrese el sabor de te que quiere consumir > """)

#asignando valor a los atributos del objeto te
te.Sabor_te=sabor

formato= int(input(""" 
De los siguientes formatos, ¿Cual desa llevar?
Formato de 300 gr
Formato de 500 gr

respuesta >  """))

#asignando valor a los atributos del objeto te
te.Formato= formato

valor= Te.precios(formato)

print("")
print("-------Respuesta-------")
print("")
print(f"- Eleigo el sabor: {te.Sabor_te}")
print("")
print(f"- El formato de {te.Formato} tiene un valor de {valor} pesos")

print("")
print("Se le sugiere esta recomandacion con este tipo de Té")
desicion=Te.info_te(clase_te)
print("----------------------")