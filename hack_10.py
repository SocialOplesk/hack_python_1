"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result.split()  
    result = result.replace('o','0')
    result = result.replace('i','1')
    result = result.replace('a', '@')
    result = ",".join(result)
    result = "'".join(result)    

    return result
    
