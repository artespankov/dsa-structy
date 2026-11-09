def max_subarray_product_size_k(nums, k):
    """
    Write a function that takes in a list of numbers and a size k as arguments.
    The function should return the maximum product of subarrays that contain exactly k elements.

    You can assume that k is less than or equal to the length of the input list.

    You can assume that numbers of the list are non-zero.
    Time: O(n)
    Space: O(1)
    """
    L = 0
    max_prod = float("-inf")

    prod = 1
    for R in range(len(nums)):
        prod *= nums[R]
        if R - L + 1 == k:
            max_prod = max(max_prod, prod)
            prod /= nums[L]
            L += 1
    return max_prod

    # import math
    # current_product = math.prod(nums[:k])
    # max_product = current_product
    # for i in range(0, len(nums) - k):
    #     current_product /= nums[i]
    #     current_product *= nums[i + k]
    #     max_product = max(current_product, max_product)
    # return max_product


if __name__ == "__main__":
    max_subarray_product_size_k([4, 2, 1, -9, 8, 2, 3], 3) # -> 48
    # [8,2,3] is the subarray of size 3 with the maximal product
    max_subarray_product_size_k([-9, 1, -8, 2, 3, 7], 3) # -> 72
    max_subarray_product_size_k([7, 4, -5, -7, 8, -10, -1], 2) # -> 35
    max_subarray_product_size_k([60, 20, 10, 90, 50], 1) # -> 90
    max_subarray_product_size_k([1,2,3,4], 4) # -> 24
    nums = [1] * 9000 # [1,1,1,...]
    max_subarray_product_size_k(nums, 1000) # -> 1
    nums = [1] * 40000 # [1,1,1,...]
    max_subarray_product_size_k(nums, 5000) # -> 1
