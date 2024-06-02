def performSelectionSort(nums): 
    n = len(nums)
    fixThisIndex = n - 1 
    while fixThisIndex > 0:
        maxEleIndex = fixThisIndex
 
 
        if maxEleIndex != fixThisIndex:
            temp = nums[maxEleIndex] 
            nums[maxEleIndex] = nums[fixThisIndex]
            nums[fixThisIndex] = temp 
        print(nums)
        fixThisIndex -= 1 