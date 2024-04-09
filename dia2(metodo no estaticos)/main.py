from pelota import Pelota

#Creaccion de objetos o instancia de la clase

# Se crea instancia
pelota_multicolor = Pelota()


#print(pelota_multicolor.color) -> AttributeError: 'Pelota' object has no attribute 'color'

pelota_multicolor.asigna_color("rojo")
print(pelota_multicolor.color)
pelota_multicolor.lee_color()

pelota_multicolor.asigna_color("verde")
pelota_multicolor.lee_color_local_y_atributo("amarillo")

"""
da error por que no tiene color y la funcion "lee_color_local_y_atributo" la llama en esta parte "self.lee_color()"

pelota_negra = Pelota()
pelota_negra.lee_color_local_y_atributo("Negro")"""