import mysql.connector
import credenciales
from Prestamo import Prestamo
from TipoUsuario import TipoUsuario
from Usuario import Usuario
from Libro import Libro
from Autor import Autor
from Copia import Copia

class DAO:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None

    def conectar(self):
        self.__conexion = mysql.connector.connect(**credenciales.get_credenciales())
        self.__cursor = self.__conexion.cursor()
    
    def cerrar(self):
        self.__conexion.commit()
        self.__conexion.close()

    def registrarUsuario(self,u:Usuario):
        self.conectar()
        sql = "INSERT INTO usuario (Rut,Nombre,Telefono,Id_TipoUsuario) VALUES (%s,%s,%s,%s)"
        values = (u.get_rut() ,u.get_nombre(),u.get_telefono(),u.get_tipo_usuario())
        self.__cursor.execute(sql,values)
        id = self.__cursor.lastrowid
        self.cerrar()
        return id

    def registrarLibro(self,li:Libro):
        self.conectar()
        sql = "INSERT INTO libro (Titulo) VALUES (%s)"
        values = (li.get_titulo(),)
        self.__cursor.execute(sql,values)
        id = self.__cursor.lastrowid
        self.cerrar()
        return id

    def registrarAutor(self,au:Autor):
        self.conectar()
        print("autor:",au.get_nombre())
        sql = "INSERT INTO autor (Nombre,Apellido) VALUES (%s,%s)"
        values = (au.get_nombre(),au.get_apellido())
        self.__cursor.execute(sql,values)
        id = self.__cursor.lastrowid
        self.cerrar()
        return id

    def registroLibroAutor(self,idlibro,idautor):
        self.conectar()
        sql = "INSERT INTO libroautor (IdLibro,IdAutor) VALUES (%s,%s)"
        values = (idlibro,idautor)
        self.__cursor.execute(sql,values)
        self.cerrar()


    def registrarCopia(self,cop:Copia):
        self.conectar()
        sql = "INSERT INTO copia (Cantidad,Id_EstadoCopia,IdLibro) VALUES (%s,%s,%s)"
        values = (cop.get_cantidad(),cop.get_estado_copia(),cop.get_idlibro())
        self.__cursor.execute(sql,values)
        self.cerrar()


    def recuperarIDtipo(self,n_tipo:TipoUsuario):
        self.conectar()
        sql = "SELECT Id_TipoUsuario FROM tipousuario WHERE nombre = %s"
        values = (n_tipo.get_nombre(),)
        self.__cursor.execute(sql,values)
        ide = self.__cursor.fetchall()
        self.cerrar()
        return ide

    def recuperarAutores(self):
        self.conectar()
        sql = "SELECT * FROM autor"
        self.__cursor.execute(sql)
        o = self.__cursor.fetchall()
        lista = []
        for a in o:
            autor = Autor(a[1],a[2])
            autor.set_id_autor(a[0])
            #print(autor)
            lista.append(autor)
        self.cerrar()
        return lista


    
