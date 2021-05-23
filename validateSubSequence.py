def validateSubsequence(array,sequence):
    sequenceIndex = 0
    for value in array:
        if sequenceIndex == len(sequence):
            return True
        if sequence[sequenceIndex] == value:
            sequenceIndex += 1
    return sequenceIndex == len(sequence)
    
validateSubsequence([1,6,8,7,45,23],[6,7,8])
