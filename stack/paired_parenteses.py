def paired_parentheses(string):
    """
    Write a function, paired_parentheses, that takes in a string as an argument.
    The function should return a boolean indicating whether or not the string has well-formed parentheses.
    You may assume the string contains only alphabetic characters, '(', or ')'.
    n = length of string
    Time: O(n)
    Space: O(1)
    """
    stack = []
    for c in string:
        if c == ")":
            if not stack or stack.pop() != "(":
                return False
        elif c == "(":
            stack.append(c)
    return not stack

def paired_parentheses2(string):
    """
    n = length of string
    Time: O(n)
    Space: O(1)
    """
    counter = 0
    for c in string:

        if c == "(":
            counter += 1
        elif c == ")":
            counter -= 1
            if counter < 0:
                return False
    return counter == 0


if __name__ == "__main__":
    paired_parentheses("(david)((abby))")  # -> True
    paired_parentheses("()rose(jeff")  # -> False
    paired_parentheses(")(")  # -> False
    paired_parentheses("()")  # -> True
    paired_parentheses("(((potato())))")  # -> True
    paired_parentheses("(())(water)()")  # -> True
    paired_parentheses("(())(water()()")  # -> False
    paired_parentheses("")  # -> True
    paired_parentheses("))()")  # False