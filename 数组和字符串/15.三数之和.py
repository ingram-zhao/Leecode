def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if nums[i] > 0: return res
        if i > 0 and nums[i] == nums[i-1]: return res
        low, high = i + 1, len(nums) - 1
        while low < high:
            if nums[low] + nums[high] > -nums[i]:
                high -= 1
            elif nums[low] + nums[high] < -nums[i]:
                low += 1
            else:
                res.append([nums[low],nums[high],nums[i]])
                while low < high and nums[low] == nums[low + 1]:
                    low += 1
                while low < high and nums[high] == nums[high - 1]:
                    high -= 1
                low += 1
                high -= 1  
    return res
if __name__ == "__main__":
    # 特殊测试用例： [0,0,0,0]
    lista = [1,-1,-1,0]
    res = threeSum(lista)
    print(res)