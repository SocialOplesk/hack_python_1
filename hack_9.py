"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    result.insert(1,"@")
    result.insert(3,"@")
    result.insert(5,"@")
    return result  