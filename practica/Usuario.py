from TipoUsuario import TipoUsuario

class Usuario:
    def __init__(self,rut,nombre,telefono,tipo_usuario):
        self.__rut = rut
        self.__nombre = nombre
        self.__telefono = telefono
        self.__tipo_usuario = tipo_usuario
    
    def get_rut(self):
        return self.__rut
    def set_rut(self,rut):
        self.__rut = rut
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre

    def get_telefono(self):
        return self.__telefono
    def set_telefono(self,telefono):
        self.__telefono = telefono
    
    def get_tipo_usuario(self):
        return self.__tipo_usuario
    def set_tipo_usuario(self,tipo_usuario):
        self.__tipo_usuario = tipo_usuario
    