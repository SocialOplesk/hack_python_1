"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    result = []
    result = [result for result in range (6)]
    return result  