import pdb

def swap(array, indexLeft, indexRight):
    temp = array[indexLeft]
    array[indexLeft] = array[indexRight]
    array[indexRight] = temp


def sumNum(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return num + sumNum(num-1)

def sortingAlgorithm(elements):
    indexMax = 0
    end = len(elements)

    while end-1 >0:
        for i in range(end):
            if elements[i] > elements[indexMax]:
                indexMax = i

        swap(elements, indexMax, end-1)  
        end =end-1                  
    return elements


"""
################ Insertion Sort ################
"""
def insertionSort(array):
    """
    Assume first element is sorted and move to next element
    For each remaining unsorted item,
        store the unsorted item to be used for comparison
        compare the element with previous element
        while the element is less than previous element, 
            shift the previous element forward
            compare it with next previous until it is not less than the element compared with

    """

    for i in range(1,len(array)):
        currIndex =i-1
        value = array[i]
        while value < array[currIndex] and currIndex>=0:
            array[currIndex+1]=array[currIndex]
            currIndex = currIndex-1
            #pdb.set_trace()    
        currIndex = currIndex+1       
        array[currIndex]=value
    return array    

"""
################ Merge Sort ################
"""
def mergeSort(array):
    if len(array)<=1:
        return array

    mid = len(array)//2    

    left = array[:mid]
    right = array[mid:]

    left = mergeSort(left)
    right = mergeSort(right)

    return list(merge(left, right))

def merge(left, right):
    elements=[]

    leftInd = 0
    rightInd=0

    while leftInd<len(left) and rightInd<len(right):
        if(left[leftInd] <= right[rightInd]):
            elements.append(left[leftInd])
            leftInd += 1
        else:
            elements.append(right[rightInd])
            rightInd+=1

    if left:
        elements.extend(left[leftInd:])

    if right:
        elements.extend(right[rightInd:]) 

    return elements       
 
    



given_list = [5,4,3,2,1]

#merge(given_list,elements,0,len(given_list)//2,len(given_list)-1)
print(mergeSort(given_list), end=" ")

print("The sum is {}".format(sumNum(10)))
   
