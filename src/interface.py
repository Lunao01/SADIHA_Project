# Librerías
from tkinter import *
from tkinter import messagebox, Canvas
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os


"""
    Class name: interface
    Function:   El objetivo de esta clase es implementar una interfaz funcional que permita comunicarnos con el usuario y mostrar los resultados 
                del archivo SADIHA.pl, el programa de inferencia escrito en Prolog.
"""



###############################################################################################################################
#   Variables                                                                                                                 #
###############################################################################################################################
tiene_sombrero = -1 
tamano_sombrero = ""
forma_sombrero = ""
color_sombrero = ""
superficie_sombrero = ""
forma_carpoforo = ""
color_carpoforo = ""
superficie_carpoforo = ""
tipo_himenio = ""
color_himenio = ""
tipo_laminas = ""
tiene_pie = -1
pie_con_anillo = -1
color_pie = ""
tipo_pie = ""

# En las variables de sí/no -1 = no inicializada   0 = no   1 = sí


###############################################################################################################################
#   Listas de elementos                                                                                                       #
###############################################################################################################################
elementos = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5", "Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4", "Elemento 5"]






###############################################################################################################################
#   Métodos                                                                                                                   #
###############################################################################################################################

"""
    Method name:   click_search 
    Function:      Método que activa el botón buscar seta, el objetivo es ocultar frame root y mostrar la interfaz para buscar la seta
"""
def click_search():
    root_frame.forget() # Se oculta el frame de las opciones principales
    search_frame.place(x = 0, y = 0) # Se muestra el nuevo frame
    vertical_line_1.place(x = 370, y = 120) # Frame para línea vertical 1
    vertical_line_2.place(x = 740, y = 120) # Frame para línea vertical 2
    horizontal_line.place(x = 405, y = 300) # Frame para línea vertical 1
    l_img_root.destroy() # Se elimina la imagen del menú principal


"""
    Method name:   exit 
    Function:      Método para salir de la aplicación.
"""
def exit():
    if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir?"):
        root.quit()


"""
    Method name:   search_mushroom
    Function:      Método para buscar la seta dada una descripción por el usuario.
"""
def search_mushroom():
    print("Buscando:")





# Definir ventana
root = Tk() 
root.title("SADIHA") 
root.geometry("1100x600") 
root.configure(bg = "#fff")
root.resizable(False, False)    



###############################################################################################################################
#   Frame root (menú con opciones principales)                                                                                #
###############################################################################################################################
# Se crea frame para elementos de la interfaz
root_frame = Frame(root, width=700, height=700, bg = "white")
# Mostramos el frame root
root_frame.place(x = 430, y = 45)

# Subtítulo - ¿Qué desea hacer?
subtitle_root = Label(root_frame, text="¿Qué desea hacer?", fg="black", bg="white", font=('Microsoft YaHei UI Light', 35, "bold"))
subtitle_root.place(x = 145, y = 0)


# Cargar imagen menú
img_root = PhotoImage(file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "icon_SADIHA.png"))
img_root = img_root.subsample(2) # Redimension de imagen
l_img_root = Label(root, image = img_root, bg = "white")
l_img_root.place(x = 20, y = 57) # Mostramos la imagen

#################################### Botón Buscar seta
# Cargar la imagen
start_icon = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "buscar_seta.png"))  # Icono para el botón
start_icon = start_icon.resize((210, 210), Image.ADAPTIVE)  # Redimensionar la imagen 
imagen_start = ImageTk.PhotoImage(start_icon)

# Crear el botón con la imagen
start_button = Button(root_frame, image=imagen_start, compound="left", background= "#837F8A", command=click_search)
start_button.pack(padx=10, pady=10)
start_button.place(x = 140 , y = 75)


#################################### Botón Taxonomia
# Cargar la imagen
taxonomy_icon = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "taxonomia.png"))  # Icono para el botón
taxonomy_icon = taxonomy_icon.resize((210, 210), Image.ADAPTIVE)  # Redimensionar la imagen 
imagen_taxonomy = ImageTk.PhotoImage(taxonomy_icon)

# Crear el botón con la imagen
taxonomy_button = Button(root_frame, image=imagen_taxonomy, compound="left", background= "#937C8C")
taxonomy_button.pack(padx=10, pady=10)
taxonomy_button.place(x = 360 , y = 75)

#################################### Botón Info
# Cargar la imagen
info_icon = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "informacion.png"))  # Icono para el botón
info_icon = info_icon.resize((210, 210), Image.ADAPTIVE)  # Redimensionar la imagen 
imagen_info = ImageTk.PhotoImage(info_icon)

# Crear el botón con la imagen
info_button = Button(root_frame, image=imagen_info, compound="left", background= "#A27A8E")
info_button.pack(padx=10, pady=10)#D1B0AD
info_button.place(x = 140 , y = 295)


#################################### Botón Salir
# Cargar la imagen
exit_icon = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "salir.png"))  # Icono para el botón
exit_icon = exit_icon.resize((210, 210), Image.ADAPTIVE)  # Redimensionar la imagen 
imagen_exit = ImageTk.PhotoImage(exit_icon)

# Crear el botón con la imagen
exit_button = Button(root_frame, image=imagen_exit, compound="left", background= "#B17890", command=exit)
exit_button.pack(padx=10, pady=10)
exit_button.place(x = 360 , y = 295)
                


###############################################################################################################################
#   Frame buscar seta (menú para buscar una seta)                                                                             #
###############################################################################################################################
# Se crea frame para elementos de la interfaz
search_frame = Frame(root, width=1100, height=600, bg = "white")

# Subtítulo - ¿Qué desea hacer?
subtitle_search = Label(search_frame, text="Describa la seta:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 28, "bold"))
subtitle_search.place(x = 20, y = 20)

# Líneas verticales
vertical_line_1 = Frame(root, width=2, height=400, bg="black")
vertical_line_2 = Frame(root, width=2, height=400, bg="black")
horizontal_line = Frame(root, width=300, height=2, bg="black")





#########################################
#   Sombrero                            #
#########################################

# ¿Tiene sombrero?
subtitle_tiene_sombrero = Label(search_frame, text="¿Tiene sombrero?", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_tiene_sombrero.place(x = 40, y = 80)

si_tiene_sombrero = Radiobutton(search_frame, text="Sí", variable=tiene_sombrero, value=1, font=('Microsoft YaHei UI Light', 12))
si_tiene_sombrero.place(x=50, y=120)
no_tiene_sombrero = Radiobutton(search_frame, text="No", variable=tiene_sombrero, value=0, font=('Microsoft YaHei UI Light', 12))
no_tiene_sombrero.place(x=120, y=120)


# Tamaño del sombrero (diámetro)
subtitle_tamano_sombrero = Label(search_frame, text="Tamaño del sombrero (Diámetro):", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_tamano_sombrero.place(x = 40, y = 180)
subtitle_cm = Label(search_frame, text="cm", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_cm.place(x = 170, y = 215)

text_box_tamano_sombrero = Entry(search_frame, width= 20)
text_box_tamano_sombrero.place(x=40, y=220)


# Forma del sombrero
subtitle_forma_sombrero = Label(search_frame, text="Forma del sombrero:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_forma_sombrero.place(x = 40, y = 280)

combox_forma_sombrero = Combobox(search_frame, values=elementos)
combox_forma_sombrero.place(x=40, y=315)


# Color del sombrero
subtitle_color_sombrero = Label(search_frame, text="Color del sombrero:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_color_sombrero.place(x = 40, y = 370)

combox_color_sombrero = Combobox(search_frame, values=elementos)
combox_color_sombrero.place(x=40, y=405)


# Superficie del sombrero
subtitle_superficie_sombrero = Label(search_frame, text="Superficie del sombrero:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_superficie_sombrero.place(x = 40, y = 460)

combox_superficie_sombrero = Combobox(search_frame, values=elementos)
combox_superficie_sombrero.place(x=40, y=495)


#########################################
#   Carpóforo                           #
#########################################
# Forma del carpoforo
subtitle_forma_carpoforo = Label(search_frame, text="Forma del carpóforo:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_forma_carpoforo.place(x = 430, y = 30)

combox_forma_carpoforo = Combobox(search_frame, values=elementos)
combox_forma_carpoforo.place(x=430, y=65)


# Color del carpoforo
subtitle_color_carpoforo = Label(search_frame, text="Color del carpóforo:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_color_carpoforo.place(x = 430, y = 120)

combox_color_carpoforo = Combobox(search_frame, values=elementos)
combox_color_carpoforo.place(x=430, y=155)


# Superficie del carpoforo
subtitle_superficie_carpoforo = Label(search_frame, text="Superficie del carpóforo:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_superficie_carpoforo.place(x = 430, y = 210)

combox_superficie_carpoforo = Combobox(search_frame, values=elementos)
combox_superficie_carpoforo.place(x=430, y=245)



#########################################
#   Himenio                             #
#########################################

# Tipo de himenio
subtitle_tipo_himenio = Label(search_frame, text="Tipo de himenio:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_tipo_himenio.place(x = 430, y = 320)

combox_tipo_himenio = Combobox(search_frame, values=elementos)
combox_tipo_himenio.place(x=430, y=355)


# Color de himenio
subtitle_color_himenio = Label(search_frame, text="Color de himenio:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_color_himenio.place(x = 430, y = 410)

combox_color_himenio = Combobox(search_frame, values=elementos)
combox_color_himenio.place(x=430, y=445)


# Tipo de láminas
subtitle_tipo_laminas = Label(search_frame, text="Tipo de láminas:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_tipo_laminas.place(x = 430, y = 500)

combox_tipo_laminas = Combobox(search_frame, values=elementos)
combox_tipo_laminas.place(x=430, y=535)



#########################################
#   Pie                                 #
#########################################

# ¿Tiene pie?
subtitle_tiene_pie = Label(search_frame, text="¿Tiene pie?", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_tiene_pie.place(x = 820, y = 30)

si_tiene_pie = Radiobutton(search_frame, text="Sí", variable=tiene_pie, value=1, font=('Microsoft YaHei UI Light', 12))
si_tiene_pie.place(x=830, y=70)
no_tiene_pie = Radiobutton(search_frame, text="No", variable=tiene_pie, value=0, font=('Microsoft YaHei UI Light', 12))
no_tiene_pie.place(x=900, y=70)


# ¿Pie con anillo?
subtitle_pie_con_anillo = Label(search_frame, text="¿Pie con anillo?", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_pie_con_anillo.place(x = 820, y = 130)

si_pie_con_anillo = Radiobutton(search_frame, text="Sí", variable=pie_con_anillo, value=1, font=('Microsoft YaHei UI Light', 12))
si_pie_con_anillo.place(x=830, y=170)
no_pie_con_anillo = Radiobutton(search_frame, text="No", variable=pie_con_anillo, value=0, font=('Microsoft YaHei UI Light', 12))
no_pie_con_anillo.place(x=900, y=170)


# Color de pie
subtitle_color_pie = Label(search_frame, text="Color de pie:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_color_pie.place(x = 820, y = 230)

combox_color_pie = Combobox(search_frame, values=elementos)
combox_color_pie.place(x=820, y=265)


# Color de pie
subtitle_tipo_pie = Label(search_frame, text="Tipo de pie:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_tipo_pie.place(x = 820, y = 320)

combox_tipo_pie = Combobox(search_frame, values=elementos)
combox_tipo_pie.place(x=820, y=355)



#########################################
#       Botones                         #
#########################################
# Botón de búsqueda
button_search_mushroom = Button(search_frame, text="Buscar", command=search_mushroom, font=('Microsoft YaHei UI Light', 18))
button_search_mushroom.place(x=985, y=530)
# Botón para cancelar
button_search_mushroom = Button(search_frame, text="Cancelar", font=('Microsoft YaHei UI Light', 18))
button_search_mushroom.place(x=865, y=530)



root.mainloop() # Loop de la ventana
root.quit() # Liberar recursos cuando se cierre la ventana
