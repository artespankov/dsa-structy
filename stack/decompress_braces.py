def decompress_braces(string):
    """
    Write a function, decompress_braces, that takes in a compressed string as an argument.
    The function should return the string decompressed.
    The compression format of the input string is 'n{sub_string}',
    where the sub_string within braces should be repeated n times.
    You may assume that every number n is guaranteed to be an integer between 1 through 9.
    You may assume that the input is valid and the decompressed string will only contain alphabetic characters.
    s = length of string
    m = count of brace pairs
    Time: O((9^m) * s)
    Space: O((9^m) * s)
    """
    numbers = '1234567890'
    stack = []
    for c in string:
        if c == "}":
            segment = ''
            while stack:
                popped = stack.pop()
                if popped in numbers:
                   stack.append(int(popped) * segment)
                   break
                else:
                    segment = popped + segment
        elif c != "{":
            stack.append(c)
    return "".join(stack)


def decompress_braces2(string):
    numbers = '1234567890'
    stack = []
    for c in string:
        if c in numbers:
            stack.append(int(c))
        else:
            if c == "}":
                segment = ''
                while isinstance(stack[-1], str):
                    segment = stack.pop() + segment
                num = stack.pop()
                stack.append(num * segment)
            elif c != "{":
                stack.append(c)
    return "".join(stack)


if __name__ == "__main__":
    decompress_braces("2{q}3{tu}v")
    # -> qqtututuv
    decompress_braces("ch3{ao}")
    # -> chaoaoao
    decompress_braces("2{y3{o}}s")
    # -> yoooyooos
    decompress_braces("z3{a2{xy}b}")
    # -> zaxyxybaxyxybaxyxyb
    decompress_braces("2{3{r4{e}r}io}")
    # -> reeeerreeeerreeeerioreeeerreeeerreeeerio
    decompress_braces("go3{spinn2{ing}s}")
    # -> gospinningingsspinningingsspinningings
    decompress_braces("2{l2{if}azu}l")
    # -> lififazulififazul
    decompress_braces("3{al4{ec}2{icia}}")
    # -> alececececiciaiciaalececececiciaiciaalececececiciaicia