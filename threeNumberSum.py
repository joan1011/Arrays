#O(n^2) time | O(n) space
def threeNumberSum(array,target):
    array.sort()
    triplets = []
    for i in range(len(array)-2):
        leftIndex = i+1
        rightIndex = len(array)-1
        while leftIndex < rightIndex:
            currentsum = array[i] + array[leftIndex] + array[rightIndex]
            if currentsum == target:
                triplets.append([array[i],array[leftIndex],array[rightIndex]])
                leftIndex +=1
                rightIndex -=1
            elif currentsum > target:
                rightIndex -=1
            elif currentsum < target:
                leftIndex +=1
    return triplets
        
            
            
            
threeNumberSum([100,200,30,50,0,-20],80)
    
    
        
