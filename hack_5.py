"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    result2 = result.replace('o','0')
    newresult = result2.replace('a','@')
    print(newresult)
    return result  

fn_hack_5()