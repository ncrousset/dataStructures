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