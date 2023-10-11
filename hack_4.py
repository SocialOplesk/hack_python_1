"""
text: "fooziman" output => "foozimaN"
"""

def fn_hack_4():
    result = "fooziman"
    capital = result[:7] + result[-1].upper()
    print(capital)
    return result

fn_hack_4()