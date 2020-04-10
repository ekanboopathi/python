def bubblesort(a):
    n=len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

a=[]
s=int(input('enter the element:'))
for x in range(0,s):
    f=int(input())
    a.append(f)
print (bubblesort(a))