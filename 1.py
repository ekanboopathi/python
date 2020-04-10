a=[1,2,3]
def myfun(b):
    print('the value of b is',  b)
    b[0]=100
    b[1]=22
    print('the new value of b is', b)
    myfun(a)
