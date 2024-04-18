# Librerías
from tkinter import *
from tkinter import messagebox, Canvas
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os
import webbrowser


"""
    Class name: interface
    Function:   El objetivo de esta clase es implementar una interfaz funcional que permita comunicarnos con el usuario y mostrar los resultados 
                del archivo setasExper.pl, el programa de inferencia escrito en Prolog.
"""


###############################################################################################################################
#   Métodos                                                                                                                   #
###############################################################################################################################
#########################################
#   Root frame                          #
#########################################

"""
    Method name:   click_search 
    Function:      Método que activa el botón buscar seta, el objetivo es ocultar frame root y mostrar la interfaz para buscar la seta
"""
def click_search():
    root_frame.place_forget() # Se oculta el frame de las opciones principales
    search_frame.place(x = 0, y = 0) # Se muestra el frame de búsqueda de setas
    vertical_line_1.place(x = 370, y = 120) # Frame para línea vertical 1
    vertical_line_2.place(x = 740, y = 120) # Frame para línea vertical 2
    horizontal_line.place(x = 405, y = 300) # Frame para línea vertical 1

"""
    Method name:   click_information 
    Function:      Método que activa el botón Información, con el objetivo de acceder a una ventana donde se explique el objetivo del proyecto
"""
def click_taxonomy():
    root_frame.place_forget() # Se oculta el frame de las opciones principales
    taxonomy_frame.place(x = 0, y = 0) # Se muestra el frame para mostrar la taxonomía seguida al usuario



"""
    Method name:   click_information 
    Function:      Método que activa el botón Información, con el objetivo de acceder a una ventana donde se explique el objetivo del proyecto
"""
def click_information():
    root_frame.place_forget() # Se oculta el frame de las opciones principales
    information_frame.place(x = 0, y = 0) # Se muestra el frame para la información del proyecto


"""
    Method name:   exit 
    Function:      Método para salir de la aplicación.
"""
def exit():
    if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir?"):
        root.quit()



#########################################
#   Search frame                        #
#########################################
"""
    Method name:   search_mushroom
    Function:      Método para buscar la seta dada una descripción por el usuario.
"""
def search_mushroom():
    number = text_box_tamano_sombrero.get()
    forma_sombrero = combox_forma_sombrero.get()
    color_sombrero = combox_color_sombrero.get()
    superficie_sombrero = combox_superficie_sombrero.get()
    forma_carpoforo = combox_forma_carpoforo.get()
    color_carpoforo = combox_color_carpoforo.get()
    superficie_carpoforo =  combox_superficie_carpoforo.get()
    tipo_himenio = combox_tipo_himenio.get()
    color_himenio = combox_color_himenio.get()
    tipo_laminas = combox_tipo_laminas.get()
    color_pie = combox_color_pie.get()
    tipo_pie = combox_tipo_pie.get()

    if tiene_sombrero.get() == 1: # Sí tiene sombrero
        # Comprobamos primero si el usuario ha completado bien los valores correspondientes al sombrero 
        if not(forma_sombrero == "" or color_sombrero == "" or superficie_sombrero == "" or number == ""):
             # Verifica si el valor del tamaño del sombrero es positivo mayor que 0
            try:
                tamano_sombrero = float(number) # El tamaño del sombrero puede ser float
                if tamano_sombrero > 0: # El tamaño del sombrero debe ser positivo
                    a = tipo_himenio == "laminado"
                    b = tipo_laminas != ""
                    # Se comprueban los valores relacionados con el himenio
                    if not(tipo_himenio == "" or color_himenio == "") and ((a and b) or (not a and not b)):
                        # Se comprueban los valores relacionados con el pie (si tiene pie claro)
                        if tiene_pie.get() == 1 and (color_pie == "" or tipo_pie == ""):
                            messagebox.showinfo("Mensaje", "Complete todos los campos correctamente.")
                        else:
                            print("CORRECTISIMO") # AQUI VA LA LLAMADA AL MÉTODO PARA EL CÁLCULO CON PROLOG
                    else:
                        messagebox.showinfo("Mensaje", "Complete todos los campos correctamente.")
                else:
                    messagebox.showinfo("Mensaje", "El tamaño del sombrero debe ser un valor numérico positivo.")
            except ValueError:
                messagebox.showinfo("Mensaje", "El tamaño del sombrero debe ser un valor numérico positivo.")
        else:
            messagebox.showinfo("Mensaje", "Complete todos los campos correctamente.")
    else: # No tiene sombrero
        # Se comprueban los valores relacionados con el carpóforo
        if not(forma_carpoforo == "" or color_carpoforo == "" or superficie_carpoforo == ""):
            a = tipo_himenio == "laminado"
            b = tipo_laminas != ""
            # Se comprueban los valores relacionados con el himenio
            if not(tipo_himenio == "" or color_himenio == "") and ((a and b) or (not a and not b)):
                # Se comprueban los valores relacionados con el pie (si tiene pie claro)
                if tiene_pie.get() == 1 and (color_pie == "" or tipo_pie == ""):
                    messagebox.showinfo("Mensaje", "Complete todos los campos correctamente.")
                else:
                    print("CORRECTISIMO") # AQUI VA LA LLAMADA AL MÉTODO PARA EL CÁLCULO CON PROLOG
            else:
                messagebox.showinfo("Mensaje", "Complete todos los campos correctamente.")
        else:
            messagebox.showinfo("Mensaje", "Complete todos los campos correctamente.")



"""
    Method name:   cancel_search_mushroom
    Function:      Método para cancelar la búsqueda de setas y volver al menú principal.
"""
def cancel_search_mushroom():
    if messagebox.askokcancel("Confirmación", "¿Está seguro de que desea cancelar la búsqueda?"):
        search_frame.place_forget() # Se oculta el frame de búsqueda de setas
        vertical_line_1.place_forget() # Frame para línea vertical 1
        vertical_line_2.place_forget() # Frame para línea vertical 2
        horizontal_line.place_forget() # Frame para línea vertical 1
        root_frame.place(x = 0, y = 0) # Se muestra el frame de las opciones principales
    else:
       messagebox.showinfo("Mensaje", "Operación cancelada.")
 
"""
    Method name:   click_si_tiene_sombrero
    Function:      Método para activar/desactivar los campos si el usuario selecciona que la seta a buscar sí tiene sombrero.
"""
def click_si_tiene_sombrero():
    # Sombrero
    text_box_tamano_sombrero.config(state="normal")
    combox_forma_sombrero.config(state="enabled")
    combox_color_sombrero.config(state="enabled")
    combox_superficie_sombrero.config(state="enabled")

    # Carpóforo
    combox_forma_carpoforo.config(state="disabled")
    combox_color_carpoforo.config(state="disabled")
    combox_superficie_carpoforo.config(state="disabled")
    combox_forma_carpoforo.set("")
    combox_color_carpoforo.set("")
    combox_superficie_carpoforo.set("")

"""
    Method name:   click_no_tiene_sombrero
    Function:      Método para activar/desactivar los campos si el usuario selecciona que la seta a buscar no tiene sombrero.
"""
def click_no_tiene_sombrero():
    # Sombrero
    text_box_tamano_sombrero.delete(0, "end")
    text_box_tamano_sombrero.insert(0, "") 
    text_box_tamano_sombrero.config(state="disabled")
    combox_forma_sombrero.config(state="disabled")
    combox_color_sombrero.config(state="disabled")
    combox_superficie_sombrero.config(state="disabled")
    combox_forma_sombrero.set("")
    combox_color_sombrero.set("")
    combox_superficie_sombrero.set("")

    # Carpóforo
    combox_forma_carpoforo.config(state="enabled")
    combox_color_carpoforo.config(state="enabled")
    combox_superficie_carpoforo.config(state="enabled")



"""
    Method name:   accion_seleccion_himenio_laminado
    Function:      Método para activar/desactivar el tipo de láminas. Solo se activa si el tipo de himenio es laminado.
"""
def accion_seleccion_himenio_laminado(event):
    v = combox_tipo_himenio.get()
    if v == "laminado":
        combox_tipo_laminas.config(state="ensabled")
    else:
        combox_tipo_laminas.config(state="disabled")
        combox_tipo_laminas.set("")


"""
    Method name:   click_si_tiene_pie
    Function:      Método para activar/desactivar los campos si el usuario selecciona que la seta a buscar sí tiene pie.
"""
def click_si_tiene_pie():
    si_pie_con_anillo.config(state="normal")
    no_pie_con_anillo.config(state="normal")
    combox_color_pie.config(state="enabled")
    combox_tipo_pie.config(state="enabled")

"""
    Method name:   click_no_tiene_pie
    Function:      Método para activar/desactivar los campos si el usuario selecciona que la seta a buscar no tiene pie.
"""
def click_no_tiene_pie():
    si_pie_con_anillo.config(state="disabled")
    no_pie_con_anillo.config(state="disabled")
    combox_color_pie.config(state="disabled")
    combox_tipo_pie.config(state="disabled")
    combox_color_pie.set("")
    combox_tipo_pie.set("")




#########################################
#   Information frame                   #
#########################################
"""
    Method name:   go_back_information
    Function:      Método para volver al menú principal desde la ventana de información.
"""
def go_back_information():
    root_frame.place(x = 0, y = 0) # Se muestra el frame de las opciones principales
    information_frame.place_forget() # Se oculta el frame para la información del proyecto


#########################################
#   Taxonomy frame                      #
#########################################
"""
    Method name:   go_back_taxonomy
    Function:      Método para volver al menú principal desde la ventana de taxonomia.
"""
def go_back_taxonomy():
    root_frame.place(x = 0, y = 0) # Se muestra el frame de las opciones principales
    taxonomy_frame.place_forget() # Se oculta el frame para la taxonomía del proyecto


"""
    Method name:   open_pdf
    Function:      Método para abrir los respectivos documentos taxonómicos.
"""
def open_pdf():
    ruta_pdf = os.path.join(os.path.dirname(os.path.abspath(__file__)), "taxonomy", listbox.get(listbox.curselection()) + ".pdf") 
    try:
        webbrowser.open(ruta_pdf)
    except OSError:
        print("No se pudo abrir el archivo PDF.")


"""
    Method name:   open_link_1
    Function:      Método para abrir la fuente del primer link.
"""
def open_link_1(event):
    webbrowser.open("https://taxateca.com/claseagaricomycetes.html")


"""
    Method name:   open_link_2
    Function:      Método para abrir la fuente del segundo link.
"""
def open_link_2(event):
    webbrowser.open("https://www.fungipedia.org/")


# Definir ventana de la aplicación
root = Tk() 
root.title("SADIHA") 
root.geometry("1100x600") 
root.configure(bg = "#fff")
root.resizable(False, False)    



###############################################################################################################################
#   Variables                                                                                                                 #
###############################################################################################################################
tiene_sombrero = IntVar()
tiene_sombrero.set(1)
tamano_sombrero = 0
tiene_pie = IntVar()
tiene_pie.set(1)
pie_con_anillo = IntVar()
pie_con_anillo.set(1)


###############################################################################################################################
#   Listas de elementos                                                                                                       #
###############################################################################################################################
list_orden = ["Resumen", "Agaricales", "Auriculariales","Boletales", "Polyporales", "Thelephorales", "Cantharellales"]
list_forma_sombrero = ["convexo", "plano", "coraloide", "centro hundido"]
list_color_sombrero = ["pardo oscuro", "rosa claro", "pardo rojizo", "anaranjado", "ocre", "blanquecino", "escarlata", "pardo gris", "verde azulado", "amarillento", "negruzco"]
list_superficie_sombrero = ["aterciopelada", "seca", "viscosa", "lisa", "escamada"]
list_forma_carpoforo = ["oreja", "semicircular", "pezuna"] 
list_color_carpoforo = ["pardo oscuro", "marron rojizo", "pardo gris", "rojo cinabrio", "grisaceo", "pardo rojizo", "circulos concentricos pardos y blanquecinos"]
list_superficie_carpoforo = ["gelatinosa", "aterciopelada", "rugosa", "seca", "resinosa"]
list_tipo_himenio = ["plegado", "laminado", "poroso", "aguijones", "liso"]
list_color_himenio = ["pardo oscuro", "marron rojizo", "blanquecino", "anaranjado", "amarillento", "pardo rojizo", "rosado", "verde palido", "pardo gris", "rojo cinabrio", "gris claro"]
list_tipo_laminas = ["apretadas", "separadas", "bifurcadas", "anastomasadas"]
list_color_pie = ["ocre", "amarillento", "pardo rojizo", "blanquecino", "pardo", "verde azulado", "pardo oscuro", "negruzco", "grisaceo"]
list_tipo_pie = ["grueso", "fino", "proporcional"]





###############################################################################################################################
#   Frame root (menú con opciones principales)                                                                                #
###############################################################################################################################
# Se crea frame para elementos de la interfaz
root_frame = Frame(root, width=1100, height=700, bg = "white")
# Mostramos el frame root
root_frame.place(x = 0, y = 0)

# Subtítulo - ¿Qué desea hacer?
subtitle_root = Label(root_frame, text="¿Qué desea hacer?", fg="black", bg="white", font=('Microsoft YaHei UI Light', 35, "bold"))
subtitle_root.place(x = 600, y = 50)


# Cargar imagen menú
img_root = PhotoImage(file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "icon_SADIHA.png"))
img_root = img_root.subsample(2) # Redimension de imagen
l_img_root = Label(root_frame, image = img_root, bg = "white")
l_img_root.place(x = 20, y = 57) # Mostramos la imagen

#################################### Botón Buscar seta
# Cargar la imagen
start_icon = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "buscar_seta.png"))  # Icono para el botón
start_icon = start_icon.resize((210, 210), Image.ADAPTIVE)  # Redimensionar la imagen 
imagen_start = ImageTk.PhotoImage(start_icon)

# Crear el botón con la imagen
start_button = Button(root_frame, image=imagen_start, compound="left", background= "#837F8A", command=click_search)
start_button.pack(padx=10, pady=10)
start_button.place(x = 600 , y = 130)


#################################### Botón Taxonomia
# Cargar la imagen
taxonomy_icon = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "taxonomia.png"))  # Icono para el botón
taxonomy_icon = taxonomy_icon.resize((210, 210), Image.ADAPTIVE)  # Redimensionar la imagen 
imagen_taxonomy = ImageTk.PhotoImage(taxonomy_icon)

# Crear el botón con la imagen
taxonomy_button = Button(root_frame, image=imagen_taxonomy, compound="left", background= "#937C8C", command=click_taxonomy)
taxonomy_button.pack(padx=10, pady=10)
taxonomy_button.place(x = 817 , y = 130)

#################################### Botón Info
# Cargar la imagen
info_icon = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "informacion.png"))  # Icono para el botón
info_icon = info_icon.resize((210, 210), Image.ADAPTIVE)  # Redimensionar la imagen 
imagen_info = ImageTk.PhotoImage(info_icon)

# Crear el botón con la imagen
info_button = Button(root_frame, image=imagen_info, compound="left", background= "#A27A8E", command= click_information)
info_button.pack(padx=10, pady=10)#D1B0AD
info_button.place(x = 600 , y = 347)


#################################### Botón Salir
# Cargar la imagen
exit_icon = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "salir.png"))  # Icono para el botón
exit_icon = exit_icon.resize((210, 210), Image.ADAPTIVE)  # Redimensionar la imagen 
imagen_exit = ImageTk.PhotoImage(exit_icon)

# Crear el botón con la imagen
exit_button = Button(root_frame, image=imagen_exit, compound="left", background= "#B17890", command=exit)
exit_button.pack(padx=10, pady=10)
exit_button.place(x = 817 , y = 347)
                




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

si_tiene_sombrero = Radiobutton(search_frame, text="Sí", variable=tiene_sombrero, value=1, font=('Microsoft YaHei UI Light', 12), command=click_si_tiene_sombrero)
si_tiene_sombrero.place(x=50, y=120)
no_tiene_sombrero = Radiobutton(search_frame, text="No", variable=tiene_sombrero, value=0, font=('Microsoft YaHei UI Light', 12), command = click_no_tiene_sombrero)
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

combox_forma_sombrero = Combobox(search_frame, values=list_forma_sombrero)
combox_forma_sombrero.place(x=40, y=315)


# Color del sombrero
subtitle_color_sombrero = Label(search_frame, text="Color del sombrero:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_color_sombrero.place(x = 40, y = 370)

combox_color_sombrero = Combobox(search_frame, values=list_color_sombrero)
combox_color_sombrero.place(x=40, y=405)


# Superficie del sombrero
subtitle_superficie_sombrero = Label(search_frame, text="Superficie del sombrero:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_superficie_sombrero.place(x = 40, y = 460)

combox_superficie_sombrero = Combobox(search_frame, values=list_superficie_sombrero)
combox_superficie_sombrero.place(x=40, y=495)


#########################################
#   Carpóforo                           #
#########################################
# Forma del carpoforo
subtitle_forma_carpoforo = Label(search_frame, text="Forma del carpóforo:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_forma_carpoforo.place(x = 430, y = 30)

combox_forma_carpoforo = Combobox(search_frame, values=list_forma_carpoforo, state="disabled")
combox_forma_carpoforo.place(x=430, y=65)


# Color del carpoforo
subtitle_color_carpoforo = Label(search_frame, text="Color del carpóforo:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_color_carpoforo.place(x = 430, y = 120)

combox_color_carpoforo = Combobox(search_frame, values=list_color_carpoforo, state="disabled")
combox_color_carpoforo.place(x=430, y=155)


# Superficie del carpoforo
subtitle_superficie_carpoforo = Label(search_frame, text="Superficie del carpóforo:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_superficie_carpoforo.place(x = 430, y = 210)

combox_superficie_carpoforo = Combobox(search_frame, values=list_superficie_carpoforo, state="disabled")
combox_superficie_carpoforo.place(x=430, y=245)



#########################################
#   Himenio                             #
#########################################

# Tipo de himenio
subtitle_tipo_himenio = Label(search_frame, text="Tipo de himenio:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_tipo_himenio.place(x = 430, y = 320)

combox_tipo_himenio = Combobox(search_frame, values=list_tipo_himenio)
combox_tipo_himenio.place(x=430, y=355)
# Evento para el tipo de himenio. Objetivo: activar campo de tipo de láminas, solo si el tipo de himenio es laminado
combox_tipo_himenio.bind("<<ComboboxSelected>>", accion_seleccion_himenio_laminado)

# Color de himenio
subtitle_color_himenio = Label(search_frame, text="Color de himenio:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_color_himenio.place(x = 430, y = 410)

combox_color_himenio = Combobox(search_frame, values=list_color_himenio)
combox_color_himenio.place(x=430, y=445)


# Tipo de láminas
subtitle_tipo_laminas = Label(search_frame, text="Tipo de láminas:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_tipo_laminas.place(x = 430, y = 500)

combox_tipo_laminas = Combobox(search_frame, values=list_tipo_laminas, state="disabled")
combox_tipo_laminas.place(x=430, y=535)




#########################################
#   Pie                                 #
#########################################

# ¿Tiene pie?
subtitle_tiene_pie = Label(search_frame, text="¿Tiene pie?", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_tiene_pie.place(x = 820, y = 30)

si_tiene_pie = Radiobutton(search_frame, text="Sí", variable=tiene_pie, value=1, font=('Microsoft YaHei UI Light', 12), command=click_si_tiene_pie)
si_tiene_pie.place(x=830, y=70)
no_tiene_pie = Radiobutton(search_frame, text="No", variable=tiene_pie, value=0, font=('Microsoft YaHei UI Light', 12), command=click_no_tiene_pie)
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

combox_color_pie = Combobox(search_frame, values=list_color_pie)
combox_color_pie.place(x=820, y=265)


# Tipo de pie
subtitle_tipo_pie = Label(search_frame, text="Tipo de pie:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 12, "bold"))
subtitle_tipo_pie.place(x = 820, y = 320)

combox_tipo_pie = Combobox(search_frame, values=list_tipo_pie)
combox_tipo_pie.place(x=820, y=355)



#########################################
#       Botones                         #
#########################################
# Botón de búsqueda
button_search_mushroom = Button(search_frame, text="Buscar", command=search_mushroom, font=('Microsoft YaHei UI Light', 18))
button_search_mushroom.place(x=985, y=530)
# Botón para cancelar
button_cancel_search_mushroom = Button(search_frame, text="Cancelar", command = cancel_search_mushroom, font=('Microsoft YaHei UI Light', 18))
button_cancel_search_mushroom.place(x=865, y=530)





###############################################################################################################################
#   Frame información                                                                                                         #
###############################################################################################################################
# Se crea frame para elementos de la interfaz
information_frame = Frame(root, width=1100, height=700, bg = "white")

# Subtítulo - Sobre el proyecto
subtitle_information = Label(information_frame, text="Sobre el proyecto:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 35, "bold"))
subtitle_information.place(x = 600, y = 50)

# Cargar imagen menú
l_img_information = Label(information_frame, image = img_root, bg = "white")
l_img_information.place(x = 20, y = 57) # Mostramos la imagen

# Caja de texto de solo lectura
texto_predeterminado = "Sistema de Ayuda a la Decisión para la Identificación de Hongos Agaricomycetes (SADIHA):\n\nSistema experto en la identificación de hongos del orden Agaricomycetes, construido con Prolog para el motor de inferencia y Python para el frontend. Esta combinación permite una integración fluida y una experiencia de usuario intuitiva. Además, se contempla mejorar el sistema expandiendo la base de datos para incluir más órdenes y especies de setas, lo que ampliaría su utilidad y robustez en la identificación de hongos.\n\n\nDesarrolladores:\n    - Francisco Javier Luna Ortiz.\n    - Alberto Barrais Bellerín."
txt_info = Text(information_frame, height=20, width=50, wrap="word")
txt_info.insert("1.0", texto_predeterminado)
txt_info.config(state = "disabled", font=('Microsoft YaHei UI Light', 13))
txt_info.place(x = 600, y = 130)



# Cargar la imagen
go_back_icon = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "flecha_icon.png"))  # Icono para el botón
go_back_icon = go_back_icon.resize((25, 25), Image.ADAPTIVE)  # Redimensionar la imagen 
go_back_image = ImageTk.PhotoImage(go_back_icon)

# Botón go back
go_back_information_button = Button(information_frame, image=go_back_image, compound="left", background= "#FFFFFF", command=go_back_information)
go_back_information_button.pack(padx=10, pady=10)
go_back_information_button.place(x = 1050 , y = 25)



###############################################################################################################################
#   Frame taxonomía                                                                                                           #
###############################################################################################################################
# Se crea frame para elementos de la interfaz
taxonomy_frame = Frame(root, width=1100, height=700, bg = "white")

# Subtítulo - Taxonomía
subtitle_taxonomy = Label(taxonomy_frame, text="Taxonomía:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 35, "bold"))
subtitle_taxonomy.place(x = 680, y = 50)

# Cargar imagen menú
l_img_taxonomy = Label(taxonomy_frame, image = img_root, bg = "white")
l_img_taxonomy.place(x = 20, y = 57) # Mostramos la imagen

# Botón go back
go_back_taxonomy_button = Button(taxonomy_frame, image=go_back_image, compound="left", background= "#FFFFFF", command=go_back_taxonomy)
go_back_taxonomy_button.pack(padx=10, pady=10)
go_back_taxonomy_button.place(x = 1050 , y = 25)

# Lista seleccionable
listbox = Listbox(taxonomy_frame, selectmode=SINGLE, font=('Microsoft YaHei UI Light', 18))
for elemento in list_orden:
    listbox.insert(END, elemento)
listbox.place(x = 680, y = 120)

# Botón para abrir el documento taxonómico
# Botón de búsqueda
button_open_taxonomy= Button(taxonomy_frame, text="Abrir", command=open_pdf, font=('Microsoft YaHei UI Light', 18))
button_open_taxonomy.place(x=780, y=450)

# Añadir referencias sobre la taxonomía
# Subtítulo - Taxonomía
subtitle_taxonomy_liks = Label(taxonomy_frame, text="Fuentes:", fg="black", bg="white", font=('Microsoft YaHei UI Light', 15, "bold"))
subtitle_taxonomy_liks.place(x = 680, y = 510)
# Enlace 1
link_1 = Text(taxonomy_frame, wrap=WORD, height=1, borderwidth=0, padx=2)
link_1.place(x = 680, y = 550)
link_1.tag_configure("hipervinculo", foreground="blue", underline=True)
link_1.insert("1.0", "taxateca.com", "hipervinculo")
link_1.tag_bind("hipervinculo", "<Button-1>", open_link_1) # Función para abrir el enlace
link_1.configure(state="disabled") # Para que el usuario no pueda modificarlo
# Enlace 2
link_2 = Text(taxonomy_frame, wrap=WORD, height=1, borderwidth=0, padx=2)
link_2.place(x = 800, y = 550)
link_2.tag_configure("hipervinculo", foreground="blue", underline=True)
link_2.insert("1.0", "fungipedia.org", "hipervinculo")
link_2.tag_bind("hipervinculo", "<Button-1>", open_link_2) # Función para abrir el enlace
link_2.configure(state="disabled") # Para que el usuario no pueda modificarlo


root.mainloop() # Loop de la ventana
root.quit() # Liberar recursos cuando se cierre la ventana
