
from hack_1 import fn_hack_1
from hack_2 import fn_hack_2
from hack_3 import fn_hack_3
from hack_4 import fn_hack_4
from hack_5 import fn_hack_5
from hack_6 import fn_hack_6
from hack_7 import fn_hack_7
from hack_8 import fn_hack_8
from hack_9 import fn_hack_9
from hack_10 import fn_hack_10


# h-1
def test_hack_1():
    v = fn_hack_1()
    ck_1 = True if v != "" else False
    ck_2 =  v.isupper() == True
    ck_3 =  v == "FOOZIMAN"
    assert (ck_1,ck_2,ck_3) == (True,True,True)


# h-2
def test_hack_2():
    v = fn_hack_2()
    ck_1 = True if v != "" else False
    ck_2 = v.islower() == True
    ck_3 = v == "fooziman"
    assert (ck_1,ck_2,ck_3) == (True,True,True)


# h-3
def test_hack_3():
    v = fn_hack_3()
    ck_1 = True if v != "" else False
    ck_2 = v[0].isupper() == True
    ck_3 = v == "Fooziman"
    assert (ck_1,ck_2,ck_3) == (True,True,True)


# h-4
def test_hack_4():
     v = fn_hack_4()
     ck_1 = True if v != "" else False
     ck_2 = v[len(v)-1].isupper() == True
     ck_3 = v == "foozimaN"
     assert (ck_1,ck_2,ck_3) == (True,True,True)
    

# h-5
def test_hack_5():
    v = fn_hack_5()
    ck_1 = True if v != "" else False
    ck_2 = True if type(v) is str else False
    ck_3 = v == "f00z1m@n"
    assert (ck_1,ck_2,ck_3) == (True,True,True)

    
#h-6 
def test_hack_6():
    v = fn_hack_6()
    ck_1 = True if type(v) is list else False
    ck_2 = True if len(v) != 0 else False
    ck_3 = v == [0,1,2,3,4,5]
    assert (ck_1,ck_2,ck_3) == (True,True,True)
    

# h-7
def test_hack_7():
    v = fn_hack_7()
    ck_1 = True if type(v) is list else False
    ck_2 = True if len(v) != 0 else False
    ck_3 = v == [5,4,3,2,1,0]     
    assert (ck_1,ck_2,ck_3) == (True,True,True)

    
# h-8
def test_hack_8():
    v = fn_hack_8()
    ck_1 = True if type(v) is list else False
    ck_2 = True if len(v) != 0 else False
    ck_3 = v == [3,5,7]
    assert (ck_1,ck_2,ck_3) == (True,True,True)

    
# h-9    
def test_hack_9():
    v = fn_hack_9()
    ck_1 = True if type(v) is list else False
    ck_2 = True if len(v) != 0 else False
    ck_3 = v == [1,'@',2,'@',3,'@']
    assert (ck_1,ck_2,ck_3) == (True,True,True)

    
# h-10    
def test_hack_10():
    v = fn_hack_10()
    ck_1 = True if type(v) is list else False
    ck_2 = True if len(v) != 0 else False
    ck_3 = v == ["F","0","0","Z","1","M","@","N"]
    assert (ck_1,ck_2,ck_3) == (True,True,True)