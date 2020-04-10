'''
    For Loop
    for temp_variabe in Collection:
        ...
    for temp_variable in range(start, end, step): +1
        ....
'''

# for x in range(10, 0, -1):
#     print(x)

for x in range(0, 10):
    for y in range(0, 10):
        print(f"{x} {y}")

'''
    00
    11
    22
    33
    44
    55
'''

for x in range(0, 10):
    print(x, end='')


'''
    0
    01
    012
    0123
    01234
'''
n=6
for x in range (0,n):
    for y in range(0,x+1):
        print(y,end='')
    print()