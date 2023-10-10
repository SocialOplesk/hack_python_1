"""
text: "fooziman" output => "foozimaN"
"""

#Para este ejercicio utilizo slicing para extraer la parte de cadena que deseo cambiar, también el plus para concatenarla

def fn_hack_4():
    result = "fooziman"
    result = result[:-1] + result[-1].upper()
    return result