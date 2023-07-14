from cProfile import label
from distutils.log import Log
from msilib.schema import ListBox
from tkinter import ttk
from Prestamo import Prestamo
from TipoUsuario import TipoUsuario
from Usuario import Usuario
from Libro import Libro
from Autor import Autor
from Copia import Copia
import tkinter
from tkinter import messagebox
from DAO import DAO




def ValidarEntero(campo:str,error:bool):
    if error == False:
        try:
            x = int(campo)
            if x > 0:
                return x
            else: 
                messagebox.showerror("Intente nuevamente","Se debe ingresar un numero valido")
                error = True
        except:
            messagebox.showerror("Intente nuevamente","Se debe ingresar un numero valido")
        
  

def RegistrarUsuarios():
    dao = DAO() 
    rut = cajitarut.get()
    #print(rut)
    nombre = cajitanombre.get()
    telefono = cajitatelefono.get()
    e_tipo_usuario = cajitatipo.get().lower()
    print(e_tipo_usuario)
    obj_tipo_usuario = TipoUsuario(e_tipo_usuario)
    print(obj_tipo_usuario.get_nombre())

    o_tipo_usuario = dao.recuperarIDtipo(obj_tipo_usuario)
    a_tipo_usuario = o_tipo_usuario[0]
    
    tipo_usuario = a_tipo_usuario[0]
    print(tipo_usuario)
    
    us = Usuario(rut,nombre,telefono,tipo_usuario)
    dao.registrarUsuario(us)

def RegistrarLibros_Autores_Copias():
    global id_libro
    
    titulo = cajitatitulo.get()
    error = False
    e_cant_autores = cajitac_autor.get()
    cant_autores = ValidarEntero(e_cant_autores,error)
    e_cantidad_copias = cajitacantidad.get()
    cantidad_copias = ValidarEntero(e_cantidad_copias,cant_autores==None)
    li = Libro(titulo)
    

    dao = DAO()
    
    id_libro = dao.registrarLibro(li)
    print(f"{id_libro} olaa" )
    ca = Copia(cantidad_copias,1,id_libro)
    
    dao.registrarCopia(ca)


    if cant_autores > 1:
        AsignacionAutores()
    elif cant_autores == 1:
        RegistroAutores(id_libro)
        

def RegistrarPrestamo():
    pass
    
def RegistrarAutor():
    global id_libro
    nombre_autor = cajitanombre_autor.get()
    apellido_autor = cajitaapellido_autor.get()
    au = Autor(nombre_autor,apellido_autor)
    dao = DAO()
    print(f"el nombre del autor es: {au.get_nombre()}  {au.get_apellido()}")
    print(f"hola: {cajitanombre_autor.get()}")
    id = dao.registrarAutor(au)
    dao.registroLibroAutor(id_libro,id)
    print(id)

def AsignarAutor(idautor):
    global id_libro

    dao = DAO()
    dao.registroLibroAutor(id_libro,idautor)

    pass




def LogIn():
    global ventana_login,cajita_admin,cajita_password

    ventana_login = tkinter.Tk()
    ventana_login.geometry("300x300")

    ventana_login.title("Log-in")
    titulo = ttk.Label(ventana_login,text="Inicio de Sesión")

    label1 = ttk.Label(ventana_login,text="Usuario")
    label2 = ttk.Label(ventana_login,text="Contraseña")
    
    label1.grid(row=1,column=2)
    label2.grid(row=2,column=2)

    
    cajita_admin = tkinter.Entry(ventana_login)
    cajita_password = tkinter.Entry(ventana_login,show="*")


    cajita_admin.grid(row=1,column=3)
    cajita_password.grid(row=2,column=3)
    
    boton = tkinter.Button(ventana_login, text="Ingresar",command=Menu)
    boton.grid(row=5,column=3)
    titulo.grid(row=0,column=3)
    ventana_login.mainloop()

def RegistroUsuario():
    global ventana_usuario, cajitarut,cajitanombre,cajitatelefono,cajitatipo,opciones

    ventana_menu.destroy()

    ventana_usuario = tkinter.Tk()
    ventana_usuario.geometry("300x300")

    ventana_usuario.title("Registro de Usuarios")
    titulo = ttk.Label(ventana_usuario,text="Registro de Usuarios")

    label1 = ttk.Label(ventana_usuario,text="Rut")
    label2 = ttk.Label(ventana_usuario,text="Nombre")
    label3 = ttk.Label(ventana_usuario,text="Telefono")
    label4 = ttk.Label(ventana_usuario,text="Tipo Usuario")

    label1.grid(row=1,column=2)
    label2.grid(row=2,column=2)
    label3.grid(row=3,column=2)
    label4.grid(row=4,column=2)


    cajitarut = tkinter.Entry(ventana_usuario)
    cajitanombre = tkinter.Entry(ventana_usuario)
    cajitatelefono = tkinter.Entry(ventana_usuario)
    opciones = ['Alumno','Profesor']
    cajitatipo = tkinter.StringVar()
    cajitatipo.set(opciones[0])
    electa = tkinter.OptionMenu(ventana_usuario,cajitatipo,*opciones)
    electa.grid(row=1,column=3)

    cajitarut.grid(row=1,column=3)
    cajitanombre.grid(row=2,column=3)
    cajitatelefono.grid(row=3,column=3)
    electa.grid(row=4,column=3)


    boton = tkinter.Button(ventana_usuario, text="Registro",command=RegistrarUsuarios)
    boton.grid(row=5,column=3)
    titulo.grid(row=0,column=3)

    ventana_usuario.mainloop()

def RegistroLibro():
    global ventana_libro, cajitatitulo,cajitac_autor,cajitacantidad

    ventana_menu.destroy()

    ventana_libro = tkinter.Tk()
    ventana_libro.geometry("300x300")

    ventana_libro.title("Registro de Libros")
    titulo = ttk.Label(ventana_libro,text="Registro de Libros")

    label1 = ttk.Label(ventana_libro,text="Titulo")
    label2 = ttk.Label(ventana_libro,text="Cantidad Autores")
    label3 = ttk.Label(ventana_libro,text="Cantidad Stock")

    label1.grid(row=1,column=2)
    label2.grid(row=2,column=2)
    label3.grid(row=3,column=2)


    cajitatitulo = tkinter.Entry(ventana_libro)
    cajitac_autor = tkinter.Entry(ventana_libro)
    cajitacantidad = tkinter.Entry(ventana_libro)


    cajitatitulo.grid(row=1,column=3)
    cajitac_autor.grid(row=2,column=3)
    cajitacantidad.grid(row=3,column=3)

    boton = tkinter.Button(ventana_libro, text="Registrar Libro",command=RegistrarLibros_Autores_Copias)
    boton.grid(row=5,column=3)
    titulo.grid(row=0,column=3)

    ventana_libro.mainloop()

def RegistroAutores(id_libro):
    global ventana_autor,cajitanombre_autor,cajitaapellido_autor

    ventana_libro.destroy()

    ventana_autor = tkinter.Tk()
    ventana_autor.geometry("300x300")

    ventana_autor.title("Registro de Autores")
    titulo = ttk.Label(ventana_autor,text="Registro de Autor")

    label1 = ttk.Label(ventana_autor,text="Nombre Autor")
    label2 = ttk.Label(ventana_autor,text="Apellido Autor")
    
    label1.grid(row=1,column=2)
    label2.grid(row=2,column=2)

    
    cajitanombre_autor = tkinter.Entry(ventana_autor)
    cajitaapellido_autor = tkinter.Entry(ventana_autor)


    cajitanombre_autor.grid(row=1,column=3)
    cajitaapellido_autor.grid(row=2,column=3)
    
    boton = tkinter.Button(ventana_autor, text="Registrar Autor",command=RegistrarAutor)
    boton.grid(row=5,column=3)
    titulo.grid(row=0,column=3)
    ventana_autor.mainloop()
    pass

def AsignacionAutores():
    global ventana_asignacion, listbox1, listbox2


    #ventana_libro.destroy()

    ventana_asignacion = tkinter.Tk()
    ventana_asignacion.title("Select")
    ventana_asignacion.geometry('500x300')

    listbox1 = tkinter.Listbox(ventana_asignacion)
    listbox1.grid(row=1,column=2)


    dao = DAO()
    a = dao.recuperarAutores()
    #print(type(a))
    i = 0
    for y in a:
        listbox1.insert(i+1,y)
        i += 1






    
    listbox2 = tkinter.Listbox(ventana_asignacion)
    listbox2.grid(row=1,column=6)


    def item_seleccionado():
        for item in listbox1.curselection():
            sel = listbox1.get(item)
            i = 0
            listbox2.insert(i+1,sel)
            i += 1

    def devolver_autor():
        listbox2.delete(tkinter.ANCHOR)


    boton_devolver = tkinter.Button(ventana_asignacion, text="Devolver Autor", command=devolver_autor)
    boton_devolver.grid(row=1,column=5)

    boton_asignar = tkinter.Button(ventana_asignacion, text="Asignar Autor", command= item_seleccionado)
    boton_asignar.grid(row=1,column=3)






    def tuplalb2(x):
        o = ""
        for a in x:
            for i in a:
                if i != " ":
                    o += i
                else:
                    break
        print(o)

    def uwu():
        x = listbox2.get(0,tkinter.END)
        for l in x:
            tuplalb2(l)





#WHERE NOMBRE = %S AND APELLIDO = %S
    


    boton_a = tkinter.Button(ventana_asignacion, text="Asignar Autor", command= uwu)
    boton_a.grid(row=3,column=4)

    ventana_asignacion.mainloop()

def RegistroPrestamo():

    ventana_menu.destroy()

    ventana_prestamo = tkinter.Tk()
    ventana_prestamo.geometry("300x300")

    ventana_prestamo.title("Menú Opciones")

    label1 = ttk.Label(ventana_prestamo,text="Prestamos")
    label1.grid(row=1,column=2)

    
    ventana_menu.mainloop()


def Menu():
    global ventana_menu

    ventana_login.destroy()

    ventana_menu = tkinter.Tk()
    ventana_menu.geometry("300x300")

    ventana_menu.title("Menú Opciones")

    boton_usuario = tkinter.Button(ventana_menu, text="Registrar Usuario",command=RegistroUsuario)
    boton_usuario.grid(row=5,column=3)

    boton_libro = tkinter.Button(ventana_menu, text="Registrar Libro",command=RegistroLibro)
    boton_libro.grid(row=5,column=4)

    boton_asig_prestamo = tkinter.Button(ventana_menu,text="Asignar Prestamo",command=RegistroPrestamo)
    boton_asig_prestamo.grid(row=5,column=5)

    ventana_menu.mainloop()




#dao = DAO()
#a = dao.recuperarAutores()
#print(type(a))
#for y in a:
#    print(y)
#    break


AsignacionAutores()

#LogIn()