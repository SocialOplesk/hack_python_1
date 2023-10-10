"""
loop: for [] output => [0,1,2,3,4,5]
"""
#En este ejercicio utilizo list comprehension para crear una lista con una sintaxis mas corta basada en el 
#rango que he especificado en el bucle
def fn_hack_6():
    result = []
    result = [i for i in range(6)]
    return result  