class Autor:
    def __init__(self,nombre,apellido):
        self.__nombre = nombre
        self.__apellido = apellido
        
    def get_id_autor(self):
        return self.__id_autor
    def set_id_autor(self,id_autor):
        self.__id_autor = id_autor

    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido
    def set_apellido(self,apellido):
        self.__apellido = apellido