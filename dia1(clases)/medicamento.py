class Medicamento():
    #Atributos
    descuento= 0.05
    IVA= 0.18
    
    @staticmethod
    def validad_mayor_a_cero(numero: int):
        return numero > 0
    
    
    #los metodos estaticos no pueden modificar los atributos de por si solos
    @staticmethod
    def modificar_atibuto():
        Medicamento.IVA= 0.19 #modifica la clase completa