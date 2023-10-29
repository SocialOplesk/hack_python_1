"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    i = ['@','@','@']
    intercalar = []
    x = 0
    y = 0
    while x < len(result) and y < len(i):
        intercalar.append(result[x])
        intercalar.append(i[y])
        x += 1
        y += 1
    while x < len(result):
        intercalar.append(result[x])
        x += 1
    while y < len(i):
        intercalar.append(i[y])
        y += 1
    return intercalar  