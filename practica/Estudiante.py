from Usuario import Usuario

class Alumno(Usuario):
    
    def __init__(self,rut,nombre,telefono,tipo_usuario,cantidad_libros) :
        super().__init__(rut,nombre,telefono,tipo_usuario)
        self.__cantidad_libros = cantidad_libros

    def get_cantidad(self):
        return self.__cantidad_libros
    def set_cantidad(self,cantidad_libros):
        self.__cantidad_libros = cantidad_libros