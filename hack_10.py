"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    o = "0"
    i = "1"
    a = "@"
    new_result1 = result.replace ("o","0") 
    new_result2 = new_result1.replace ("i","1") 
    new_result3 = new_result2.replace ("a","@")
    return list(new_result3.upper())