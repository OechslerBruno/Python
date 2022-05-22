#Loops
bruno = {}
bruno['first'] = 'Bruno'
bruno['last'] = 'Oechsler'

for name in bruno:
    print(name)


for i in range(0, 2):#start, number of iterations
    print(i)
    
    
myList = ['a', 'b', 'c', 'd']
    
for i in range(0, len(myList)):
    print(i)
    
index = 0    
while index < len(myList):
    print(myList[index])
    index += 1
    
#repetição de itens da lista
print('\n')
myListA = [1, 2]
myListB = myListA * 3
print(myListB)

#verifica se um item está na lista
print('b' in myList)

#adiciona item na lista
myList.append('e')
print(myList)