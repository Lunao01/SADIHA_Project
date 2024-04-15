from pyswip import Prolog

# Inicializar el motor de Prolog
prolog = Prolog()

# Cargar el archivo Prolog
prolog.consult("prolog.pl")

# Consulta Prolog para obtener pájaros rojos
resultados = list(prolog.query("color(Bird, red)"))

# Imprimir los resultados
print("Birds with red color:")
for resultado in resultados:
    print(resultado["Bird"])