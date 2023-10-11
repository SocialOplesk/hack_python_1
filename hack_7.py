"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    num = 5
    
    while(num >= 0):
        result.append(num)
        num -= 1
    print(result)
    
fn_hack_7()