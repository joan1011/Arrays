def twoNumberSum(array,target):
    
    array.sort()
    leftIndex = 0;
    rightIndex = len(array) - 1
    while leftIndex < rightIndex:
        currentsum = array[leftIndex] + array[rightIndex]
        if currentsum == target:
            return [array[leftIndex],array[rightIndex]]
        elif currentsum > target:
            rightIndex -=1
        elif currentsum < target:
            leftIndex +=1
            
            
            
twoNumberSum([100,200,30,50,60],80)
    
    
        
