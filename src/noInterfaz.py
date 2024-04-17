# pyswip lleva mucho tiempo sin actualizarse, recomiendo utilizar una vesion anterior de swi-prolog

from pyswip import Prolog
import sys




# Carga el archivo Prolog
prolog = Prolog()

prolog.consult("./src/SetasExper.pl")

# Consulta el predicado
# if prolog.query("iniciar"):
#    print("Consulta exitosa")

respuesta = list(prolog.query("iniciar,seta(X)"))


print("Respuesta:", respuesta[0]["X"])
print("\nHabitat:")
print(list(prolog.query("salida(habitat,X)"))[0]["X"])
print("\nComestibilidad:")
print(list(prolog.query("salida(comestibilidad,X)"))[0]["X"])