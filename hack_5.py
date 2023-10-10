"""
text: "fooziman" output => "f00z1m@n"
"""

#Función que contiene 2 parametros, el primero cadena principal y el segundo es una lista cuyo valores son unas tuplas
#que representan una relación entre valor a buscar y valor de reemplazo, en el bucle for se desempaqueta la tupla.  
#Se utilizan los métodos de cadena find para encontrar coincidencia con la cadena principal y replace para reemplazar el valor en
#caso de coincidencia.

def fn_hack_5():
    result = "fooziman"
    caract=[('oo','00'),('i','1'),('a','@')]

    for i in range(len(caract)):
        str_sear, str_rep= caract[i]
        if result.find(str_sear):            
            result= result.replace(str_sear, str_rep) 

    return result