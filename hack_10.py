"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    
    result = result.replace ("fooziman", "F00Z1M@N") 
    result = list(result)
    return result  