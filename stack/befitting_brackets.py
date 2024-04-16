def befitting_brackets(string):
    """
    Write a function, befitting_brackets, that takes in a string as an argument.
    The function should return a boolean indicating whether or not the string contains correctly matched brackets.
    You may assume the string contains only characters: ( ) [ ] { }
    n = length of string
    Time: O(n)
    Space: O(n)
    """
    def matches(obr, cbr):
        map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        return map[obr] == cbr

    closing = ")}]"
    stack = []
    for c in string:
        if c in closing:
            if not stack or not matches(stack.pop(), c):
                return False
        else:
            stack.append(c)
    return not stack


if __name__ == "__main__":
    befitting_brackets('(){}[](())')  # -> True
    befitting_brackets('({[]})')  # -> True
    befitting_brackets('[][}')  # -> False
    befitting_brackets('{[]}({}')  # -> False
    befitting_brackets('[]{}(}[]')  # -> False
    befitting_brackets('[]{}()[]')  # -> True
    befitting_brackets(']{}')  # -> False
    befitting_brackets('')  # -> True
    befitting_brackets("{[(}])")  # -> False
