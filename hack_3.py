"""
text: "fooziman" output => "Fooziman"
"""

#Para este ejercicio utilizo slicing para extraer la parte de cadena que deseo cambiar, también el plus para concatenarla

def fn_hack_3():
    result = "fooziman"
    result = result[0].upper() + result[1:]
    #otra manera de concatenar sería f"{result[0].upper()}{result[1:]}"
    return result