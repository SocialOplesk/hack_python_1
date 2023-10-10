"""
loop: while [] output => [5,4,3,2,1,0]
"""

#En este ejercicio utilizo list comprehension para crear una lista con una sintaxis mas corta basada en el 
#rango que he especificado en el bucle y el método de lista reverse() para invertir los valores.
def fn_hack_7():
    result = []
    result = [i for i in range(6)]
    #otro método result.sort(reverse=True)
    result.reverse()
    return result  