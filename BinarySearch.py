import pdb


def RecusrsiveBinarySearch(num, given_list):
    if bsearch(0,len(given_list)-1, num,given_list):
        print("Found it")
    else:
        print("Not found")    

def bsearch(start,end,num, items):
    mid= (start+end)//2
    if start<=end:
        if num<items[mid]:
            end=mid-1
            return bsearch(start, end, num, items)
        elif num>items[mid]:
            start=mid+1
            return bsearch(start, end, num, items)
        elif num==items[mid]:
            return True
    else:    
        return False   


def IterativeBinarySearch(num,given_list):
    start =0
    end = len(given_list)-1

    while start<=end:
        mid = (start+end)//2
        if given_list[mid]==num:
            return True
        elif num>given_list[mid]:
            start=mid+1
        elif num<given_list[mid]:
            end=mid-1

    return False        


testList=[4,8,33,34,37,43,50]
#RecusrsiveBinarySearch(4, testList)

if IterativeBinarySearch(0,testList):
    print("I nab am!")
else:
    print("GERRARAHERE!")    
