
def boo (list,n):
 l = 0
 u = len(list)-1

 while l <= u:
     mid = (l+u)//2
     if list[mid] == n:
         return True
     else: 
            if list[mid] < n:
                l = mid
            else:
                u = mid

list = [1,2,3,4,5,6,7,]
n = 4

if boo (list,n):
    print("it is found")
else:
    print("it is not found")