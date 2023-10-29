"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    o = "0"
    i = "1"
    a = "@"
    new_result1 = result.replace ("o","0") 
    new_result2 = new_result1.replace ("i","1") 
    new_result3 = new_result2.replace ("a","@")
    return new_result3  