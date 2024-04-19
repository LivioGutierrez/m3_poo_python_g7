"""
class MisExecepciones(Exception):

    def imprimir_promedio(self, dividendo, divisor):
        promedio=dividendo/divisor#ZeroDivisionError: division by zero
        print(f"el promedio es: {promedio}")

calculo_promedio= MisExecepciones()

calculo_promedio.imprimir_promedio(100,0)
"""
class Error(Exception):
    pass
class DivisorError(Error):
    def __init__(self, mensaje, divisor):
        self.divisor = divisor
        self.mensaje= mensaje

class MisExecepciones(Exception):

    def imprimir_promedio(self, dividendo, divisor):
        try:
            promedio=dividendo/divisor#ZeroDivisionError: division by zero
            print(f"el promedio es: {promedio}")
        #Captura generica de una excepcion
        except Exception as error:
            print(f"Se ha producido un error: {error}")#Se ha producido un error: division by zero
        finally:
            print("Gracias por participar en clases")
    
calculo_promedio= MisExecepciones()
valido=True

while valido:
    try:
        dividendo= int(input("Ingrese el numero dividendo: "))
        valido= False
    except ValueError:
        print("Error en el ingreso de datos")
    
valido=True
while valido:
    try:
        divisor= int(input("Ingrese el numero divisor: "))
        if divisor == 0:
            raise DivisorError("Divisor no puede ser cero",divisor)
        valido= False
    except DivisorError as dError:
        print(f"Error en el ingreso del divisor: {dError}")
    
    #Captura espesifica de una excepcion
    except ZeroDivisionError:
            print(f"El divisor no puede ser un cero")
    
    except ValueError:
        print("Error en el ingreso del divisor")

calculo_promedio.imprimir_promedio(dividendo,divisor)

