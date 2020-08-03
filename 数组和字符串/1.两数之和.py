def twoSum(nums,target):
    set1 = {}
    for i in range(len(nums)):
        if target - nums[i] in set1:
            return [set1[target-nums[i]],i]
        set1[nums[i]] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    res = twoSum(nums,target)
    print(res)