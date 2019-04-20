def swap(elements, x, y):
    temp = elements[x]
    elements[x] = elements[y]
    elements[y] = temp


def getMinElementIndex(elements):
    minimum = 0

    for i in range(len(elements)):
        if elements[i]<elements[minimum]:
            minimum = i

    return minimum        

def SelectionSort(array):
    arrayLength = len(array)
    position = 0
    while arrayLength > 0:
        for i in range(position+1, arrayLength):
            min = getMinElementIndex(array[position+1:])
            swap(array, position, min)
        position =position+1 
        arrayLength = arrayLength-1

    return array    



given = [29, 10, 1, 14, 37, 13, 23, 4]

print(SelectionSort(given))
