"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

#Reutilización del código del ejercicio 5. Solo se cambian los valores de la variable correspondiente a la cadena principal
#y las tuplas de los valores a buscar y a reemplazar.

def fn_hack_10():
    result = "fooziman"
    caract=[('o','0'),('i','1'),('a','@')]

    for i in range(len(caract)):
        str_sear, str_rep= caract[i]
        if result.find(str_sear):            
            result= result.replace(str_sear, str_rep) 

    return list(result.upper())
