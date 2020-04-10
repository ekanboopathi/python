def boo(n):
    if (n <=1):
        return 1
    else:
        return(n*boo(n-1))

n = int(input("Enter the number:"))
boo(n)
print("Factoraial",boo(n))