def can_concat(s, words):
    return _can_concat(s, 0, words, {})


def _can_concat(s, start, words, memo):
    if start in memo:
        return memo[start]
    if start >= len(s):
        return True

    for w in words:
        if len(w) > (len(s) - start) + 1:
            continue
        i = 0
        str_matches = True
        while i < len(w):
            if w[i] != s[start+i]:
                str_matches = False
                break
            i += 1
        if str_matches:
            if _can_concat(s, start+len(w), words, memo):
                memo[start] = True
                return True
    memo[start] = False
    return False
