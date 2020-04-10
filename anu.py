count=dict()
n = [10,20,30,20,40,10,80,50,60,70,80,10,9]
# print ([[i,n.count(i)] for i in set(n)])
# count=dict()
for i in n:
    count[i]=count.get(i,0)+1
print(count)