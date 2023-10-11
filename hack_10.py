"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result1 = result.upper()
    result2 = result1.replace('O','0')
    result3 = result2.replace('I','1')
    result4 = result3.replace('A','@')
    ls = list(result4)
    print(ls)
    return result  

fn_hack_10()