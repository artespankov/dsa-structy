# from functools import lru_cache
#
#
# def max_path_sum(grid):
#     n, m = len(grid), len(grid[0])
#     max_sum = 0
#
#     @lru_cache(maxsize=None)
#     def bfs(row, column, curr_sum):
#         nonlocal max_sum
#         if row >= n or column >= m:
#             return
#         if grid[row][column] == 'x':
#             return
#         curr_sum += grid[row][column]
#         max_sum = max(max_sum, curr_sum)
#         old_val = grid[row][column]
#         # grid[row][column] = 'x'
#         bfs(row, column + 1, curr_sum)
#         bfs(row + 1, column, curr_sum)
#         grid[row][column] = old_val
#     bfs(0, 0, 0)
#     return max_sum


def max_path_sum(grid):
    """
    max path sum
    Write a function, max_path_sum, that takes in a grid as an argument.
    The function should return the maximum sum possible by traveling a path from the top-left corner to the bottom-right corner. You may only travel through the grid by moving down or right.
    You can assume that all numbers are non-negative.
    r = # rows
    c = # columns
    Time: O(2^(r+c))
    Space: O(r+c)
    2: only two options, right or down
    r + c: you need to traverse the field completely, from top left to down right corner

    Time: O(r*c) with memoization
    Space: O(r*c) with memoization
    r * c comes from the size of the memo, where r,c is the combination for key,
    so we could have r*c different keys in memo
    """
    return _max_path_sum(0, 0, grid, {})


def _max_path_sum(row, column, grid, memo):
    pos = (row, column)
    if pos in memo:
        return memo[pos]
    if row == len(grid) or column == len(grid[0]):
        return 0
    if row == len(grid) - 1 and column == len(grid[0]) - 1:
        return grid[row][column]
    right = _max_path_sum(row, column + 1, grid, memo)
    down = _max_path_sum(row + 1, column, grid, memo)
    memo[pos] = grid[row][column] + max(right, down)
    return memo[pos]


if __name__ == "__main__":
    grid = [
        [1, 3, 12],
        [5, 1, 1],
        [3, 6, 1],
    ]
    max_path_sum(grid)  # -> 18
    grid = [
        [1, 2, 8, 1],
        [3, 1, 12, 10],
        [4, 0, 6, 3],
    ]
    max_path_sum(grid)  # -> 36
    grid = [
        [1, 2, 8, 1],
        [3, 10, 12, 10],
        [4, 0, 6, 3],
    ]
    max_path_sum(grid)  # -> 39
    grid = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    max_path_sum(grid)  # -> 27
    grid = [
        [1, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 2, 1, 1, 6, 1, 1, 5, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 5, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [2, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1],
        [2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 42, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
    max_path_sum(grid)  # -> 82
