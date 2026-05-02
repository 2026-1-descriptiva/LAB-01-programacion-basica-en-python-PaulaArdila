"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """

    resultado = {}
    with open("files/input/data.csv", newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter="\t")
        for fila in reader:
            letra_col0 = fila[0]
            valor_col2 = int(fila[1])
            letras_col4 = fila[3].split(",")

            for letra in letras_col4:
                if letra not in resultado:
                    resultado[letra] = 0
                resultado[letra] += valor_col2

    # a continuación ordeno alfabéticamente por clave
    resultado_ordenado = dict(sorted(resultado.items()))

    return resultado_ordenado

if __name__ == "__main__":
    pregunta_11()