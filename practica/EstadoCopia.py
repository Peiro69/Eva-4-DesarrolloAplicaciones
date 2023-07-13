class EstadoCopia:
    def __init__(self,nombre_estadoCopia):
        self.__nombre_estadoCopia = nombre_estadoCopia

    def get_nombre_estadoCopia(self):
        return self.__nombre_estadoCopia
    def set_nombre_estadoCopia(self,nombre_estadoCopia):
        self.__nombre_estadoCopia = nombre_estadoCopia

    def get_id_estadoCopia(self):
        return self.__id_estadoCopia
    def set_id_estadoCopia(self,id_estadoCopia):
        self.__id_estadoCopia = id_estadoCopia