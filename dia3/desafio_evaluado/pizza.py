
class Pizza():
    masa=["tradicional","delgada"]
    proteicos=["pollo", "vacuno", "carne"]
    verduras= ["tomate","aceitunas","champiñones"]
    
    #Requerimiento 1
    #Atributos
    tipo_masa= None
    vegetal1= None
    vegetal2= None
    proteico= None
    
    @staticmethod
    def validador(elemento, valor):#valor seria la lista
        if elemento in valor:
            return True
        return False
    
    #Requerimiento 3 y 5-C
    def pedido_a_realizar(self):
        #Menu
        print("""
                            Ingredientes:
                    
            Proteicos          Vegetal          Masa
            ---------          -------          ----   
            > Pollo            > Tomate        > Tradicional  
            > Vacuno           > Aceitunas     > Delgada
            > Carne            > Champiñones
        """)
        
        #Asignandole los valores que ingrese el usuario a los atributos
        self.proteico= input("Ingrese proteicos > ")
        self.vegetal1= input("Ingrese vegetales > ")
        self.vegetal2= input("Ingrese vegetales > ")
        self.tipo_masa= input("Ingrese masa > ")
        
        # basicamente lo que hace es tomar los atributo validar y luego llama la clase, validad que el input que ingreso este en la lista
        self.valida = Pizza.validador(self.proteico,Pizza.proteicos) \
            and Pizza.validador(self.vegetal1,Pizza.verduras) \
            and Pizza.validador(self.vegetal2,Pizza.verduras) \
            and Pizza.validador(self.tipo_masa,Pizza.masa)