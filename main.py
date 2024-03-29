import tkinter
from tkinter import ttk ,font,END
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog,messagebox
import pyttsx3


#Definimos los eventos de los botones

def open_file():
    filepath = filedialog.askopenfilename(title="Selecione archivo",filetypes=(("archivo.txt","*.txt*"),("Todos","*.*")))
    if filepath != "":
        file = open(filepath,"r")
        contenido = file.read()
        text.delete("1.0",END)
        text.insert("0.0",contenido)
        window.title(filepath)

def start_read():
    text_read = text.get("1.0",END)
    voice = selec_voice.get()
    voices = engine.getProperty("voices")
    
    if voice == "Español":
        engine.setProperty("voice",voices[0].id)
    
    if voice == "Ingles":
        engine.setProperty("voice",voices[1].id)
    
    if len(text_read) >2:
        engine.say(text_read)
        engine.runAndWait()
        engine.stop()
    else:
        messagebox.showerror("Error","No hay texto para leer")

def speed_sound(event):
    level = int(scale_speed.get())
    engine.setProperty("rate",level)
    signal_speed["text"]=str(level)

def volume_sound(event):
    level = scale_volume.get()
    engine.setProperty("volume",round(level,2))
    signal_volume["text"]=str(round(level,2))

def save_sound():
    if len(text.get("1.0",END)) >2:
        name = text.get("1.0",END).split(" ")
        name = name[0:1][0]
        engine.save_to_file(text.get("1.0",END),f"{name}.mp3")
        engine.runAndWait()
        messagebox.showinfo("Aviso","Audio guardado correctamente")
    else:
        messagebox.showerror("Error","No hay texto para grabar")


#Creamos la ventana principal
window = tkinter.Tk()

window.geometry("600x400+400+100")

window.title("Texto a voz")

window.config(bg="#1F1F35")
window.minsize(500,300)
window.iconbitmap("assets/icon.ico")

#Inicializamos el modulo de voz
engine = pyttsx3.init("sapi5")

#Configuramos el grid de las columnas y filas
window.columnconfigure(0,weight=8)
window.columnconfigure(1,weight=1)
window.rowconfigure(0,weight=1)


#Asignamos las rutas de las imagenes a las variables
image_woman = tkinter.PhotoImage(file="assets/woman.png")
image_file = tkinter.PhotoImage(file="assets/file.png")
image_record = tkinter.PhotoImage(file="assets/record.png")


#Creamos y configuramos el frame que contendra todo el texto
frame_text = tkinter.Frame(window,bg="white",width=400,height=400)
frame_text.grid(column=0,row=0,sticky="NSEW",padx=5,pady=5)

frame_text.columnconfigure(0,weight=1)
frame_text.rowconfigure(0,weight=1)

frame_text.grid_propagate(0)

#Creamos y configuramos el frame que contendra todos los botones
frame_control = tkinter.Frame(window,bg="#1F1F35",width=200,height=400)
frame_control.grid(column=1,row=0,sticky="NSEW",padx=5,pady=5)

frame_control.columnconfigure([0,1],weight=1)
frame_control.rowconfigure([0,1,2,3,4,5,6,7,8],weight=1)
frame_control.grid_propagate(0)


#Agregamos un scrolltext al frame texto
text = ScrolledText(frame_text,font=("Corbel",12,"italic"),insertbackground="#AFEFED",bg="black",fg="#AFEFED")
text.grid(column=0,row=0,sticky="NSEW",)

#BOTONES

#Creamos un boton para abrir archivos
button_open = tkinter.Button(frame_control,image=image_file,compound="left",text="ABRIR ARCHIVO",bg="black",fg="#AFEFED",bd=0.5,cursor="Hand1",font=("Terminal",11,"bold"),command=open_file)
button_open.grid(column=0,row=0,columnspan=2,sticky="EW")

#Creamos un boton para leer el archivo
button_read = tkinter.Button(frame_control,image=image_woman,compound="left",text="LEER ARCHIVO",bg="black",fg="#AFEFED",bd=0.5,cursor="Hand1",font=("Terminal",11,"bold"),command=start_read)
button_read.grid(column=0,row=1,columnspan=2,sticky="EW")

#Creamos un boton para grabar y guardar el audio
button_grab = tkinter.Button(frame_control,image=image_record,compound="left",text="GRABAR AUDIO  ",bg="black",fg="#AFEFED",bd=0.5,cursor="Hand1",font=("Terminal",11,"bold"),command=save_sound)
button_grab.grid(column=0,row=2,columnspan=2,sticky="EW")

#Creamos la opcion de elegir un idioma de la voz 
tkinter.Label(frame_control,bg="#1F1F35",fg="#AFEFED",text="Idioma",font=("Terminal",11,"bold")).grid(columnspan=2,column=0,row=3,sticky="EW")

selec_voice = ttk.Combobox(frame_control,values=["Español","Ingles"],state="readonly")
selec_voice.grid(columnspan=2,column=0,row=4)
#seleccionamos por defecto el ingles
selec_voice.set("Ingles")

#Creamos una barra para controlar la velocidad de lectura del bot
tkinter.Label(frame_control,bg="#1F1F35",fg="#AFEFED",text="Velocidad",font=("Terminal",11,"bold")).grid(columnspan=2,column=0,row=5,sticky="EW")

scale_speed = ttk.Scale(frame_control,from_=150,to=350,command=speed_sound)
scale_speed.grid(column=0,row=6,sticky="EW")
signal_speed =tkinter.Label(frame_control,bg="#1F1F35",fg="#AFEFED",text="150",font=("Terminal",11,"bold"))
signal_speed.grid(column=1,row=6,sticky="EW")


#Creamos una barra para controlar el volumen del bot
tkinter.Label(frame_control,bg="#1F1F35",fg="#AFEFED",text="Volumen",font=("Terminal",11,"bold")).grid(columnspan=2,column=0,row=7,sticky="EW")

scale_volume = ttk.Scale(frame_control,from_=0,to=1,command=volume_sound)
scale_volume.grid(column=0,row=8,sticky="EW")

signal_volume =tkinter.Label(frame_control,bg="#1F1F35",fg="#AFEFED",text="1",font=("Terminal",11,"bold"))
signal_volume.grid(column=1,row=8,sticky="EW")

#Le damos un fondo negro al scale
style=ttk.Style()
style.configure("Horizontal.TScale",background="#1F1F35")

window.mainloop()