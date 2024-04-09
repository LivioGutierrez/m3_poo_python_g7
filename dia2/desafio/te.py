class Te():
    #Atributos
    Sabor_te= ""
    Formato= 0
    
    #Metodo estatico que devuelve informacion del té
    @staticmethod
    def info_te(respuesta):
        tiempo_preparacion= {
            1:{"minutos de preparacion":3,
                "ingerir":"en el desayuno"},# te_negro
            2:{"minutos de preparacion":5,
                "ingerir":"en el medio dia"}, #te_verde
            3:{"minutos de preparacion":6,
                "ingerir":"en el atardecer"}}#agua_hierba
        
        for clave, valor in tiempo_preparacion.items():
            if respuesta == clave:
                print(f"Opcion de Té: {clave}")
                for clave, valor in valor.items():
                    print(f"  - {clave}: {valor}")
        return respuesta
    
    #Metodo de precios
    @staticmethod
    def precios(desicion):
        if desicion == 300:
            return 3000
        else:
            return 5000
