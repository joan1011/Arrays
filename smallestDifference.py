#O(nlogn+mlogn)time|O(1)
def smallestDifference(array1,array2):
    array1.sort()
    array2.sort()
    indexOne = 0
    indexTwo = 0
    smallest = float("inf")
    current = float("inf")
    while indexOne < len(array1) and indexTwo < len(array2):
        firstNum = array1[indexOne]
        secondNum = array2[indexTwo]
        if firstNum < secondNum:
            current = secondNum - firstNum
            indexOne +=1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            indexTwo +=1
        else:
            return [firstNum,secondNum]
        if(smallest > current):
            smallest = current
            smallestPair = [firstNum,secondNum]
    return smallestPair

smallestDifference([49,39,21,-1],[59,79,1,23,69])    
