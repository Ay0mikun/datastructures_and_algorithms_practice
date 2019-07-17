def quickSort(arr):
    less = []
    pivotList = []
    more = []

    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more



def reverseList(head):
    if head is None or head.next is None:
        return head

    remaining = reverseList(head.next)    

    head.next.next=head
    head.next=None

    return remaining


given=[5,4,10]
print(quickSort(given))