"""
Clase abstracta
Clase componente  de campaña
"""
from subtipoinvalidoerror import SubTipoInvalidoError
from abc import ABC, abstractmethod

class Anuncio(SubTipoInvalidoError,ABC):
    
    def __init__(self, url_archivo, url_clic, sub_tipo,ancho=1, alto=1):
        self.__ancho=ancho
        self.__alto=alto
        self.__url_archivo=url_archivo
        self.__url_clic:url_clic
        self.__sub_tipo:sub_tipo
        
        # super().__init__(*args)
    
    def mostrar_formato():
        pass
    
    @abstractmethod
    def comprimir_anuncio(self): #abstracta
        pass
    
    @abstractmethod
    def redimensionar_anuncio(self ): #abstracta
        pass
    
    #GETTER Y SETTER DE ANCHO
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if ancho > 0:
            self.__ancho= ancho
        return 
    
    #GETTER Y SETTER DE ALTO
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        if alto > 0:
            self.__alto= alto
        return 
    
    #GETTER Y SETTER DE url_archivo
    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self):
        pass
    
    #GETTER Y SETTER DE url_clic
    @property
    def url_clic(self):
        return self.__url_clic
    
    @url_clic.setter
    def url_clic(self):
        pass

if __name__ == "__main__":
    
    anuncio=Anuncio(url_archivo="htpps//...", url_clic="click",sub_tipo="tiposo",ancho=9,alto=5)
    print(f"el ancho de la publicacion a sido cambiado a: {anuncio.ancho} y el alto a cambiado a: {anuncio.alto}")