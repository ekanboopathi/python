n = int(input("enter the element to be inserted: "))
a=[]
for i in range(0,n):
    ele = int(input("enter the element: "))
    a.append(ele)
avg=sum(a)/n
print("Average of the element in the list",avg)