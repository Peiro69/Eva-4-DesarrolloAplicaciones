class Copia:
    def __init__(self,cantidad,estado_copia,idlibro):
        self.__cantidad = cantidad
        self.__estado_copia = estado_copia
        self.__idlibro = idlibro

    def get_cantidad(self):
        return self.__cantidad
    def set_cantidad(self,cantidad):
        self.__cantidad = cantidad

    def get_idCopia (self):
        return self.__idCopia
    def set_idCopia(self,idCopia):
        self.__idCopia = idCopia

    def get_estado_copia(self):
        return self.__estado_copia
    def set_estado_copia(self,estado_copia):
        self.__estado_copia = estado_copia
    
    def get_idlibro(self):
        return self.__idlibro 
    def set_idlibro(self,idlibro):
        self.__libro = idlibro