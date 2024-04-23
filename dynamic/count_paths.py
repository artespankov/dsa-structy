def count_paths(grid):
    """
    Write a function, count_paths, that takes in a grid as an argument.
    In the grid, 'X' represents walls and 'O' represents open spaces.
    You may only move down or to the right and cannot pass through walls.
    The function should return the number of ways possible to travel
    from the top-left corner of the grid to the bottom-right corner.

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
    return _count_paths(0, 0, grid, {})


def _count_paths(i, j, grid, memo):
    pos = (i, j)
    if pos in memo:
        return memo[pos]
    if i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 'X':
        return 0
    if i == len(grid)-1 and j == len(grid[0])-1:
        return 1
    # move right & down paths
    memo[pos] = _count_paths(i, j+1, grid, memo) + _count_paths(i+1, j, grid, memo)
    return memo[pos]


if __name__ == "__main__":
    grid = [
        ["O", "O"],
        ["O", "O"],
    ]
    count_paths(grid)  # -> 2
    grid = [
        ["O", "O", "X"],
        ["O", "O", "O"],
        ["O", "O", "O"],
    ]
    count_paths(grid)  # -> 5
    grid = [
        ["O", "O", "O"],
        ["O", "O", "X"],
        ["O", "O", "O"],
    ]
    count_paths(grid)  # -> 3
    grid = [
        ["O", "O", "O"],
        ["O", "X", "X"],
        ["O", "O", "O"],
    ]
    count_paths(grid)  # -> 1
    grid = [
        ["O", "O", "X", "O", "O", "O"],
        ["O", "O", "X", "O", "O", "O"],
        ["X", "O", "X", "O", "O", "O"],
        ["X", "X", "X", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O"],
    ]
    count_paths(grid)  # -> 0
    grid = [
        ["O", "O", "X", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "X"],
        ["X", "O", "O", "O", "O", "O"],
        ["X", "X", "X", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O"],
    ]
    count_paths(grid)  # -> 42
    grid = [
        ["O", "O", "X", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "X"],
        ["X", "O", "O", "O", "O", "O"],
        ["X", "X", "X", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "X"],
    ]
    count_paths(grid)  # -> 0
    grid = [
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
    ]
    count_paths(grid)  # -> 40116600
    grid = [
        ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
        ["X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
        ["X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "X", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
        ["X", "X", "X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
        ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
    ]
    count_paths(grid)  # -> 3190434
