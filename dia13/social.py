from dia13.anuncios import Anuncio

class Social(Anuncio):
    FORMATO= "Social"
    SUB_TIPOS= ("facebook","linkedin")
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    
    def comprimir_anuncio():
        pass
    
    def redimensionar_anuncio():
        pass