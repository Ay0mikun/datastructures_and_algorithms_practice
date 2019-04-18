import pdb

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

def swap(array, indexLeft, indexRight):
    temp = array[indexLeft]
    array [indexLeft] = array[indexRight]
    array[indexRight] =temp


def sumNum(num):
    if num ==0:
        return 0
    if num==1:
        return 1    
    return num + sumNum(num-1) 


given_list = [5,4,3,2,1]



print(sortingAlgorithm(given_list), end=" ")

print("The sum is {}".format(sumNum(10)))
   