# pyswip lleva mucho tiempo sin actualizarse, recomiendo utilizar una vesion anterior de swi-prolog

from pyswip import Prolog
import sys




# Carga el archivo Prolog
prolog = Prolog()
# Agrega los hechos usando asserta/1
hechos = [
    "known(yes, sombrero, 'si')",
    "known(yes, 'superficie sombrero', 'seca')",
    "known(yes, 'tamano sombrero', 7.5)",
    "known(yes, sombrero, convexo)",
    "known(yes, 'forma sombrero', 'convexo')",
    "known(yes, 'color sombrero', 'blanquecino')",
    "known(yes, 'color himenio', 'rosado')",
    "known(yes, 'tipo laminas', 'apretadas')",
    "known(yes, pie, 'si')",
    "known(yes, 'anillo', 'si')",
    "known(yes, 'tipo himenio', laminado)",
    "known(yes, 'color pie', 'blanquecino')",
    "known(yes, 'tipo pie', 'grueso')"
]

for hecho in hechos:
    prolog.assertz(hecho)

prolog.consult("./src/SetasExper.pl")
# Consulta sobre la seta
consulta = "seta(X)"
soluciones = list(prolog.query(consulta))

if len(soluciones) == 0:
    print("No se encontraron soluciones")
else:
    respuesta = list(prolog.query("seta(X)"))


    print("Respuesta:", respuesta[0]["X"])
    print("\nHabitat:")
    print(list(prolog.query("salida(habitat,X)"))[0]["X"])
    print("\nComestibilidad:")
    print(list(prolog.query("salida(comestibilidad,X)"))[0]["X"])