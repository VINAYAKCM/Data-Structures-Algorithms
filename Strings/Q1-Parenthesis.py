#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#1. Open brackets must be closed by the same type of brackets.
#2. Open brackets must be closed in the correct order.
#3. very close bracket has a corresponding open bracket of the same type.

def isValid(s):
    opened = "([{"
    closed = ")]}"
    stack = []

    for char in s:
        if char in opened:
            stack.append(char)
        else:
            if not stack:
                return False

            top = stack.pop()

            if opened.index(top) != closed.index(char):
                return False

    return len(stack) == 0