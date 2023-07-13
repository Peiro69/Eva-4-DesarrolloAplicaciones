class Prestamo:
    def __init__(self,fecha_inicio,fecha_fin,fecha_real):
        self.__fecha_inicio = fecha_inicio
        self.__fecha_fin = fecha_fin
        self.__fecha_real = fecha_real

    def get_fecha_inicio(self):
        return self.__fecha_inicio
    def set_rut(self,fecha_inicio):
        self.__fecha_inicio = fecha_inicio

    def get_fecha_fin(self):
        return self.__fecha_fin
    def set_fecha_fin(self,fecha_fin):
        self.__fecha_fin = fecha_fin
            
    def get_fecha_real(self):
        return self.__fecha_real
    def set_fecha_real(self,fecha_real):
        self.__fecha_real = fecha_real

    def set_id_prestamo(self,id_prestamo):
        self.__id_prestamo = id_prestamo