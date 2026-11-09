
def max_subarray_sum_size_k(nums, k):
    """
    Write a function that takes in a list of numbers and a size k as arguments. The function should return the maximum sum of subarrays that contain exactly k elements.
    You can assume that k is less than or equal to the length of the input list.
    Time: O(n)
    Space: O(1)
    """

    # Time: O(n*k) BRUTE - TIMEOUT
    # Space: O(1)
    # max_sum = -float('inf')
    # for i in range(0, len(nums) - k + 1):
    #     current_sum = sum(nums[i: i + k])
    #     if current_sum > max_sum:
    #     max_sum = current_sum
    # return max_sum

    # max_summ = float("-inf")
    # for i in range(0, len(nums)-k+1):
    #     max_summ = max(max_summ, sum(nums[i: i + k]))
    # return max_summ


    # summ = 0
    # max_summ = float("-inf")
    # n = len(nums)
    # L = 0
    # for R in range(n):
    #     summ += nums[R]
    #     if R-L + 1 > k:
    #         summ -= nums[L]
    #         L += 1
    #     if R-L + 1 == k:
    #         max_summ = max(max_summ, summ)
    # return max_summ

    curr_sum = sum(nums[:k])
    max_sum = curr_sum

    for i in range(0, len(nums) - k + 1):
        curr_sum -= nums[i]
        curr_sum += nums[i+k]
        max_sum = max(max_sum, curr_sum)
    return max_sum









if __name__ == "__main__":
    max_subarray_sum_size_k([4, 2, 1, -9, 8, 4, 3], 3) # -> 15
    # [8,4,3] is the subarray of size 3 with the maximal sum

    max_subarray_sum_size_k([2, 1, 5, -4, 6] , 3) # -> 8

    max_subarray_sum_size_k([1, 4, 1, 10, 25, 3, 1, 0, 20], 4) # -> 40
    max_subarray_sum_size_k([20, 50, 10, 60, 80, 70], 1) # -> 80
    max_subarray_sum_size_k([-4, -18, -2, -5, -9], 2) # -> -7
    nums = [1] * 10000 # [1,1,1,1,...]
    max_subarray_sum_size_k(nums, 1000) # -> 1000
    nums = [1] * 80000 # [1,1,1,1,...]
    max_subarray_sum_size_k(nums, 5000) # -> 5000
