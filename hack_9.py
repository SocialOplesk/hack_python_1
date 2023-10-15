"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    i = 0
    while i<=5:
        if i==1 or i==3 or i==5:
            result.insert(i,"@")            
        i+=1
    return result  

fn_hack_9()