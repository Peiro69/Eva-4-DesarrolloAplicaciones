class TipoUsuario:
    def __init__(self,nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre
    def set_rut(self,nombre):
        self.__nombre = nombre

    def set_id_tipo_usuario(self,id_tipo_usuario):
        self.__id_tipo_usuario = id_tipo_usuario
    def get_id_tipo_usuario(self):
        return self.__id_tipo_usuario