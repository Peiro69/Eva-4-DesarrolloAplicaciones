class Libro:
    def __init__(self,titulo):
        self.__titulo = titulo

    def get_id_libro(self):
        return self.__id_libro
    def set_id_libro(self,id_libro):
        self.__id_libro = id_libro

    def get_titulo(self):
        return self.__titulo
    def set_titulo(self,titulo):
        self.__titulo = titulo