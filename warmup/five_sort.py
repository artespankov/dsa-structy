def five_sort(nums):
    """
    Write a function, five_sort, that takes in a list of numbers as an argument.
    The function should rearrange elements of the list such that all 5s appear at the end.
    Your function should perform this operation in-place by mutating the original list.
    The function should return the list.
    Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.
    n = array size
    Time: O(n)
    Space: O(1)
    """
    L, R = 0, len(nums) - 1
    while L < R and L < len(nums) - 1:
        if nums[R] == 5:
            R -= 1
        elif nums[L] == 5:
            nums[L], nums[R] = nums[R], nums[L]
            L += 1
        else:
            L += 1
    return nums


five_sort([12, 5, 1, 5, 12, 7])
# -> [12, 7, 1, 12, 5, 5]
five_sort([5, 2, 5, 6, 5, 1, 10, 2, 5, 5])
# -> [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]
five_sort([5, 5, 5, 1, 1, 1, 4])
# -> [4, 1, 1, 1, 5, 5, 5]
five_sort([5, 5, 6, 5, 5, 5, 5])
# -> [6, 5, 5, 5, 5, 5, 5]
five_sort([5, 1, 2, 5, 5, 3, 2, 5, 1, 5, 5, 5, 4, 5])
# -> [4, 1, 2, 1, 2, 3, 5, 5, 5, 5, 5, 5, 5, 5]
fours = [4] * 20000
fives = [5] * 20000
nums = fours + fives
five_sort(nums)
# twenty-thousand 4s followed by twenty-thousand 5s
# -> [4, 4, 4, 4, ..., 5, 5, 5, 5]
