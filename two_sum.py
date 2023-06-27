
def twoSum():
    nums=[]
    num=[]
    for i in range (len(nums)):
        nums[i]=int(input("enter num ",i))
        for j in range(len(nums)):
            t=nums[j+1]+nums[i]
            if target==t:
                num=[i,j+1]
                break
    return num
twoSum()