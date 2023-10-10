"""
list: [1,3,5,7,9] output => [3,5,7]
"""

#Aplico slicing para obtener la parte de la lista que deseo y la sobreescribo
def fn_hack_8():
    result = [1,3,5,7,9]
    result = result[1:4]
    return result  