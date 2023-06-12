def is_valid(s):
    if s == " " or len(s) % 2 != 0:
        return False
    open_close = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for chr in s:
        if chr in open_close:
            stack.append(chr)
        elif not stack or open_close[stack.pop()] != chr:
            return False
    return not stack


s = "()"
s1 = "()[]{}"
s2 = "(]"
s3 = "(("
print(is_valid(s1))
