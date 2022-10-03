#INTEGRANTES: 
"""Merary Julissa Araujo Velasquez"""
"""Nathaly Sarai Rodriguez Silva """

from tkinter import GROOVE, Label,Button, Tk,filedialog,messagebox
from PIL import Image,ImageTk,ImageFilter

class cargar():
   
    def __init__(self):
        self.archivo = ""
        self.size = (300,300)

#metodo cargar, para cargar la imagen 
    def cargar_metodo(self):
        self.archivo = filedialog.askopenfilename(title="Elija una imagen",filetypes=(("jpg file","*.jpg"),("png files","*.png"),("all files","*.*")))
        try:
            imagen2 = Image.open(self.archivo)
            imagen2resiz = imagen2.resize(self.size,Image.Resampling.LANCZOS)
            render2 = ImageTk.PhotoImage(imagen2resiz)
            imagen.configure(image=render2)
            imagen.image = render2
        except:
            messagebox.showerror("Cargar imagen","Seleccione una imagen jpg. POR ¡FAVOR!")

#Metodo de filtro de imagen destallada

    def Resaltar(self):
        if self.archivo !="":
            imagen3 = Image.open(self.archivo)
            filtro1 = imagen3.filter(ImageFilter.EMBOSS)
            image3resiz = filtro1.resize(self.size,Image.Resampling.LANCZOS)
            render3 = ImageTk.PhotoImage(image3resiz)
            imagen.configure(image=render3)
            imagen.image = render3
            filtro1.save("Imagen Destallada.jpg")
            messagebox.showinfo("Cargar imagen","Se aplicó el filtro de resaltar.")
        else:
            messagebox.showerror("Cargar imagen","Seleccione una imagen jpg. POR ¡FAVOR!")

    #metodo de filtro de desenfoque

    def desenfoque(self):
        if self.archivo !="":
            imagen3 = Image.open(self.archivo)
            filtro2 = imagen3.filter(ImageFilter.BLUR)
            image3resiz = filtro2.resize(self.size,Image.Resampling.LANCZOS)
            render3 = ImageTk.PhotoImage(image3resiz)
            imagen.configure(image=render3)
            imagen.image = render3
            filtro2.save("Imagen con desenfoque.jpg")
            messagebox.showinfo("Cargar imagen","Se aplicó el filtro de desenfoque.")
        else:
            messagebox.showerror("Cargar imagen","Seleccione una imagen jpg. POR ¡FAVOR!")

#metodo de contorno

    def contorno(self):
        if self.archivo !="":
            imagen3 = Image.open(self.archivo)
            filtro3 = imagen3.filter(ImageFilter.CONTOUR)
            image3resiz = filtro3.resize(self.size,Image.Resampling.LANCZOS)
            render3 = ImageTk.PhotoImage(image3resiz)
            imagen.configure(image=render3)
            imagen.image = render3
            filtro3.save("Imagen con contorno.jpg")
            messagebox.showinfo("Cargar imagen","Se aplicó el contorno a la imagen.")
        else:
            messagebox.showerror("Cargar imagen","Seleccione una imagen jpg. POR ¡FAVOR!")
            
#metodo de filtro en blanco negro
    def blanco_y_negro(self):
        if self.archivo !="":
            imagen4 = Image.open(self.archivo)
            imagenbn = imagen4.convert("L")
            imagenbnresiz = imagenbn.resize(self.size,Image.Resampling.LANCZOS)
            render4 = ImageTk.PhotoImage(imagenbnresiz)
            imagen.configure(image=render4)
            imagen.image = render4
            imagenbn.save("Imagen en blanco y negro.jpg")
            messagebox.showinfo("Cargar imagen","Se aplicó el efecto Blanco y negro.")
        else:
            messagebox.showerror("Cargar imagen", "Seleccione una imagen jpg. POR ¡FAVOR!")


#formulario principal

ventana = Tk()
clase1 = cargar() #llamdao a la clase cargar
#definicion de dimensiones
ancho_ventana = 550
alto_ventana = 500

x_ventana = ventana.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = ventana.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
ventana.geometry(posicion)
ventana.title("Imagen con filtros")
ventana.configure(background='LightPink')
ventana.resizable(0,0)

#mostrar controles, textos y mensajes definidos

txt0 = Label(ventana,text="Cargar imagenes ",bg='LightPink',font='arial 16 bold')
txt0.pack()
imagen = Label(ventana,image="",bg='LightPink',relief=GROOVE,border=10)
imagen.place(x = 40,y = 40,width=300,height=300)
btnCargar = Button(ventana,command=clase1.cargar_metodo,text="Cargar Imagen")
btnCargar.place(x = 370,y = 150,width = 150,height = 40)
btnblancoNegro = Button(ventana,command=clase1.blanco_y_negro,text="Blanco/Negro")
btnblancoNegro.place(x = 40,y = 400,width = 100,height = 40)
btnDesenfoque = Button(ventana,command=clase1.desenfoque,text="Desenfoque")
btnDesenfoque.place(x = 150,y = 400,width = 100,height = 40)
btnContorno = Button(ventana,command=clase1.contorno,text="Contorno")
btnContorno.place(x = 260,y = 400,width = 100,height = 40)
btnResaltar = Button(ventana,command=clase1.Destallar,text="Resaltar")
btnResaltar.place(x = 370,y = 400,width = 100,height = 40)
ventana.mainloop()