'''
    Collections - List, Tuple, Dictionary

    Variable - Quantitative variable, categorical variable
'''

# vegetables
item1 = 'tomato'
item2 = 'potato'
item3 = 'carrot'
item4 = 'brinjal'

# List
vegetables = ['tomato', 'potato', 'brinjal', 'carrot']

print(vegetables[2])

vegetables[0] = 'beetroot'
print(vegetables[0])

# List item add
vegetables.append('drumstick')

print(vegetables[4])

# Iterate
# for x in vegetables:
#     print(x)

for x in range(0, len(vegetables)):
    print(vegetables[x])

# Print
# print(vegetables[-1])
# print(vegetables[1:4])
# print(vegetables[0:2])

# [0,1,2,3,4,5]

vegetables.insert(2, 'raddish')
print('final inserted items ')
for x in vegetables:
    print(x)

# Delete
vegetables.remove('beetroot')

print('final deleted items ')

for x in vegetables:
    print(x)

# Add Multiple numbers

numbers = [3, 7, 9, 12, 8, 12, 65, 3]
totalvalue = 0

for x in numbers:
    totalvalue = totalvalue + x


print(f'The totalvalue is {totalvalue}')

