# 解法1：遍历 O(N)
def searchInsert(nums,target):
    i = 0
    while i < len(nums):
        if target <= nums[i]:
            return i 
        i += 1
    return i


# 解法2：二分查找 O(logN)
def searchInsert2(nums,target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low+high) // 2
        if target == nums[mid]:
            return mid 
        elif target < nums[mid]:
            high = mid
        else: 
            low = mid
    return low  

if __name__ == "__main__":
    pass