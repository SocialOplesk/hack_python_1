"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    n = len(result)
    i = 0
    new_result=[]
    
    while (i < n):
        new_result.append(result[i])
        if i < n - 1:
            new_result.append('@')
        i += 1
    print (new_result)
    return result

fn_hack_9()