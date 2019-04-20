import pdb

def swap(elements, x, y):
    temp = elements[x]
    elements[x] = elements[y]
    elements[y] = temp

def bubblesort(array):
    numElements = len(array)

    while numElements>0:
        for i in range(numElements-1):
            pdb.set_trace()
            if array[i]>array[i+1]:
                swap(array, i, i+1)
   
        numElements = numElements-1    

    return array    


given = [29, 10, 14, 37, 14]

print(bubblesort(given))