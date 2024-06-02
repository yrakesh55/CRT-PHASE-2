def perfomancebubblesort(nums):
    n=len(nums)
    fixthisindex=n-1
    while fixthisindex >0:
        for index in range(fixthisindex):
            if nums[index]>nums[index+1]:
                temp=nums[index]
                nums[index]=nums[index+1]
                nums[index+1]=temp
        print(nums)
        fixthisindex-=1
nums=[10,28,7,9,2,3]
print("before sorting",nums)
print("after sorting",nums)
perfomancebubblesort(nums)
