#Bubblesort
def Anu (n):
    for j in range(len(n)-1,0,-1):
        for i in range(j):
            if n[i]> n[i+1]:
                temp = n[i]
                n[i] = n[i+1]
                n[i+1] = temp

n = [1,4,8,2,9,54,34]
Anu(n)
print(n)                
