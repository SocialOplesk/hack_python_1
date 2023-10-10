"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

#Aplicando un while con un contador para el punto de cierre y el método de lista 
#insert() para adicionar la información que deseo en el índice especificado
def fn_hack_9():
    result = [1,2,3]
    lg_res = len(result)*2
    count = 1
    while (count<lg_res):
        result.insert(count,'@')
        count+=2
    return result  
