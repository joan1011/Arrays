#O(nlogn+mlogn)time|O(1)
def moveElemenToEnd(array,target):
    i = 0
    j = len(array) - 1
    while(i<j):
        while(i<j and array[j] == target):
            j -=1
        if(array[i] == target):
            array[i],array[j] = array[j],array[i]
        i +=1
    return array
    
moveElemenToEnd(([4,3,8,4,5,6,7]),4)
