class Medicamento():
    #Atributos
    descuento= 0.05
    IVA= 0.18
    
    @staticmethod
    def validad_mayor_a_cero(numero: int):
        return numero > 0
    
    #modifica la clase completa
    @staticmethod
    def modificar_atibuto():
        Medicamento.IVA= 0.19