from dia13.anuncios import Anuncio

class Display(Anuncio):
    FORMATO= "Display"
    SUB_TIPOS= ("tradicional","native")
    
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)
    
    def comprimir_anuncio():
        pass
    
    def redimensionar_anuncio():
        pass