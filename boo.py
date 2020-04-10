n = [10,20,30,20,40,10,80,50,60,70,80,10,9]
count = 0
# for i in range(0,len(n)):
#     for j in range(i+1,len(n)):
#         if n[i] == n[j]:
#             print(n[j])
print ([[k,n.count(k)] for k in set(n)])  