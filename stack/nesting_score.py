def nesting_score(string):
    """
    Write a function, nesting_score, that takes in a string of brackets as an argument. The function should return the score of the string according to the following rules:
    You may assume that the input only contains well-formed square brackets.
    [] = 1 points
    XY = m + n points, X Y - well-formed brackets, and m & n - their scores
    [S] = 2 * s points, s is the score of substring S
    n = length of string
    Time: O(n)
    Space: O(n)
    """
    stack = [0]
    for c in string:
        if c == "[":
            stack.append(0)
        else:
            popped = stack.pop()
            if popped > 0:
                # we have an open sequence, result is x2
                popped *= 2
            else:
                # we have a simple open pair, result is +1
                popped += 1
            top = stack.pop()
            stack.append(top + popped)

    return stack[-1]


if __name__ == "__main__":
    nesting_score("[]")  # -> 1
    nesting_score("[][][]")  # -> 3
    nesting_score("[[]]")  # -> 2
    nesting_score("[[][]]")  # -> 4
    nesting_score("[[][][]]")  # -> 6
    nesting_score("[[][]][]")  # -> 5
    nesting_score("[][[][]][[]]")  # -> 7
    nesting_score("[[[[[[[][]]]]]]][]")  # -> 129
    nesting_score("")  # -> 0