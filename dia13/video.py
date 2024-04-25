from dia13.anuncios import Anuncio

class Video(Anuncio):
    FORMATO= "Video"
    SUB_TIPOS= ("instream","outstream")
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo, duracion=5):
        
        self.__ancho= 1
        self.__alto= 1
        self.__duracion= duracion
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    
    def comprimir_anuncio():
        return f"COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN"
    
    def redimensionar_anuncio():
        return f"RECORTE DE VIDEO NO IMPLEMENTADO AÚN"
    
    #GETTER Y SETTER DE ANCHO
    @property
    def ancho(self):
        return self.__ancho
    
    #GETTER Y SETTER DE ALTO
    @property
    def alto(self):
        return self.__alto
    
    #GETTER Y SETTER DE DURACION
    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self, duracion):
        if duracion > 0:
            self.__duracion=duracion
        return