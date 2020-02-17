"""
Definiendo y utilizando algunas funciones
mas comunes y uliles de lista
"""
myList = [1,2,3]

def title(label):
    print(f"------{label}------")

def labelWithList(myList, label="Origin"):
    strList = '[' + ','.join(map(str, myList)) + ']'
    print(f"{label} = {strList}")

# agregar un elemento al final
title('append()')
labelWithList(myList)
myList.append(5)
labelWithList(myList, "Now")
print('\n')

# Agregando un elemento con su indice
title('insert()')
labelWithList(myList)
myList.insert(0,0)
labelWithList(myList, "Now")
print('\n')

# extender la lista con otra lista
title('extend()')
labelWithList(myList)
myList.extend([6,7,8])
labelWithList(myList, "Now")
print('\n')

# extender con :
title('extend with ":"')
labelWithList(myList)
myList[3:4] = [10,11, 12]
labelWithList(myList, "Now")
print('\n')

# clear
title('clear()')
labelWithList(myList)
myList.clear()
labelWithList(myList, "Now")
print('\n')

# del()
title('del')
myList = [1,2,3]
labelWithList(myList)
del myList[1:]
labelWithList(myList, "Now")
del myList[:]
labelWithList(myList, "Now Del all")
print('\n')

# count()
myList = ['one','one', 'two', 'three', 'five']
print(f"Out of count(): {myList.count('one')}")
print('\n')

# index() get the first element
print(f"Out of index(): {myList.index('one')}")
print('\n')

# sort()
title('sort()')
myList = [1, 4, 3, 5, 2]
labelWithList(myList)
myList.sort()
labelWithList(myList, "Now")

title('sort(reverse=True)')
myList = [1, 4, 3, 5, 2]
labelWithList(myList)
# myList = sorted(myList, reverse=True)
myList.sort(reverse=True)
labelWithList(myList, "Now")

print('\n')
